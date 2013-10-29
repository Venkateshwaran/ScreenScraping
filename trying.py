from bs4 import BeautifulSoup
import re
sentence = 'Hello, <code>This is the string i want to extract</code>' 	
print re.sub('<[^>]*>', ',',  sentence)
