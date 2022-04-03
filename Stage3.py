from github import Github
import csv
import os

def importStageThree(token, strRepo):
    g = Github(token)
    repo = g.get_repo(strRepo)
    
    #Read commit SHAs from data2.csv
    read_file = open('data2.csv')
    csvreader = csv.DictReader(read_file)

    read_file_header = []
    read_file_header = next(csvreader)

    commits = []
    for row in csvreader:
        commits.append(row)

    read_file.close()

    #Delete file if it exists
    file = 'data3.csv'
    if (os.path.exists(file) and os.path.isfile(file)):
        os.remove(file)
    
    csvFile = open(file, 'w+', encoding='utf-8')

    csv_columns = ['path','size']

    writer = csv.DictWriter(csvFile, fieldnames=csv_columns)
    writer.writeheader()

    for row in commits:
        git_tree = repo.get_git_tree(row['commit'], True)
        git_tree_list = git_tree.tree

        for i in range(len(git_tree_list)):
            if (git_tree_list[i].size != None):
                writer.writerow(
                    {
                        "path" : git_tree_list[i].path,
                        "size" : git_tree_list[i].size
                    }
                )
    
    csvFile.close()
        
def visualizeStageThree():
    print('TBD')