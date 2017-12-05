import os
import random

class Person:
    def __str__(self):
        column_width = 15
        express = ""
        seperator = "    "
        express = self.sex +' '*(column_width-len(self.sex))+ seperator
        express += self.age +' '*(column_width-len(self.age))+ seperator
        express += self.area +' '*(column_width-len(self.area))+ seperator
        express += self.edu +' '*(column_width-len(self.edu))+ seperator
        express += self.marriage +' '*(column_width-len(self.marriage))+ seperator
        express += self.job +' '*(column_width-len(self.job))+ seperator
        express += self.employ +' '*(column_width-len(self.employ))+ seperator
        express += self.home_salary +' '*(column_width-len(self.home_salary))+ seperator
        express += self.medical +' '*(column_width-len(self.medical))+ seperator
        express += self.compliance +' '*(column_width-len(self.compliance))
        return express
    def get(self, section):
        if section == "sex":
            return self.sex
        elif section == "age":
            return self.age
        elif section == "area":
            return self.area
        elif section == "edu":
            return self.edu
        elif section == "marriage":
            return self.marriage
        elif section == "job":
            return self.job
        elif section == "employ":
            return self.employ
        elif section == "home_salary":
            return self.home_salary
        elif section == "medical":
            return self.medical
        elif section == "compliance":
            return self.compliance
    def set(self, section, value):
        if section == "sex":
            self.sex = value
        elif section == "age":
            self.age = value
        elif section == "area":
            self.area = value
        elif section == "edu":
            self.edu = value
        elif section == "marriage":
            self.marriage = value
        elif section == "job":
            self.job = value
        elif section == "employ":
            self.employ = value
        elif section == "home_salary":
            self.home_salary = value
        elif section == "medical":
            self.medical = value
        elif section == "compliance":
            self.compliance = value
            
    sex=""
    age=""
    area=""
    edu=""
    marriage=""
    job=""
    employ=""
    home_salary=""
    medical=""
    compliance=""
    
def random_fill(persons_list, num, section, value):
    index_range = len(persons_list) - 1
    fill_count = 0
    random.seed()
    for i in range(num):
        index = random.randint(0, index_range)
        if persons_list[index].get(section) == "":
            persons_list[index].set(section,value)
            fill_count = fill_count + 1
        else:
            index = random.randint(0, index_range)
            if persons_list[index].get(section) == "":
                persons_list[index].set(section,value)
                fill_count = fill_count + 1
            else:
                for n in range(index_range):
                    if persons_list[index].get(section) == "":
                        persons_list[index].set(section,value)
                        fill_count = fill_count + 1
    return fill_count

def rest_fill(persons_list, section, value):
    index_range = len(persons_list)
    for n in range(index_range):
        if persons_list[n].get(section) == "":
            persons_list[n].set(section,value)
    
total = 714
persons = []
for i in range(total):
    persons.append(Person())
    
#sex
male = 340
random_fill(persons, male, "sex", "Male")
rest_fill(persons,"sex", "Female")
                
#age
below_45 = 265
between45_60 = 241
upon_60 = 208
random_fill(persons, below_45, "age", "<45")
random_fill(persons, between45_60, "age", "45-60")
rest_fill(persons,"age", ">60")
        
#area   
country = 356
random_fill(persons, country, "area", "country")
rest_fill(persons,"area", "city")

#edu
bachelar = 391
#320-city, 71-country
city_bachelar = 320
country_bachelar = 71
#find out the city and country list
persons_city = []
persons_country = []
for n in range(total):
    if persons[n].area == "country":
        persons_country.append(persons[n])
    else:
        persons_city.append(persons[n])
number_of_persons_country = len(persons_country)
number_of_persons_city = len(persons_city)
#print("number of persons in country is 356: %d" % number_of_persons_country)
#print("number of persons in city is 358: %d" % number_of_persons_city)
random_fill(persons_city, city_bachelar, "edu", "bachelar")
random_fill(persons_country, country_bachelar, "edu", "bachelar")
rest_fill(persons,"edu", "hign school")
        
#marriage
not_married = 318
random_fill(persons, not_married, "marriage", "not_married")
rest_fill(persons,"marriage", "married")
        
#job
job_A = 97
job_B = 107
job_C = 113
job_D = 101
job_E = 117
job_F = 98
random_fill(persons, job_A, "job", "Job_A")
random_fill(persons, job_B, "job", "Job_B")
random_fill(persons, job_C, "job", "Job_C")
random_fill(persons, job_D, "job", "Job_D")
random_fill(persons, job_E, "job", "Job_E")
random_fill(persons, job_F, "job", "Job_F")
rest_fill(persons,"job", "Job_G")

#employ
unemployed = 282
retired = 212
onjob = 220
#unemployed: 40 in city , 242 in country
#retired = 191 in >60, 21 in 45_60
unemployed_city = 40
unemployed_country = 242
retired_upon60 = 191
retired_45_60 = 21

persons_upon_60 = []
persons_45_60 = []
for n in range(total):
    if persons[n].age == "45-60":
        persons_45_60.append(persons[n])
    elif persons[n].age == ">60":
        persons_upon_60.append(persons[n])
number_of_persons_upon_60 = len(persons_upon_60)
number_of_persons_45_60 = len(persons_45_60)
#print("number of persons >60:%d 45-60:%d" % (number_of_persons_upon_60, number_of_persons_45_60))
random_fill(persons_upon_60, retired_upon60, "employ", "retired")
random_fill(persons_45_60, retired_45_60, "employ", "retired")
unemployed_set_count = random_fill(persons_city, unemployed_city, "employ", "unemployed")
unemployed_set_count = unemployed_set_count + random_fill(persons_country, unemployed_country, "employ", "unemployed")
D_unemployed = unemployed - unemployed_set_count
random_fill(persons, D_unemployed, "employ", "unemployed")
rest_fill(persons, "employ", "OnJob")

#home_salary
#<2000 and 2001-3500 all in country, >5000 all in city
#the rest of home_salary will be filled as "3501-5000"
salary_less_2000 = 162
salary_2001_3500 = 180
salary_3501_5000 = 187
salary_more_5000 = 185
random_fill(persons_city, salary_more_5000, "home_salary", ">5000")
random_fill(persons_country, salary_less_2000, "home_salary", "<2000")
random_fill(persons_country, salary_2001_3500, "home_salary", "2001-3500")
rest_fill(persons, "home_salary", "3501-5000")
        
#medical
#medicalA all in city, medicalC all in country
#the rest are medicalB
medicalA = 117
medicalB = 279
medicalC = 318
random_fill(persons_city, medicalA, "medical", "medicalA")
random_fill(persons_country, medicalC, "medical", "medicalC")
rest_fill(persons,"medical", "medicalB")

#compliance A B C
#Male: 37A;60B;243C
#Female:56A;121B;197C
persons_Male = []
persons_Female = []
for n in range(total):
    if persons[n].sex == "Male":
        persons_Male.append(persons[n])
    else:
        persons_Female.append(persons[n])
random_fill(persons_Male, 37, "compliance", "complianceA")
random_fill(persons_Male, 60, "compliance", "complianceB")
rest_fill(persons_Male,"compliance", "complianceC")

random_fill(persons_Female, 56, "compliance", "complianceA")
random_fill(persons_Female, 121, "compliance", "complianceB")
rest_fill(persons_Female,"compliance", "complianceC")

#age-compliance        
persons_45 = []
persons_45_60 = []
persons_60 = []
for i in range(total):
    if persons[i].age == "<45":
        persons_45.append(persons[i])
    elif persons[i].age == "45-60":
        persons_45_60.append(persons[i])
    else:
        persons_60.append(persons[i])
number_of_persons_45 = len(persons_45)
number_of_persons_45_60 = len(persons_45_60)
number_of_persons_60 = len(persons_60)

number_of_complianceA = 0
number_of_complianceB = 0
number_of_complianceC = 0
complianceA = []
complianceB = []
complianceC = []
def reset_compliance():
    global number_of_complianceA
    global number_of_complianceB
    global number_of_complianceC
    global complianceA
    global complianceB
    global complianceC
    
    number_of_complianceA = 0
    number_of_complianceB = 0
    number_of_complianceC = 0
    complianceA = []
    complianceB = []
    complianceC = []

    for i in range(total):
        if persons[i].compliance == "complianceA":
            complianceA.append(persons[i])
            number_of_complianceA = number_of_complianceA + 1
        elif persons[i].compliance == "complianceB":
            complianceB.append(persons[i])
            number_of_complianceB = number_of_complianceB + 1
        else:
            complianceC.append(persons[i])
            number_of_complianceC = number_of_complianceC + 1    
reset_compliance()
#print("A:%d  B:%d  C:%d" % (number_of_complianceA, number_of_complianceB, number_of_complianceC))

section=""
compliance_statistic = 0
compliance_condition = ""
def adjust_complianceA():
    global number_of_complianceA
    global number_of_complianceB
    global number_of_complianceC
    global complianceA
    global complianceB
    global complianceC
    global section
    global compliance_statistic
    global compliance_condition
    
    tmp_compliance_statistic = 0
    for i in range(number_of_complianceA):
        if complianceA[i].get(section) == compliance_condition:
            if tmp_compliance_statistic < compliance_statistic:
                tmp_compliance_statistic = tmp_compliance_statistic + 1
            else:
                complianceA[i].compliance = "complianceB"
                #print("change A to B.")
    if tmp_compliance_statistic < compliance_statistic:
        D_value = compliance_statistic - tmp_compliance_statistic
        copy_D_value = D_value
        for i in range(number_of_complianceB):
            if complianceB[i].get(section) == compliance_condition:
                complianceB[i].compliance = "complianceA"
                #print("change B to A.")
                copy_D_value = copy_D_value - 1
                if copy_D_value == 0:
                    break
        if copy_D_value > 0:
            for i in range(number_of_complianceC):
                if complianceC[i].get(section) == compliance_condition:
                    complianceC[i].compliance = "complianceA"
                    #print("change C to A.")
                    copy_D_value = copy_D_value - 1
                    if copy_D_value == 0:
                        break
        
section = "age"    
compliance_statistic = 48
compliance_condition = "<45"
adjust_complianceA()
reset_compliance()  
compliance_statistic = 20
compliance_condition = "45-60"
adjust_complianceA()
reset_compliance()  
compliance_statistic = 25
compliance_condition = ">60"
adjust_complianceA()
reset_compliance()

#area
section = "area"    
compliance_statistic = 40
compliance_condition = "country"
adjust_complianceA()
reset_compliance()  
compliance_statistic = 53
compliance_condition = "city"
adjust_complianceA()
reset_compliance()

#edu
section = "edu"    
compliance_statistic = 56
compliance_condition = "bachelar"
adjust_complianceA()
reset_compliance()   
compliance_statistic = 37
compliance_condition = "hign school"
adjust_complianceA()
reset_compliance()

#marriage
section = "marriage"    
compliance_statistic = 28
compliance_condition = "not_married"
adjust_complianceA()
reset_compliance()
compliance_statistic = 65
compliance_condition = "married"
adjust_complianceA()
reset_compliance()

#job
section = "job"    
compliance_statistic = 17
compliance_condition = "Job_A"
adjust_complianceA()
reset_compliance()  
compliance_statistic = 14
compliance_condition = "Job_B"
adjust_complianceA()
reset_compliance()
compliance_statistic = 15
compliance_condition = "Job_C"
adjust_complianceA()
reset_compliance()
compliance_statistic = 6
compliance_condition = "Job_D"
adjust_complianceA()
reset_compliance()
compliance_statistic = 18
compliance_condition = "Job_E"
adjust_complianceA()
reset_compliance()
compliance_statistic = 9
compliance_condition = "Job_F"
adjust_complianceA()
reset_compliance()
compliance_statistic = 14
compliance_condition = "Job_G"
adjust_complianceA()
reset_compliance()

#employ
section = "employ"    
compliance_statistic = 35
compliance_condition = "unemployed"
adjust_complianceA()
reset_compliance()
compliance_statistic = 25
compliance_condition = "retired"
adjust_complianceA()
reset_compliance()
compliance_statistic = 33
compliance_condition = "OnJob"
adjust_complianceA()
reset_compliance()

#home_salary
section = "home_salary"    
compliance_statistic = 35
compliance_condition = ">5000"
adjust_complianceA()
reset_compliance()
compliance_statistic = 29
compliance_condition = "3501-5000"
adjust_complianceA()
reset_compliance()
compliance_statistic = 17
compliance_condition = "2001-3500"
adjust_complianceA()
reset_compliance()
compliance_statistic = 12
compliance_condition = "<2000"
adjust_complianceA()
reset_compliance()

#medical
section = "medical"    
compliance_statistic = 45
compliance_condition = "medicalA"
adjust_complianceA()
reset_compliance()
compliance_statistic = 26
compliance_condition = "medicalB"
adjust_complianceA()
reset_compliance()
compliance_statistic = 22
compliance_condition = "medicalC"
adjust_complianceA()
reset_compliance()

def adjust_complianceB():
    global number_of_complianceB
    global number_of_complianceC
    global complianceB
    global complianceC
    global section
    global compliance_statistic
    global compliance_condition
    
    tmp_compliance_statistic = 0
    for i in range(number_of_complianceB):
        if complianceB[i].get(section) == compliance_condition:
            if tmp_compliance_statistic < compliance_statistic:
                tmp_compliance_statistic = tmp_compliance_statistic + 1
            else:
                complianceB[i].compliance = "complianceC"
                #print("change B to C.")
    if tmp_compliance_statistic < compliance_statistic:
        D_value = compliance_statistic - tmp_compliance_statistic
        copy_D_value = D_value
        for i in range(number_of_complianceC):
            if complianceC[i].get(section) == compliance_condition:
                complianceC[i].compliance = "complianceB"
                #print("change C to B.")
                copy_D_value = copy_D_value - 1
                if copy_D_value == 0:
                    break
        if copy_D_value > 0:
            print("*****************ERROR***************")

section = "age"    
compliance_statistic = 72
compliance_condition = "<45"
adjust_complianceB()
reset_compliance()  
compliance_statistic = 69
compliance_condition = "45-60"
adjust_complianceB()
reset_compliance()  
compliance_statistic = 40
compliance_condition = ">60"
adjust_complianceB()
reset_compliance()

#area
section = "area"    
compliance_statistic = 79
compliance_condition = "country"
adjust_complianceB()
reset_compliance()  
compliance_statistic = 102
compliance_condition = "city"
adjust_complianceB()
reset_compliance()

#edu
section = "edu"    
compliance_statistic = 90
compliance_condition = "bachelar"
adjust_complianceB()
reset_compliance()   
compliance_statistic = 91
compliance_condition = "hign school"
adjust_complianceB()
reset_compliance()

#marriage
section = "marriage"    
compliance_statistic = 73
compliance_condition = "not_married"
adjust_complianceB()
reset_compliance()
compliance_statistic = 108
compliance_condition = "married"
adjust_complianceB()
reset_compliance()

#job
section = "job"    
compliance_statistic = 30
compliance_condition = "Job_A"
adjust_complianceB()
reset_compliance()  
compliance_statistic = 25
compliance_condition = "Job_B"
adjust_complianceB()
reset_compliance()
compliance_statistic = 28
compliance_condition = "Job_C"
adjust_complianceB()
reset_compliance()
compliance_statistic = 20
compliance_condition = "Job_D"
adjust_complianceB()
reset_compliance()
compliance_statistic = 33
compliance_condition = "Job_E"
adjust_complianceB()
reset_compliance()
compliance_statistic = 20
compliance_condition = "Job_F"
adjust_complianceB()
reset_compliance()
compliance_statistic = 25
compliance_condition = "Job_G"
adjust_complianceB()
reset_compliance()

#employ
section = "employ"    
compliance_statistic = 50
compliance_condition = "unemployed"
adjust_complianceB()
reset_compliance()
compliance_statistic = 66
compliance_condition = "retired"
adjust_complianceB()
reset_compliance()
compliance_statistic = 65
compliance_condition = "OnJob"
adjust_complianceB()
reset_compliance()

#home_salary
section = "home_salary"    
compliance_statistic = 50
compliance_condition = ">5000"
adjust_complianceB()
reset_compliance()
compliance_statistic = 46
compliance_condition = "3501-5000"
adjust_complianceB()
reset_compliance()
compliance_statistic = 47
compliance_condition = "2001-3500"
adjust_complianceB()
reset_compliance()
compliance_statistic = 38
compliance_condition = "<2000"
adjust_complianceB()
reset_compliance()

#medical
section = "medical"    
compliance_statistic = 56
compliance_condition = "medicalA"
adjust_complianceB()
reset_compliance()
compliance_statistic = 79
compliance_condition = "medicalB"
adjust_complianceB()
reset_compliance()
compliance_statistic = 46
compliance_condition = "medicalC"
adjust_complianceB()
reset_compliance()

#print("A:%d  B:%d  C:%d" % (number_of_complianceA, number_of_complianceB, number_of_complianceC))


for i in range(total):
    print(persons[i])
os.system(exit(0))

