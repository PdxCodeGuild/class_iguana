


import requests
import re


response = requests.get('http://www.gutenberg.org/files/58500/58500-0.txt')
text = response.text

regex = '[a-zA-Z’\'.]+'

words = re.findall(regex, text)

print(len(words))


