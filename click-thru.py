#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Analyzes the included data sets to report click-thru rate (CTR)
Builds a random forest classifier for clicked (1) or no-click (0)

Please see the README for info about the data tables
'''

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load the data tables into separate pandas DataFrames
emails = pd.read_csv('data/email_table.csv')
opened = pd.read_csv('data/email_opened_table.csv')
clicked = pd.read_csv('data/link_clicked_table.csv')

# Make a copy of the emails DataFrame to work with
emails_proc = emails.copy()

# Set the index to be the email's ID
emails_proc.set_index('email_id', drop=True, inplace=True)

# Define prefixes to use when creating dummy variables below
prefixes = {'email_text': 'text',
            'email_version': 'version',
            'weekday': 'weekday',
            'user_country': 'country'}

# Convert the categorical variables to dummies
emails_proc = pd.get_dummies(emails_proc,
                             prefix=prefixes,
                             columns=['email_text',
                                      'email_version',
                                      'weekday',
                                      'user_country'],
                             drop_first=False)

# Create new boolean columns to encode whether the user opened / clicked
# Copy these values to the working DataFrame
emails_proc['user_opened'] = int(0)
opened['user_opened'] = int(1)
opened.set_index('email_id', drop=True, inplace=True)
emails_proc.update(opened)

emails_proc['user_clicked'] = int(0)
clicked['user_clicked'] = int(1)
clicked.set_index('email_id', drop=True, inplace=True)
emails_proc.update(clicked)

# Display what proportion of emails were opened and clicked
num_opened = emails_proc['user_opened'].sum()
num_clicked = emails_proc['user_clicked'].sum()
total_emails = emails_proc.shape[0]

print(f'{num_opened / total_emails: 2.2f}% of the emails were opened')
print(f'{num_clicked / total_emails: 2.2f}% of the emails were clicked')
