#ONLINE_PROCTORED_ASSESSMENT_22_MAY_2020
class doctor:
    def __init__(self, doctorId, doctorName, specialisation, cunsultationFee):
        self.doctorId = doctorId
        self.doctorName = doctorName
        self.specialisation = specialisation
        self.cunsultationFee = cunsultationFee
class Hospital:
    def __init__(self, doctorDB):
        self.doctorDB = doctorDB
    def searchByDoctorName(self, doctorName):
        l = []
        # c = 0
        for doc in doctorDB.values():
            if doctorName == doc.doctorName:
                l.append(doc)
                # c += 1
        # if c == 0:
        #     return "No Doctor Exists with the given DoctorName"
        return l

    def calculateConsultationFeeBySpecialization(self, specialiation):
        s = 0
        c2 = 0
        for doc in doctorDB.values():
            if specialiation == doc.specialisation:
                s += doc.cunsultationFee
                c2 += 1
        if c2 == 0:
            return "No Doctor with the given specialization"
        return s
    
   
n = int(input())
lst = []
for i in range(n):
    did = int(input())
    name = input()
    spec = input()
    fee = int(input())
    d = doctor(did,name,spec,fee)
    lst += [d]
searchname = input()
searchspec = input()
doctorDB = {}
c = 1
for i in lst:
    doctorDB[c] = i
    c+=1
h = Hospital(doctorDB)
rname = h.searchByDoctorName(searchname)
rspec = h.calculateConsultationFeeBySpecialization(searchspec)
if len(rname)==0:
    print("No Doctor Exists with the given DoctorName")
else:
    for i in rname:
        print(i.doctorId)
        print(i.doctorName)
        print(i.specialisation)
        print(i.cunsultationFee)
print(rspec)    
