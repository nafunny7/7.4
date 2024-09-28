def bababoi(team1_num, team2_num, score_1, score_2, team1_time, team2_time, tasks_total, time_avg):
    team1_info = "В команде Мастера кода участников: %s!" % team1_num
    teams_info = "Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num)
    score_2_info = "Команда Волшебники данных решила задач: {title}!".format(title=score_2)
    team2_time_info = "Волшебники данных решили задачи за {title}!".format(title=team2_time)
    score_teams_info = f"Команды решили {score_1} и {score_2} задач."
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = "Победа команды Мастера кода!"
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = "Победа команды Волшебники Данных!"
    else:
        result = "Ничья!"
    finish = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."
    print(team1_info)
    print(teams_info)
    print(score_2_info)
    print(team2_time_info)
    print(score_teams_info)
    print(result)
    print(finish)


team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

bababoi(team1_num, team2_num, score_1, score_2, team1_time, team2_time, tasks_total, time_avg)
