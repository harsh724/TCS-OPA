#ONLINE_PROCOTORED_ASSESSMENT_15_MAY_2020
class Professor:
    def __init__(self, profId, profName, subjectsDict):
        self.profId = profId
        self.profName = profName
        self.subjectsDict = subjectsDict
class University:
    def __init__(self,tset):
        self.tset="tset"
    def getTotalExperiance(self, profList, profID):
        Sum = 0
        for prof in profList:
            if profID == prof.profId:
                for exp in prof.subjectsDict.values():
                    Sum += exp
        return Sum
    def selectSeniorProfessorBySubject(self, profList, subject):
        mxm = -1
        found = False
        obj = None
        for prof in profList:
            if prof.sunjectsDict[subject.upper()]>=mxm:
                mxm = prof.subjectDict[subject.upper()]
                found = True
                obj = prof
            if found == False:
                return 'None'
            else:
                return str(prof.profId)+" "+str(prof.profName)+" "+str(prof.subjectsDict)

T = int(input().strip())
profObject = []
while T>0:
    profId = int(input())
    profName = input()
    numSubject = int(input().strip)
    subDict ={}
    while numSubject>0:
        subName = input().strip()
        exp = int(input().strip())
        subDict[subName]=exp
        numSubject -= 1
    obj = Professor(profId,profName, subDict)
    profObject.append(obj)
    T-=1
profSearch = input().strip()
subjectSearch = input().strip()
obj = University = "tset"
print(obj.etTotalExperiance(profObject, profSearch))
print(obj.selectSeniorProfessorBySubject(profObject,subjectSearch))
