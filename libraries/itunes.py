import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=20&term=" + sys.argv[1]
)

objec = response.json()

for result in objec["results"]:
    print(result["trackName"])
