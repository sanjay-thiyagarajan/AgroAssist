from django.shortcuts import render, redirect
import requests
from PIL import Image
from math import ceil
from predictor.models import ImagePicker
from predictor.core.agro_assist_pipeline import OnnxAgroAssistPipeline

def home(request):
    return render(request, 'predictor/index.html')

def select(request):
    if request.method == 'POST':
        url_input = request.POST.get('url_input')
        file_input = request.FILES.get('file_input')
        pipeline = OnnxAgroAssistPipeline(onnx_filename =  "predictor/models/agro_model.onnx")
        if (url_input == '') and (file_input == ''):
            return render(request, 'predictor/select.html', {'error': 'Please choose the image in either of the two formats'})
        else:
            if url_input:
                im = Image.open(requests.get(url_input, stream=True).raw)
                im.save('AgroAssist/static/img/url.jpg')
                result = pipeline.run(image_filename=im)
                return results(request, result, 'img/url.jpg')
            elif file_input:
                image = ImagePicker(image = file_input)
                image.save()
                im = Image.open(image.image)
                im.save('AgroAssist/static/img/url.jpg')
                result = pipeline.run(image_filename=im)
                return results(request, result, 'img/url.jpg')
    return render(request, 'predictor/select.html')

def results(request, result, url):

    return render(request, 'predictor/results.html', {'name': result['name'].capitalize(), 'score': result['score'], 'url': url})
