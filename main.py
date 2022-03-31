from xml.etree.ElementTree import Comment
from github import Github
import csv

if __name__ == '__main__':
    g = Github(github_token)
    repo = g.get_repo("freeCodeCamp/freeCodeCamp")

csvFile = open('data.csv', 'w')

csv_columns = ['state','opened_at','closed_at','labels','comments','assignees']

writer = csv.DictWriter(csvFile, fieldnames=csv_columns)
writer.writeheader()

issues  = repo.get_issues(state='all')

for issue in issues:
    writer.writerow(
      {
            "state" : issue.state,
            "opened_at" : issue.created_at,
            "closed_at" : issue.closed_at,
            "labels" : issue.labels,
            "comments" : issue.comments,
            "assignees" : issue.assignees
        }  
    )

csvFile.close()