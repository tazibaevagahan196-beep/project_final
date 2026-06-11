import matplotlib.pyplot as plt


with open('logs.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()


data = []
for line in lines[1:]:
    if line.strip():
        parts = line.strip().split(';')
        data.append(parts)


days = {}
for rec in data:
    date = rec[0].split()[0]
    if date in days:
        days[date] = days[date] + 1
    else:
        days[date] = 1

plt.figure()
plt.bar(days.keys(), days.values())
plt.xticks(rotation=45)
plt.title('События по дням')
plt.tight_layout()
plt.savefig('events_by_day.png')


actions = {}
for rec in data:
    act = rec[2]
    if act in actions:
        actions[act] = actions[act] + 1
    else:
        actions[act] = 1

plt.figure()
plt.pie(actions.values(), labels=actions.keys(), autopct='%1.1f%%')
plt.title('Действия администраторов')
plt.savefig('actions_pie.png')


success = 0
failed = 0
for rec in data:
    if rec[2] == 'login':
        if rec[4] == 'True':
            success = success + 1
        else:
            failed = failed + 1

plt.figure()
plt.bar(['Успешные', 'Неудачные'], [success, failed])
plt.title('Результаты входов')
plt.savefig('logins.png')

print('Графики сохранены: events_by_day.png, actions_pie.png, logins.png')
