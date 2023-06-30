import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

track = sys.argv[1]
response = requests.get(f"http://itunes.apple.com/search?entity=song&limit=1&term={track}")
print(json.dumps(response.json(), indent=2))

