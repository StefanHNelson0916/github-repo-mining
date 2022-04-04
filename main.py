import sys
import Stage1
import Stage2
import Stage3
import Stage4

GITHUB_TOKEN = ''  # ENTER TOKEN HERE
REPO = "freeCodeCamp/freeCodeCamp"

if __name__ == '__main__':
    stageInput = -1
    importInput = -1

    while stageInput != 0 and stageInput != 1 and stageInput != 2 and stageInput != 3 and stageInput != 4:
        if stageInput == 0:
            sys.exit("User Exit")
        stageInput = int(input("Which stage would you like to run (0 = Exit, 1, 2, 3, 4): "))

    while importInput != 0 and importInput != 1 and importInput != 2:
        if importInput == 0:
            sys.exit("User Exit")
        importInput = int(input("Would you like to run the import process? (0 = Exit, 1 = Yes, 2 = No): "))

    if stageInput == 1:
        if importInput == 1:
            Stage1.importStageOne(GITHUB_TOKEN, REPO)

        Stage1.visualizeStageOne()
    elif stageInput == 2:
        if importInput == 1:
            Stage2.importStageTwo(GITHUB_TOKEN, REPO)

        Stage2.visualizeStageTwo()
    elif stageInput == 3:
        if importInput == 1:
            print('TODO')

        print('TODO')
    elif stageInput == 4:
        if importInput == 1:
            print('TODO')

        print('TODO')
