#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from google_images_scraper import scraper
from urls_downloader import pkl_downloader
from data_transformation import tran

"""
Config

Change these to your liking

"""

queries_list = 'animals.txt'
data_path = '../raw_data/'
comp_path = '../data/'
errors = 'urls_errors.txt'


if __name__ == "__main__":
    scraper('animals.txt')
    pkl_downloader('animals_dict.pkl', data_path, errors)
    tran(data_path, comp_path)