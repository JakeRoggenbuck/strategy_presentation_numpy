import requests

end_point = "team/frc254"
url = f"https://www.thebluealliance.com/api/v3/{end_point}"

request = requests.get(url)
print(request)
