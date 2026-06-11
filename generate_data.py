import os
import random
from datetime import datetime, timedelta



logs = []
start = datetime(2026, 4, 1)

for i in range(30):
    ip = "203.0.113." + str(random.randint(1,100)) if i % 4 == 0 else "192.168." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
    action = ["вход", "создать_вм", "удалить_вм", "изменение данных"][random.randint(0,3)]
    success = False if (action == "вход" and i % 5 == 0) else True
    logs.append({
        "время": (start + timedelta(hours=i)).strftime("%Y-%m-%d %H:%M:%S"),
        "пользователь": "admin" + str(random.randint(1,4)),
        "действие": action,
        "источник_ip": ip,
        "успех": success
    })


f = open("logs.txt", "w", encoding="utf-8")
f.write("время;пользователь;действие;источник_ip;успех\n")
for rec in logs:
    f.write(f"{rec['время']};{rec['пользователь']};{rec['действие']};{rec['источник_ip']};{rec['успех']}\n")
f.close()

suspicious = sum(1 for rec in logs if rec["источник_ip"].startswith("203.0.113."))
failed_login = sum(1 for rec in logs if rec["действие"] == "вход" and not rec["успех"])
risk_score = suspicious * 2 + failed_login * 3
risk_level = "высокий" if risk_score > 25 else "средний" if risk_score > 12 else "низкий"


f = open("stats.txt", "w", encoding="utf-8")
f.write(f"Всего записей: {len(logs)}\n")
f.write(f"Подозрительных IP: {suspicious}\n")
f.write(f"Неудачных входов: {failed_login}\n")
f.write(f"Оценка риска: {risk_score}\n")
f.write(f"Уровень риска: {risk_level}\n")
f.close()

print(f"Расчёт завершён. Уровень риска: {risk_level}")

import pandas as pd

f = open("logs.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

headers = lines[0].strip().split(";")
data = [line.strip().split(";") for line in lines[1:] if line.strip()]
df = pd.DataFrame(data, columns=headers)

print("Таблица событий:")
print(df.head(30).to_string(index=False))

f = open("stats.txt", "r", encoding="utf-8")
print("\nСтатистика рисков:")
print(f.read())
f.close()

import matplotlib.pyplot as plt

f = open("logs.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()
data = [line.strip().split(";") for line in lines[1:] if line.strip()]




days = {}
for rec in data:
    date = rec[0].split()[0]
    days[date] = days.get(date, 0) + 1

plt.figure()
plt.bar(days.keys(), days.values())
plt.xticks(rotation=45)
plt.title("События по дням")
plt.tight_layout()
plt.savefig("диаграмма по дням.png")

actions = {}
for rec in data:
    act = rec[2]
    actions[act] = actions.get(act, 0) + 1

plt.figure()
plt.pie(actions.values(), labels=actions.keys(), autopct='%1.1f%%')
plt.title("Действия администраторов")
plt.savefig("круговая диаграмма.png")


success = sum(1 for rec in data if rec[2] == "вход" and rec[4] == "True")
failed = sum(1 for rec in data if rec[2] == "вход" and rec[4] == "False")

plt.figure()
plt.bar(["Успешные", "Неудачные"], [success, failed])
plt.title("Результаты входов")
plt.savefig("результаты входов.png")

print("Графики сохранены")
