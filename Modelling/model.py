#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tflearn
from tflearn.data_utils import image_preloader
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from tflearn.data_augmentation import ImageAugmentation
#import prediction_checker
from glob import glob
from PIL import Image
import numpy as np
import cgi


"""
Change this if needed
"""
def model_run(testimage):
	# data_path = '../data/';
	# X, Y = image_preloader(data_path + 'train/', image_shape = (32, 32), mode = 'folder');
	# X_valid, Y_valid = image_preloader(data_path + 'valid/', image_shape = (32, 32), mode = 'folder');


	 img_aug = ImageAugmentation()
	 img_aug.add_random_rotation(max_angle=25.)
	 img_aug.add_random_blur(sigma_max=3.);
	 network = input_data(shape=[None, 32, 32, 3],
	                    data_augmentation=img_aug)

	 network = conv_2d(network, 32, 3, activation='relu');

	 network = max_pool_2d(network, 2)

	 network = conv_2d(network, 64, 3, activation='relu')

	 network = conv_2d(network, 64, 3, activation='relu')

	 network = max_pool_2d(network, 2)

	 network = fully_connected(network, 128, activation='relu')

	 network = dropout(network, 0.5);

	 network = fully_connected(network, 6, activation='softmax')

	 network = regression(network, optimizer='adam',
	                     loss='categorical_crossentropy',
	                     learning_rate=0.001)

	 model = tflearn.DNN(network, tensorboard_verbose=0,best_val_accuracy = 0.6);
	 #model.fit(X, Y, n_epoch=50, shuffle=True, validation_set=(X_valid, Y_valid),show_metric=True, batch_size=10,snapshot_epoch=True)
	 #model.save('best_model//model')
	 model.load('C:\\Program Files\\Apache Software Foundation\\Tomcat 9.0\\webapps\\test\\WEB-INF\\cgi\\ClassificationProject\\modelling\\CNN32x32\\best_model\\model');a="C:\\Program Files\\Apache Software Foundation\\Tomcat 9.0\\webapps\\test\\"+testimage;im = Image.open(a);im = im.resize((32,32));pic = np.array(im);pic = pic.reshape(-1,32,32,3);pred = model.predict(pic);i = int(np.where(np.array(pred[0]) == np.max(pred))[0]);return sorted([c[17:] for c in glob('C:\\Program Files\\Apache Software Foundation\\Tomcat 9.0\\webapps\\test\\WEB-INF\\cgi\\ClassificationProject\\data\\valid\\*')])[i];
     
