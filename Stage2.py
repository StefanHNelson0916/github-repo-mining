from github import Github
import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime
import calendar

def importStageTwo(token, strRepo):
    g = Github(token)
    repo = g.get_repo(strRepo)

    file = 'data2.csv'
    #Delete file if it exists
    if os.path.exists(file) and os.path.isfile(file):
        os.remove(file)

    csvFile = open(file, 'w+', encoding='utf-8')

    csv_columns = ['commit', 'author', 'date', 'tree', 'url']

    writer = csv.DictWriter(csvFile, fieldnames=csv_columns)
    writer.writeheader()

    commits = repo.get_commits()

    for commit in commits:
        print(str(commit))
        writer.writerow(
            {
                "commit": commit.commit.sha,
                "author": commit.commit.author.name,
                "date": commit.commit.author.date,
                "tree":commit.commit.tree.url,
                "url": commit.commit.url,
            }
        )

    csvFile.close()

def visualizeStageTwo():
    read_file = open('data2.csv')
    csvReader = csv.DictReader(read_file)

    daysOfWeek = {
        "Sunday": 0,
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0
    }

    # Calculate number of commits by day of week from data file,
    for row in csvReader:
            dayofWeek = calendar.day_name[datetime.strptime(row["date"], "%Y-%m-%d %H:%M:%S").weekday()]
            daysOfWeek[str(dayofWeek)] += 1

    # Convert dictionary key/value into independent lists
    days = list(daysOfWeek.keys())
    daySum = list(daysOfWeek.values())

    # Plot Data
    plt.figure(figsize=(12.5, 10))
    plt.barh(days, daySum)
    plt.title('Commits by Weekday')
    plt.xlabel('Number of Commits')
    plt.ylabel('Day of Week')
    # Bar Values
    for index, value in enumerate(daySum):
        plt.text(value, index,
                 str(value))
    plt.savefig("commitTimeline.png")
    plt.show()
