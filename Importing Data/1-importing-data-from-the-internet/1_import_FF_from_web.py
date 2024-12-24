""" Importing flat files from the web: your turn!
You are about to import your first file from the web! The flat file you will import will be 'winequality-red.csv' from the University of California, Irvine's [Machine Learning repository](http://archive.ics.uci.edu/ml/index.html). The flat file contains tabular data of physiochemical properties of red wine, such as pH, alcohol content and citric acid content, along with wine quality rating.

The URL of the file is

    'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
    
After you import it, you'll check your working directory to confirm that it is there and then you'll load it into a pandas DataFrame. """

# Import package
from urllib.request import urlretrieve

# Import pandas
import pandas as pd

# Assign url of file: url
url ='https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Save file locally
urlretrieve(url,"winequality-red.csv")

# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())
