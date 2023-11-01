class School:
    def __init__(self,name,rollnumber,section,class_school,fav_sub):
        self.name=name
        self.rollnumber=rollnumber
        self.section=section
        self.class_school=class_school
        self.fav_sub=fav_sub
    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.rollnumber}, Section: {self.section}, Class: {self.class_school}, Favorite Subject: {self.fav_sub}"

student_detail=School('Nikhil',306,'A',7,'SCIENCE')
student_detail2=School('raja',307,'A',7,'MATHS')
student_detail3=School('goopi',308,'A',7,'chemistry')
student_detail4=School('jhon',320,'A',7,'drawing')
student_detail5=School('ch',319,'A',7,'TOM')
student_detail6=School('robo',317,'A',7,'DOM')
student_detail7=School('ssss',310,'A',7,'Thermo dynamics')
student_detail8=School('abhi',302,'A',7,'Heat Tranfer')
student_detail9=School('aditya',304,'A',7,'DMM-2')
student_detail10=School('vamsi',1,'A',7,'ALL_sub')
print(student_detail)
print(student_detail2)
print(student_detail3)
print(student_detail4)
print(student_detail5)
print(student_detail6)
print(student_detail7)
print(student_detail8)
print(student_detail9)
print(student_detail10)