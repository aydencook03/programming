try:
    file = open("calculation.py", "r")
    contents = file.read()
    print(contents)
    def executeFileContents():
        exec(contents)
    executeFileContents()
finally:
    file.close()

try:
    newFile = open("NewFile.txt", "w+")
    newFile.write("Some Random Stuff")
    newFile.close()
    newFile = open("NewFile.txt", "r")
    for i in range(2):
        print(newFile.readlines(i))
finally:
    newFile.close()
