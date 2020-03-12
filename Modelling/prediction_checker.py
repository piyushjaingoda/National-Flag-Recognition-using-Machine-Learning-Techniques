#!/usr/bin/env python3
# -*- coding: utf-8 -*-
     
from glob import glob
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def pred_checker(model, path,testimage):
    #animal = np.random.choice(glob(path + 'valid/*'), 1)
    #a = np.random.choice(glob(animal[0] + '/*'))
    a="C:\\Program Files\\apache-tomcat-9.0.6\\webapps\\test\\"+testimage
    im = Image.open(a)
    im = im.resize((32,32))
    pic = np.array(im)
    
    pic = pic.reshape(-1,32,32,3)
    pred = model.predict(pic)
    
    i = int(np.where(np.array(pred[0]) == np.max(pred))[0])
    
    print('Prediction:', sorted([c[17:] for c in glob(path + 'valid/*')])[i])
    #print('Actual:', animal[0][17:])
    plt.imshow(im)
    plt.show()

