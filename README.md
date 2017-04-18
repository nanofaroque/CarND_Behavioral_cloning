# Behaviorial Cloning Project

[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

Overview
---
This repository contains starting files for the Behavioral Cloning Project.

In this project, I have used convolution neural network and deeplearing for behavioral cloing. I train, validate and test a model using Keras. The model will output a steering angle to an autonomous vehicle.

I have used the simulator provided by the udacity to collect all the data like images, steering angle etc. But in this project i have used only two informations like the image and the angle. After completing the trains, car drove the track in autonomous mode.

To meet specifications, the project will require submitting five files: </br>
* model.py (script used to create and train the model) </br>
* drive.py (script to drive the car - feel free to modify this file)</br>
* model.h5 (a trained Keras model)</br>
* a report writeup file in markdown format</br>
* video.mp4 (a video recording of your vehicle driving autonomously around the track for at least one full lap)

This README file describes how to output the video in the "Details About Files In This Directory" section.

Steps for the Projects and implementations. 
---
1. Submssion includes functional code Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing
 
```
python drive.py model.h5
```
2. model.py contains the whole implemetations of the network and find the model parmeter and save the model.
3. model.75 is the model file which has been used for autonomous driving. 
4. drive.py is helper class to drive the car by using saved model.
4. I started with very simpel model from the lecture but car was running around in a circular way. Then i started to use CNN and it improved the driving behavior. Below is the CNN structure i have used: 

Layer 1: 2D Convolution Layer 5x5 filter 24 output depth & 'relu' activation </br>
Layer 2: 2D Convolution Layer 5x5 filter 36 output depth & 'relu' activation </br>
Layer 3: 2D Convolution Layer 5x5 filter 48 output depth & 'relu' activation </br>
Layer 4: Dropout Layer Drop Probability 0.2 Layer</br>
 5: 2D Convolution Layer 3x3
 filter 64 output depth & 'relu' activation </br>
 Layer 6: Dropout Layer Drop 
 Probability 0.2 </br>
 Layer 7: 2D Convolution Layer 3x4 filter 64 output depth & 'relu' activation </br>
 Layer 8: Dropout Layer Drop Probability 0.2 </br>
 Layer 9: Flatten Layer </br>
 10: Dense Layer with 100 nodes Layer</br>
  11: Dense Layer with 50 nodes Layer </br>
  12: Dense Layer with 10 nodes Layer </br>
  13: Dense Layer with 1 node

### Dependencies
This lab requires:

* [CarND Term1 Starter Kit](https://github.com/udacity/CarND-Term1-Starter-Kit)

The lab enviroment can be created with CarND Term1 Starter Kit. Click [here](https://github.com/udacity/CarND-Term1-Starter-Kit/blob/master/README.md) for the details.

The following resources can be found in this github repository:
* drive.py
* video.py
* writeup_template.md

The simulator can be downloaded from the classroom. In the classroom, we have also provided sample data that you can optionally use to help train your model.

##Improvements:
Little more explanations of drive.py codebase and how it works
Basic guidelines of Opencv for future projects.