def openFile(filename):
    try:
        f = open(filename, "r")
        return f
    except IOError:
        print("File Opening Error!")
def readnew(filename):
    f= open(filename)
    data = ""
    for line in f.readlines():
        data += line
        print (line)
def readAll(filename):
    f = open(filename)
    data = f.read()
    print(data)


filename="C:/Users/CC Server3/PycharmProjects/GUIPractice/CodeFiles/Demo.txt"
#filename = (filename.replace('\\', "/"))
#print(filename)
openFile(filename)
#readnew(filename)
#readAll(filename)