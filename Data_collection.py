# This code downloads a large number of XML files from a specific URL using the requests library in Python.
# The code creates a list of file URLs to download, and then iterates through the list, downloading each file.

import requests
import os
import urllib.request

url = "https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/"
headers = dict(Accept="*/*")
req = requests.get(url, headers=headers)
src = req.text

# generator url_list
url_list = []
for i in range(1, 1167):
    count = str(i).zfill(4)
    url = f"https://ftp.ncbi.nlm.nih.gov/pubmed/baseline/pubmed23n{count}.xml.gz"
    url_list.append(url)

if not os.path.exists('folderofarticles'):
    os.makedirs('folderofarticles')

    # Iterate through the list of file URLs and download each file
for url in url_list:
    file_name = os.path.basename(url)
    file_path = os.path.join('folderofarticles', file_name)
    urllib.request.urlretrieve(url, file_path)











