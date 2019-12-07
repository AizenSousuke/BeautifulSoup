'''
This python file is an example of how to use beautiful to extract text\images from a website.

Requirements:
Beautiful Soup,
requests library
python

Installation:
pip install beautifulsoup4
pip install requests
Run the py file
'''

import requests;
from bs4 import BeautifulSoup;

'''
# Open a file
with open("P:\DATABASE\APPLICATION\BeautifulSoup\Test\index.html") as fp:
          soup = BeautifulSoup(fp, "lxml");
'''
'''
# Find all 'p' in the file
result = soup.find_all('p');
print(result[2].text);

# Get the text
title = soup.header.h1.text;
print(title);
'''
# Get the html response by sending a request to the url
url = requests.get("https://www.iroiroonline.com/collections/all").content;
# Parse the html using beautiful soup
soup = BeautifulSoup(url, "lxml");

# Find all img recursively
output = soup.find_all('img', "", True);

# Add all the src links to the text buffer
text = 'These are generated: \n';
for i in output:
    print(i.text);
    text +='<img src=https:' + i['src'] + '>' + "\n";

# Open the file and write the results to it
with open('P:\DATABASE\APPLICATION\BeautifulSoup\Test\index.html', "w", encoding='utf-8') as file:
    file.write(str(text));