
"""
from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "Account_number"
sheet["A2"] = "83746"
sheet["A3"] = "34859"
sheet["A4"] = "89898"
sheet["A5"] = "83874"
sheet["B1"] = "Account_name"
sheet["B2"] = "Amarr"
sheet["B3"] = "Garagedoor"
sheet["B4"] = "Automationdoor"
sheet["B5"] = "Sensordoor"
sheet["C1"] = "Datetime_created"
sheet["C2"] = "12-03-20"
sheet["C3"] = "15-03-20"
sheet["C4"] = "25-03-20"
sheet["C5"] = "03-04-20"

workbook.save(filename="hello.xlsx")
"""


"""
thisdict = {
  "Account_no": "837874,89384,89828,98984",
  "Account_name": "Amarr,Garagedoor,Nexus,Automationdoor",
  "Datetime_created": "12-03-20,15-03-20,25-03-20,03-04-20"
}
mydict = dict(thisdict)
print(mydict)
"""

"""
mycompany = {
  "company1" : {
    "Account_number" : "88769",
    "Account_name" : "Amarr",
    "Datetime_created" : "12-03-2020"
  },
  "company2" : {
    "Account_number" : "98765",
    "Account_name" : "Nexus",
    "Datetime_created" : "15-03-2020"
  },
  "company3" : {
    "Account_number" : "89766",
    "Account_name" : "Amazon",
    "Datetime_created" : "18-03-2020"
  }
}
print (mycompany)
"""

"""

company1 = {
    "Account_number" : "88769",
    "Account_name" : "Amarr",
    "Datetime_created" : "12-03-2020"
}
company2 = {
    "Account_number" : "98977",
    "Account_name" : "Nexus",
    "Datetime_created" : "15-03-2020"
}
company3 = {
    "Account_number" : "88769",
    "Account_name" : "Amazon",
    "Datetime_created" : "22-03-2020"
}

mycompany = {
  "company1" : company1,
  "company2" : company2,
  "company3" : company3
}
print (mycompany)

"""

import xlsxwriter as df

w = df.Workbook("D:\\excel\\a.xlsx")
w1 = w.add_worksheet('my')
w2 = w.add_worksheet('my1')
w1.write("A1","Account_number")
w1.write("B2","Account_name")
w1.write("C1","Datetime_created")
b = [75869,49586,84756]
c = ['Amarr','Nexus','Amazon']
d = ['12-03-2020','15-03-2020','20-03-2020']
for i in range (1,len(b)+1):
	w1.write(i,0,b[i-1])
	w1.write(i,1,c[i-1])
	w1.write(i,2,d[i-1])
w.close()

