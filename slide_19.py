# Not runnable

team_data = pull_data_from_team(118)
scores = parse_team_data(team_data)

def get_average(scores):
    total = 0
    for num in scores:
        total += num
    return total / len(scores)

print(get_average(scores))
