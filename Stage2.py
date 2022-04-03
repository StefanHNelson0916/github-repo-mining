from github import Github
import csv
import os

def importStageTwo(token, strRepo):
    g = Github(token)
    repo = g.get_repo(strRepo)

    file = 'data2.csv'
    #Delete file if it exists
    if(os.path.exists(file) and os.path.isfile(file)):
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
    print('TBD')