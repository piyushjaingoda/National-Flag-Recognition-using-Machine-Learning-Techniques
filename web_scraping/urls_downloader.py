#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from sys import argv
import os, urllib.request
import pickle
from tqdm import tqdm
from utils import create_path, load_obj

"""
Change this parameter to your desired path
"""


"""
Downloads a list of urls to a path and saves urls of errors to f
"""

def url_downloader(lst, path, f):
    opener = urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)

    i = 1
    
    for url in lst:
       
        try:
            urllib.request.urlretrieve(url, path + '/' + str(i))
            i = i + 1
            
        except Exception as inst:
            f = open(f, 'a')
            f.write(url + '\n')
            f.close()
            pass

def pkl_downloader(pkl, path, error_file):    
    create_path(path)
    
    d = load_obj(pkl)
    
    for name in tqdm(d):
        print('\n' + 'Downloading', name)
#        print(d[name])
        create_path(path + name)
        
        url_downloader(d[name], path + name, error_file)

if __name__ == "__main__":
    pkl_downloader(argv[1], argv[2], 'urls_errors.txt')