import cv2
import onnx
import numpy as np
import onnxruntime

class OnnxAgroAssistPipeline():
    """inference pipeline for leaf disease classification model on ONNX 
        Args:
            onnx_filename (str): path/to/onnx_model.onnx
    """
    def __init__(self, onnx_filename):
        
        self.onnx_model = onnx.load(onnx_filename)
        onnx.checker.check_model(self.onnx_model)
        self.session = onnxruntime.InferenceSession(onnx_filename)

        self.class_names = {
            0: 'healthy',
            1: 'multiple diseases',
            2: 'rust',
            3: 'scab'
        }

        self.mean = np.array([0.485, 0.456, 0.406]).reshape(1,1,3)
        self.std = np.array([0.229, 0.224, 0.225]).reshape(1,1,3)

    def normalize_image(self, x):
        x = (x - self.mean) / self.std
        return x

    def load_image(self, filename, size = (256,256)):
        filename = np.array(filename)
        im_original = cv2.cvtColor(filename, cv2.COLOR_BGR2RGB)/255.
        im_original_resized = cv2.resize(im_original, size)

        im_original_resized = self.normalize_image(im_original_resized)

        out =  np.expand_dims(im_original_resized.astype(np.float32).transpose(-1,0,1), axis = 0)

        return out

    def softmax(self, x):
        """Compute softmax values for each sets of scores in x."""
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum(axis=0) # only difference

    def parse_onnx_output(self, x):

        prob_map = self.softmax(x)
        result = self.class_names[np.argmax(prob_map)]
        prob_result = round(prob_map[np.argmax(prob_map)], 4)

        return {
            'name': result,
            'score': prob_result
        }

    def run(self, image_filename):

        img = self.load_image(filename = image_filename)
        onnx_input = {
            'input': img
        }
        output = self.session.run(None, onnx_input)[0].flatten()

        return self.parse_onnx_output(output)