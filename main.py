#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 19:14:16 2021

@author: haider

The data behind the Airbnb site is sourced from publicly available information from the Airbnb site.

The data has been analyzed, cleansed and scraped form 15 January 2019 to 12 January 2020.

Get the DATAIf you would like to do further analysis or produce alternate visualisations of the data, it is available below under a Creative Commons CC0 1.0 Universal (CC0 1.0) "Public Domain Dedication" license.


"""

import pandas as pd
from glob import glob

# Use glob to sort the list in assending
stock_files = sorted(glob('*.csv'))

# Concat all the separate CSV files into one dataframe
listing = pd.concat((pd.read_csv(file).assign(filename=file) for file in stock_files), ignore_index=True)

# %%
# Checking for missing values and any correlation between them
import missingno as msno

msno.matrix(listing)
msno.bar(listing)
msno.heatmap(listing)

#%%

# Data Cleaning

# selecting required colums only
data = listing[
    ['id', 'last_scraped', 'host_name', 'host_since', 'host_location', 'host_response_time', 'host_response_rate',
     'host_acceptance_rate', 'host_is_superhost', 'city', 'zipcode', 'latitude', 'longitude', 'property_type',
     'room_type', 'accommodates', 'bedrooms', 'bathrooms', 'beds', 'bed_type', 'price', 'weekly_price', 'monthly_price',
     'security_deposit', 'cleaning_fee', 'extra_people', 'minimum_nights', 'maximum_nights', 'number_of_reviews',
     'number_of_reviews_ltm', 'first_review', 'last_review', 'review_scores_rating', 'review_scores_accuracy',
     'review_scores_cleanliness', 'review_scores_checkin', 'review_scores_communication', 'review_scores_location',
     'review_scores_value', 'instant_bookable', 'reviews_per_month']]
# Percentage
data['host_response_rate'] = pd.to_numeric(data['host_response_rate'].apply(lambda x: str(x).replace('%', '').replace('nan', '')),errors='coerce') / 100
data['host_acceptance_rate'] = pd.to_numeric(data['host_acceptance_rate'].apply(lambda x: str(x).replace('%','').replace('nan','')),errors='coerce')/100

# converting object to date
data['host_since'] = pd.to_datetime(data['host_since'])
data['first_review'] = pd.to_datetime(data['first_review'])
data['last_review'] = pd.to_datetime(data['last_review'])



# %%

# Nimimum night can increase our average price. Becuase some people may have condition of 30 days as minum nigt thus thier price will be higher
#try to get price per night for all how you normalize that?