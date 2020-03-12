#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from glob import glob


def pred_checker(model, path):
    
    #country = Image.open("../../data/new_user/key.jpg")
    #im = Image.open(a)
    im = Image.open(open("key.jpg", 'rb'))
    im = im.resize((32,32))
    pic = np.array(im)
    
    pic = pic.reshape(-1,32,32,3)
    pred = model.predict(pic)
    
    i = int(np.where(np.array(pred[0]) == np.max(pred))[0])
    
    print('Prediction:',  sorted([c[17:] for c in glob(path + 'valid/*')])[i])
    print('Actual:Germany')
    plt.imshow(im)
    plt.show()

