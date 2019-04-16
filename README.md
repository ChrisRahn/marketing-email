A case study modeling the click-thru rate of an email marketing campaign.


##DATA

Data regarding every email sent as part of the pilot marketing campaign are stored in *data/email_table.csv*, with the following columns:

- email_id (INT): the ID# of the email that was sent. It is unique by email
- email_text (STRING): whether the email's text was the "long version" (4 paragraphs) or the "short version" (2 paragraphs)
- email_version (STRING): whether the email was personalized with the recipient's name or not
- hour (INT): the recipient's local time when the email was sent
- weekday (STRING): the day of the week the email was sent
- user_country (STRING): the country of the recipient, based on the IP address they used to register
- user_past_purchases (INT): how many items the recipient has bought in the past

The tables *data/email_opened_table.csv* and *data/link_clicked_table.csv* list the emails which were opened by the recipient and which had their link clicked at least once.
