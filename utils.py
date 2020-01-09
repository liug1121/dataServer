# utils fun here
import json
def readJsonFromTxtFile(pathName):
    with open(pathName) as json_file:
        data = json.load(json_file)
    return data

