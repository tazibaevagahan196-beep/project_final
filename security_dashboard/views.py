from django.shortcuts import render
import os

def index(request):
   
    logs_data = []
    if os.path.exists("logs.txt"):
        with open("logs.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            if lines:
                headers = lines[0].strip().split(";")
                for line in lines[1:]:
                    if line.strip():
                        values = line.strip().split(";")
                        logs_data.append(dict(zip(headers, values)))

    
    stats_text = ""
    if os.path.exists("stats.txt"):
        with open("stats.txt", "r", encoding="utf-8") as f:
            stats_text = f.read()

   
    charts = []
    for img in ["events_by_day.png", "actions_pie.png", "logins.png"]:
        if os.path.exists(img):
            charts.append(img)

    context = {
        "logs": logs_data[:10],
        "stats": stats_text,
        "charts": charts,
    }
    return render(request, "index.html", context)