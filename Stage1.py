from github import Github
from matplotlib import pyplot as plt
from datetime import datetime, date, timedelta
import csv
import os

def importStageOne(token, strRepo):
    g = Github(token)
    repo = g.get_repo(strRepo)

    file = 'data1.csv'
    #Delete file if it exists
    if(os.path.exists(file) and os.path.isfile(file)):
        os.remove(file)

    csvFile = open(file, 'w+')

    csv_columns = ['state', 'opened_at', 'closed_at', 'labels', 'comments', 'assignees']

    writer = csv.DictWriter(csvFile, fieldnames=csv_columns)
    writer.writeheader()

    issues = repo.get_issues(state='all')

    for issue in issues:
        if issue.state == 'open':
            writer.writerow(
                {
                    "state": issue.state,
                    "opened_at": issue.created_at,
                    "closed_at": 0,
                    "labels": issue.labels,
                    "comments": issue.comments,
                    "assignees": issue.assignees
                }
            )
        else:
            writer.writerow(
                {
                    "state": issue.state,
                    "opened_at": issue.created_at,
                    "closed_at": issue.closed_at,
                    "labels": issue.labels,
                    "comments": issue.comments,
                    "assignees": issue.assignees
                }
            )

    csvFile.close()

def filterStageOne():
    read_file = open('data1.csv')
    csvreader = csv.DictReader(read_file)

    #Oldest issue for repo
    end_date = datetime(2014, 12, 24, 0, 0, 0).date()

    #Only add issues that were opened after the chosen timer period
    issues = []
    for row in csvreader:
        issue_opened_at = datetime.strptime(row['opened_at'], '%Y-%m-%d %H:%M:%S').date()
        # if issue_opened_at > start_date:
        issues.append(row)
    
    file = 'visualizationData1.csv'
    #Delete file if it exists
    if(os.path.exists(file) and os.path.isfile(file)):
        os.remove(file)

    csvFile = open(file, 'w+')

    csv_columns = ['date', 'num_open_issues','num_closed_issues']

    writer = csv.DictWriter(csvFile, fieldnames=csv_columns)
    writer.writeheader()
    
    date = datetime.now().date()
    delta = timedelta(days = 7)

    #For each day in the time period between start_date and end_date
    #For each issue read from data1.csv
    #If issue_opened_at is the same as start_date, add 1 to the number of open issues
    #If issue_closed_at is the same as end_date subtract, 1 to the number of open issues
    #Append to open_issue_count, the value of num_open_issues with the value of start_date
    print("Filtering Data...")
    while date >= end_date:

        num_open_issues = 0
        num_closed_issues = 0

        for issue in issues:
            #If the issue has a state value of open we need set issue_closed_at to datetime.now()
            if issue['state'] == 'open':
                issue_opened_at = datetime.strptime(issue['opened_at'], '%Y-%m-%d %H:%M:%S').date()
                issue_closed_at = datetime.now().date()
                
                if (date >= issue_opened_at) and (date <= issue_closed_at):
                    num_open_issues += 1
                if (date >= issue_opened_at) and (date >= issue_closed_at) :
                    num_closed_issues += 1
            else: 
                issue_opened_at = datetime.strptime(issue['opened_at'], '%Y-%m-%d %H:%M:%S').date()
                issue_closed_at = datetime.strptime(issue['closed_at'], '%Y-%m-%d %H:%M:%S').date()

                if (date >= issue_opened_at) and (date <= issue_closed_at):
                    num_open_issues += 1
                if (date >= issue_opened_at) and (date >= issue_closed_at) :
                    num_closed_issues += 1
        
        writer.writerow(
                {
                    "date": str(date),
                    "num_open_issues": num_open_issues,
                    "num_closed_issues": num_closed_issues
                }
            )
        date -= delta
 
    csvFile.close()    

def visualizeStageOne():

    #scatterCommentsTime()
    #filterStageOne()
    linegraph()

def linegraph():
    read_file = open('visualizationData1.csv')
    csvreader = csv.DictReader(read_file)

    data = []

    for row in csvreader:
        data.append(row)

    num_open_issues = []
    for row in data:
        num_open_issues.append(int(row['num_open_issues']))

    num_closed_issues = []
    for row in data:
        num_closed_issues.append(int(row['num_closed_issues']))

    dates = []
    for row in data:
        date = datetime.strptime(row['date'], '%Y-%m-%d').date()
        dates.append(date)

    fig, axs = plt.subplots(2)
    axs[0].plot(dates, num_open_issues)
    axs[0].set_title("Open Issues")
    axs[1].plot(dates, num_closed_issues)
    axs[1].set_title("Closed Issues")

    for ax in axs.flat:
        ax.set(xlabel='Date', ylabel='# of Issues')

    plt.show()

def scatterCommentsTime():

    x = []
    y = []

    read_file = open('data1.csv')
    csvReader = csv.DictReader(read_file)
    # Calculate number of commits by day of week from data file,
    for row in csvReader:
        # Only pull closed issues and remove outliers (comments > 60)
        if row["state"] == 'closed' and int(row["comments"]) < 60:
            dateOpen = datetime.strptime(row["opened_at"], "%Y-%m-%d %H:%M:%S")
            dateClose = datetime.strptime(row["closed_at"], "%Y-%m-%d %H:%M:%S")
            daysOpen = (dateClose - dateOpen).days
            if 1 < daysOpen < 366:
                x.append(int(row["comments"]))
                y.append(daysOpen)

    plt.figure(figsize=(20, 15))
    plt.scatter(x, y, alpha=0.5)
    plt.title("Number of Comments vs Number of Days Open")
    plt.xlabel("Number of Comments")
    plt.ylabel("Number of Days Open")

    plt.savefig("scatterCommentsTime.png")
    plt.show()