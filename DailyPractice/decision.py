import random

consultancy = ["JavaDeveloper","Data Engineer","Pyhton+AWS","PythonFullStack"]
Fulltime = ["JavaDeveloper","Data Engineer","Pyhton+AWS","PythonFullStack"]

for j in range(3):
    consultancyDict = {position: 0 for position in consultancy}
    FulltimeDict = {position: 0 for position in Fulltime}
    for i in range(21):
        opinion1 = random.choice(consultancy)
        # print("opinion1",opinion1)
        opinion2 = random.choice(Fulltime)
        # print("opinion2",opinion2)

        consultancyDict[opinion1] += 1
        FulltimeDict[opinion2] += 1



    print("consultancyDict",consultancyDict)
    print("FulltimeDict",FulltimeDict)