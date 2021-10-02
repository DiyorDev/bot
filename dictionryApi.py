import requests


from pprint import pprint as print
app_id = "62b446b5"
app_key = "c2fe6960887f53b88999q767283d7e34"
language = "en-gb"

word_id = "python"
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()

r = requests.get(url, headers={"api_id": app_id, "app_key": app_key})
print(r)

res = r.json()
print(res)