from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.cricbuzz.com/live-cricket-scores/49521/ind-vs-nz-3rd-odi-india-tour-of-new-zealand-2022')

print(r)
# print(r.content)
# print(r.url)
# print(r.status_code)
soup = BeautifulSoup(r.content,'html.parser')
print(soup.prettify())