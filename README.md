<p align="center">
  <img src = "images/symbol.png" width = "10%">
  <img src = "images/logo.png" width = "50%">
</p>



[![Docker](https://github.com/sanjay-thiyagarajan/AgroAssist/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/sanjay-thiyagarajan/AgroAssist/actions/workflows/docker-publish.yml)  [![](https://img.shields.io/badge/heroku-deployed-green)](https://agroassist.herokuapp.com/)


## What is it ? 
AgroAssist aims to leverage deep-learning to help farmers diagnose their crops and then seamlessly connect them to experts for further assistance through HubSpot CMS + CRM.  

![](https://github.com/sanjay-thiyagarajan/AgroAssist/blob/master/images/flowchart.jpg?raw=true)
## How does it work ?

### Initial diagnosis powered by deep-learning 
The user uploads a picture of the damaged leaves of the crop, and our deep-learning model analyses the image and determines the status of the crop. In order to make sure that the webapp stays light, we’ve used ONNX to deploy our PyTorch model into a heroku app. 

### Seamless short-term communication via HubSpot ChatFlow
We wanted to ensure that the user is not left in the dark after he/she determines the status of their crop. This is why we used Hubspot’s ChatFlow to help users to get in touch with experts right away for initial assistance. 

### Book an on-site visit using Hubspot Contact Form:
Our experts will visit your site and provide personalized assistance in diagnozing your crops

### Who are we ? 
We're a team of 3 undergrad students who love to build new products. We're planning to build AgroAssist to become an open source agro-tech platform which aims to provide service to farmers and help them get the most out of their crops by using state of the art deep-learning based methods.

## How did HubSpot help us ? 

* **Hubspot Form**: It enables the potential customers to seamlessly book an on-site visit fot further diagnosis of their crops. 
* **ChatFlow**: ChatFlow helps us establish contact with the customer rapidly and provide immediate assistance with their crop diseases. 
* **Hubspot Marketing Hub**: Managing contacts and scaled communication is a breeze, thanks to hubspot marketing hub. Sending out newsletters and featured updates has never been easier. 
* **Hubspot Contacts**: The contacts feature in HubSpot has helped us to easily keep track of and manage our contacts.
* **Hubspot Page Builder**: The page builder tool helped us build amazing webpages for our forms and the AgroAssist shop. 
