import requests
import pprint


key = "a253b1678c"
end_point = "team/frc254"
url = f"https://www.thebluealliance.com/api/v3/{end_point}"

request_headers = {"X-TBA-Auth-Key": key}
request = requests.get(url, headers=request_headers)

pprint.pprint(request.json())
