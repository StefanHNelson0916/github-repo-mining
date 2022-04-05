from github import Github
import csv
import os
import matplotlib.pyplot as plt
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

    csv_columns = ['commit', 'author', 'date', 'tree', 'url', 'tree_SHA']

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
                "tree_SHA": commit.commit.tree.sha
            }
        )

    csvFile.close()

def visualizeStageTwo():

    commitsByWeekday()
    graphMonth()
    graphYear()

def commitsByWeekday():
    daysOfWeek = {
        "Sunday": 0,
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0
    }

    read_file = open('data2.csv', encoding='utf-8')
    csvReader = csv.DictReader(read_file)
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

def graphYear():
    read_file = open('data2.csv', encoding='utf-8')
    csvReader = csv.DictReader(read_file)

    byYear = {
        "2022": 0,
        "2021": 0,
        "2020": 0,
        "2019": 0
    }

    # Calculating number of commits by month
    for row in csvReader:
        yearL = datetime.strptime(row["date"], "%Y-%m-%d %H:%M:%S").year
        byYear[str(yearL)] += 1
    years = list(byYear.keys())
    yearSum = list(byYear.values())

    # Plot for the years
    plt.barh(years, yearSum)
    plt.title("Commits by Year")
    plt.xlabel("Number of Commits")
    plt.ylabel("Year")
    plt.savefig("graphByYear.png")
    plt.show()


def graphMonth():
    read_file = open('data2.csv', encoding='utf-8')
    csvReader = csv.DictReader(read_file)

    byMonth = {
        'January': 0,
        'February': 0,
        'March': 0,
        'April': 0,
        'May': 0,
        'June': 0,
        'July': 0,
        'August': 0,
        'September': 0,
        'October': 0,
        'November': 0,
        'December': 0
    }

    # Calculating number of commits by month
    for row in csvReader:
        monthL = calendar.month_name[datetime.strptime(row["date"], "%Y-%m-%d %H:%M:%S").month]
        byMonth[str(monthL)] += 1
    months = list(byMonth.keys())
    monthSum = list(byMonth.values())

    # Plot for the months
    plt.barh(months, monthSum)
    plt.title("Commits by Month")
    plt.xlabel("Number of Commits")
    plt.ylabel("Month")
    plt.savefig("commitsByMonth.png")
    plt.show()