#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PIL import Image,ImageFile

from glob import glob
import os
import cairosvg
from tqdm import tqdm
from utils import create_path, filetype
from sys import argv

def img_converter(path, old_name):
    if filetype(old_name) in ['ASCII', 'HTML', 'MS', 'PC', 'RIFF', 'exported', 'SVG']:         
        #print(old_name, filetype(old_name))
        with open('skipped_files.txt', 'a') as f:
            f.write(old_name + '\n')
        return
    
    im = Image.open(old_name)
    
    if not im.mode == 'RGB':
        Image.open(old_name).convert('RGB').save(old_name, 'JPEG')
        im = Image.open(old_name)
    
    out = im.resize((256, 256))
    return out
    
    
def tran(old_path, new_path):

    i = len(old_path)
    pic_names = {}

    for animal in [name[i+1:] for name in glob(old_path + '/*')]:
        pic_names[animal] = glob(old_path + '/' + animal + '/*')
    
    for animal in tqdm(pic_names):
        i = 1
        create_path(new_path + animal)
    
    for pic in pic_names[animal]:
        #print(animal, pic)
        out = img_converter(old_path, pic)
        out.save(new_path + animal + '/' + str(i) + '.jpg', "JPEG")
        i = i + 1

if __name__ == "__main__":
    tran(argv[1], argv[2])
    
    