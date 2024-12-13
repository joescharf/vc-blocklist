import re
import requests

# Read the webpage at https://a16z.com/portfolio/
response = requests.get('https://a16z.com/portfolio/')
content = response.text

# replace &quot; with "
content = content.replace('&quot;', '"')

# Use regex to find all company_url attributes
company_urls = re.findall(r'"company_url":\s*"([^"]+)"', content)

# Write the URLs to a new file
with open('./a16z/a16_portco_domains.txt', 'w') as file:
    for url in company_urls:
        # remove the escaping
        url = url.replace('\\', '')
        # Just return the domain
        url = url.split('/')[2]
        # remove www.
        url = url.replace('www.', '')
        # convert to lowercase
        url = url.lower()
        file.write("0.0.0.0 " + url + '\n')