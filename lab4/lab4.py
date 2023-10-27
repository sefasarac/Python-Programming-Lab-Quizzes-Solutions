totalStudent = 0
labCount = 0
hwCount =0
counts = input().split()
totalStudent=int(counts[0])
labCount=int(counts[1])
hwCount=int(counts[2])
id=0
students=[]
counter=0
# https://github.com/sefasarac
while(counter<totalStudent):
    infos=input()
    id=infos.split()[0]
    name=infos.split()[1]
    surname=infos.split()[2]
    totalLabGrades=0
    totalHomeworkGrades =0
    midtermNote=0
    finalNote=0
    kisareti = infos.split("<")
    labNotes = kisareti[1].split()
    for lab in labNotes:
        if(lab.isnumeric()):
            totalLabGrades+=int(lab)
    labAvg = totalLabGrades/labCount
    homeworkGrades=kisareti[2].split()
    for hw in homeworkGrades:
        if(hw.isnumeric()):
            totalHomeworkGrades+=int(hw)
    hwAvg=totalHomeworkGrades/hwCount
    midHelper=kisareti[3].split()
    midtermNote=0
    if(len(midHelper)!=1):
        midtermNote=int(midHelper[0])
    finalHelper=kisareti[4].split()
    finalNote=0
    if(len(finalHelper)!=1):
        finalNote=int(finalHelper[0])
    studentAvg=(labAvg/10)+(hwAvg/10)+(midtermNote/10)+(finalNote*8/10)
    studentAvg = round(studentAvg,3)
    students.append(str(id)+ " " + str(name + " " +surname)+ " " + str(studentAvg))
    counter+=1

found=False
requiredStudents=input().split()
for requiredStudent in requiredStudents:
    for student in students:
        number = student.split()[0]
        if(requiredStudent == number):
            found=True
            cikti=student.split()
            print(cikti[1] + " " +cikti[2]+ " " + "{:.2f}".format(float(cikti[3])))

if(found==False):
    print("None")
