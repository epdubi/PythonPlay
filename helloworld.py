import os.path
import requests
import json

def createFile(filePath):
    mode = "wt" if os.path.exists(filePath) else "a"
    file = open(filePath, mode)
    return file

def writeFileContents(file, content):
    file.write(content)
    file.close()

def getTodoTitles(todos):
    todoTitles = []
    for todo in todos:
        todoTitles.append(todo["title"])
    return ",".join(todoTitles)

def getTodoIds(todos):
    todoIds = []
    for todo in todos:
        todoIds.append(str(todo["id"]))
    return ",".join(todoIds)

try: 
    response = requests.get('https://jsonplaceholder.typicode.com/todos')

    if response.status_code == 200:
        responseFile = createFile("response.txt")
        writeFileContents(responseFile, response.text)

        todos = json.loads(response.text)

        titlesFile = createFile("titles.txt")
        titlesCsv = getTodoTitles(todos)
        writeFileContents(titlesFile, titlesCsv)

        todoIdsFile = createFile("todoIds.txt")
        todoIdsCsv = getTodoIds(todos)
        writeFileContents(todoIdsFile, todoIdsCsv)
    else:
        print('Oh no, we got a non 200 status code from our request :(')
except Exception as e:
    print(str(e))
