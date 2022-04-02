from github import Github
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
        print(str(issue) + " " + str(issue.state))
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

def visualizeStageOne():
    print('TBD')