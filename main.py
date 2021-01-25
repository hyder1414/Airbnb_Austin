#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from glob import glob

# merging multiple files with same column
# Use glob to sort the list in assending
stock_files = sorted(glob('*.csv'))

# Concat all the separate CSV files into one dataframe
listing = pd.concat((pd.read_csv(file).assign(filename=file) for file in stock_files), ignore_index=True)

# converting object to date
data['host_since'] = pd.to_datetime(data['host_since'])
data['first_review'] = pd.to_datetime(data['first_review'])
data['last_review'] = pd.to_datetime(data['last_review'])

# convert percentages to numeric from range 0 to 1
listing['host_response_rate'] = pd.to_numeric(listing['host_response_rate'].apply(lambda x: str(x).replace('%', '').replace('N/A', '')), errors='coerce') / 100
listing['host_acceptance_rate'] = pd.to_numeric(listing['host_acceptance_rate'].apply(lambda x: str(x).replace('%', '').replace('N/A', '')), errors='coerce') / 100

# convert currency to numeric
listing['price'] = pd.to_numeric(listing['price'].apply(lambda x: str(x).replace('$', '').replace(',', '')),errors='coerce')
listing['weekly_price'] = pd.to_numeric(listing['weekly_price'].apply(lambda x: str(x).replace('$', '').replace(',', '')), errors='coerce')
listing['monthly_price'] = pd.to_numeric(listing['monthly_price'].apply(lambda x: str(x).replace('$', '').replace(',', '')),errors='coerce')
listing['security_deposit'] = pd.to_numeric(listing['security_deposit'].apply(lambda x: str(x).replace('$', '').replace(',', '')),errors='coerce')
listing['cleaning_fee'] = pd.to_numeric(listing['cleaning_fee'].apply(lambda x: str(x).replace('$', '').replace(',', '')),errors='coerce')
listing['extra_people'] = pd.to_numeric(listing['extra_people'].apply(lambda x: str(x).replace('$', '').replace(',', '')),errors='coerce')

# normalize review score to fit to value between 0 to 1
listing['review_scores_rating'] = pd.to_numeric(listing['review_scores_rating'], errors='coerce')/100
listing['review_scores_accuracy'] = pd.to_numeric(listing['review_scores_accuracy'], errors='coerce')/10
listing['review_scores_cleanliness'] = pd.to_numeric(listing['review_scores_cleanliness'], errors='coerce')/10
listing['review_scores_checkin'] = pd.to_numeric(listing['review_scores_checkin'], errors='coerce')/10
listing['review_scores_communication'] = pd.to_numeric(listing['review_scores_communication'], errors='coerce')/10
listing['review_scores_location'] = pd.to_numeric(listing['review_scores_location'], errors='coerce')/10
listing['review_scores_value'] = pd.to_numeric(listing['review_scores_value'], errors='coerce')/10

# convert true/false to codes
cleanup_colval = {
                    'host_is_superhost' : {'f':0, 't':1},
                    'host_identity_verified': {'f':0, 't':1},
                    'is_location_exact': {'f':0, 't':1},
                    'instant_bookable': {'f':0, 't':1},
                    'require_guest_profile_picture': {'f':0, 't':1},
                    'require_guest_phone_verification': {'f':0, 't':1},
                    'host_has_profile_pic': {'f':0, 't':1},
                    'is_business_travel_ready': {'f':0, 't':1}
                }
listing.replace(cleanup_colval, inplace=True)

