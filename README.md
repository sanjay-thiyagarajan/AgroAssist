# AgroAssist 

[![Docker](https://github.com/sanjay-thiyagarajan/AgroAssist/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/sanjay-thiyagarajan/AgroAssist/actions/workflows/docker-publish.yml)  [![](https://img.shields.io/badge/heroku-deployed-green)](https://agroassist.herokuapp.com/)

![](https://github.com/Mayukhdeb/agro-temp/raw/main/images/light_banner_large.png)

## What is it ? 
Agro Assist is a deep-learning based crop infection diagnosis tool that aims to automate the preliminary stages of crop infection diagnosis and helps connect the farmers to the experts seamlessly using HubSpot CMS + CRM

## How does it work ?

### Initial diagnosis powered by deep-learning 
The user uploads a picture of the damaged leaves of the crop, and our deep-learning model analyses the image and determines the status of the crop. In order to make sure that the webapp stays light, we’ve used ONNX to deploy our PyTorch model into a heroku app. 

### Seamless short-term communication via HubSpot ChatFlow
We wanted to ensure that the user is not left in the dark after he/she determines the status of their crop. This is why we used Hubspot’s ChatFlow to help users to get in touch with experts right away for initial assistance. 

### Book an on-site visit using Hubspot Contact Form:
Our experts will visit your site and provide personalized assistance in diagnozing your crops


