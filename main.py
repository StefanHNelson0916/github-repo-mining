from xml.etree.ElementTree import Comment

import Stage1
import Stage2
import Stage3
import Stage4

GITHUB_TOKEN = '' #ENTER TOKEN HERE
REPO = "freeCodeCamp/freeCodeCamp"

if __name__ == '__main__':
    #Stage1.importStageOne(GITHUB_TOKEN, REPO)
    #Stage2.importStageTwo(GITHUB_TOKEN, REPO)
    #Stage3.importStageThree(GITHUB_TOKEN, REPO)

    Stage1.filterStageOne()
    Stage1.visualizeStageOne()