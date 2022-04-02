from xml.etree.ElementTree import Comment

import Stage1
import Stage2
import Stage3
import Stage4

GITHUB_TOKEN = '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'
REPO = "freeCodeCamp/freeCodeCamp"

if __name__ == '__main__':
    Stage1.importStageOne(GITHUB_TOKEN, REPO)