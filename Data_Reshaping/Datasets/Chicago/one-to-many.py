# Starting with the licenses table on the left, merge it to the biz_owners table on the column account,
# and save the results to a variable named licenses_owners.
# Group licenses_owners by title and count the number of accounts for each title. Save the result as counted_df
# Sort counted_df by the number of accounts in descending order, and save this as a variable named sorted_df.
# Use the .head() method to print the first few rows of the sorted_df.

import pandas as pd

licenses = pd.read_pickle('licenses.p')
biz_owners = pd.read_pickle('business_owners.p')

licenses_owners = licenses.merge(biz_owners, on= 'account')
counted_df = licenses_owners.groupby('title').agg({'account':'count'})


sorted_df = counted_df.sort_values('account', ascending= False)
print(licenses_owners)
print(sorted_df.head())

