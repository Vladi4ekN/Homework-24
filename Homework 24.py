# Переменные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / (team1_num + team2_num)


# Использование %
line1 = "В команде Мастера кода участников: %d !" % team1_num
print(line1)

line2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(line2)

# Использование format()
line3 = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(line3)

line4 = "Волшебники данных решили задачи за {} с !".format(team2_time)
print(line4)

# Использование f-строк
line5 = f"Команды решили {score_1} и {score_2} задач."
print(line5)

line6 = f"Результат битвы: {challenge_result}!"
print(line6)

line7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.2f} секунды на задачу!"
print(line7)
