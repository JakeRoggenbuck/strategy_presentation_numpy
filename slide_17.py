import requests


def pull_data_from_team(team_num):
    key = "12345"
    end_point = f"team/frc{team_num}/matches/2017"
    url = f"https://www.thebluealliance.com/api/v3/{end_point}"

    request_headers = {"X-TBA-Auth-Key": key}
    request = requests.get(url, headers=request_headers)

    data = request.json()
    return len(data)


pull_data_from_team(254) # 79
pull_data_from_team(1678) # 111
pull_data_from_team(118) # 123
