""" Performing HTTP requests in Python using requests
Now that you've got your head and hands around making HTTP requests using the urllib package, you're going to figure out how to do the same using the higher-level requests library. You'll once again be pinging DataCamp servers for their 
    
    "http://www.datacamp.com/teach/documentation" 

page.

Note that unlike in the previous exercises using urllib, you don't have to close the connection when using requests! """

# Import package
import requests

# Specify the url: url
url = "http://www.datacamp.com/teach/documentation"

# Packages the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response: text
text= r.text

# Print the html
print(text)
