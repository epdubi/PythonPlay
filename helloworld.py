import os.path
import requests

def writeFileContents(file, responseText):
    file.write(responseText)
    file.close()

try: 
    response = requests.get('https://jsonplaceholder.typicode.com/todos')

    if response.status_code == 200:
        filePath = "response.txt"

        if os.path.exists(filePath):
            file = open(filePath, "wt")
            writeFileContents(file, response.text)
        else:
            file = open(filePath, "a")
            writeFileContents(file, response.text)
    else:
        print('Oh no, we got a non 200 status code from our request :(')
except Exception as e:
    print(str(e))
