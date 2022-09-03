# Ensure that prereqs are installed:
#   pip install bs4
#   pip install requests
#   (if needed):
#       pip install lxml

import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.google.com")

# Ensure we receive 200 response to indicate the page is valid
print(result.status_code)

# Check HTTP header of the website to verify we accessed the correct webpage
print(result.headers)

# Store page content of website accessed to a variable:
src = result.content

# Create BS4 object based on the source variable created above:
soup = BeautifulSoup(src, 'lxml')

# Access specific information from BS4 object:
links = soup.find_all("a")
print(links)
print("\n")

# We can use text function to access content between anchor tags
for link in links:
    if "About" in link.text:
        print(link)
        print(link.attrs['href'])