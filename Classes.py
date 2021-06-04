import datetime
import random
import os
import sys

def get_line_from_file(self, file_path, line_num):
    f = open(file_path, 'r+')

    line_count = 0
    target = ""
    lines = f.readlines()

    for line in lines:
        line_count += 1
        if line_count == line_num:
            target = line
    f.close()
    return target

class Patient:
    first_name = 'uninitialized'
    middle_name = 'uninitialized'
    last_name = 'uninitialized'
    patient_id = 'uninitialized'
    dob = datetime.datetime(1111,1,1)
    phone = 'uninitialized'
    email = 'uninitialized'
    address = 'uninitialized'
    upcoming_appointments = 'none'

    
    #parameter constrcutor
    def __init__(self, first_name, middle_name, last_name, dob_year, dob_month, dob_day, phone, email, address):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.dob = datetime.date(dob_year,dob_month,dob_day)
        self.phone = phone
        self.email = email
        self.address = address        

        with open(sys.path[0] + '/identifiers/next_open_id.txt', 'r+') as f:
            first_line = f.readline()
            print("reading from file")
            print(first_line)
            number = int(first_line)
            next_number = number + random.randint(0,200)
            input_number = str(next_number)
            self.patient_id = first_line
            f.seek(0) #https://stackoverflow.com/questions/11469228/replace-and-overwrite-instead-of-appending/11469328
            f.write(input_number)
            f.truncate()
            f.close() 

        new_patient = open(sys.path[0] + "/patients/" + self.patient_id + ".txt", 'w')
        self.write_patient_to_file(self.patient_id)

        new_patient.close()



    #getters
    def get_first_name(self):
        f = open(sys.path[0] + "/patients/" + self.patient_id + ".txt", 'r+')
        first_line = f.readline()
        target = first_line.split(" ")
        f.close()
        return target[0]
    
    def get_middle_name(self):
        f = open(sys.path[0] + "/patients/" + self.patient_id + ".txt", 'r+')
        first_line = f.readline()
        target = first_line.split(" ")
        f.close()
        return target[1]


    def get_last_name(self):
        f = open(sys.path[0] + "/patients/" + self.patient_id + ".txt", 'r+')
        first_line = f.readline()
        target = first_line.split(" ")
        f.close()
        return target[2]

    def get_dob(self):
        f = open(sys.path[0] + "/patients/" + self.patient_id + ".txt", 'r+')
        f.readline()
        target = f.readline()
        f.close()
        return target

    def get_phone(self):
        f = open(sys.path[0] + "/patients/" + self.patient_id + ".txt", 'r+')
        f.readline()
        f.readline()
        target = f.readline()
        f.close()
        return target

    def get_email(self):
        f = open(sys.path[0] + "/patients/" + self.patient_id + ".txt", 'r+')
        f.readline()
        f.readline()
        f.readline()
        target = f.readline()
        f.close()
        return target
    
    def get_address(self):   
        f = open(sys.path[0] + "/patients/" + self.patient_id + ".txt", 'r+')
        f.readline()
        f.readline()
        f.readline()
        f.readline()
        target = f.readline()
        f.close()
        print(target)
        return target
        
    def get_patient_id(self):
        return self.patient_id

    #setters

    def set_first_name(self, first_name):
        self.first_name = first_name
        self.write_patient_to_file(self.patient_id)

    def set_middle_name(self, middle_name):
        self.middle_name = middle_name
        self.write_patient_to_file(self.patient_id)

    
    def set_last_name(self, last_name):
        self.last_name = last_name
        self.write_patient_to_file(self.patient_id)


    def set_dob(self, year, month, day):
        self.dob = datetime.date(year, month, day)
        self.write_patient_to_file(self.patient_id)

    def set_phone(self, phone):
        self.phone = phone
        self.write_patient_to_file(self.patient_id)
    
    def set_email(self, email):
        self.email = email
        self.write_patient_to_file(self.patient_id)

    def set_address(self, address):
        self.address = address
        self.write_patient_to_file(self.patient_id)



    
    def write_patient_to_file(self, patient_id):
        #navigate to the patients folder
        date = self.dob
        year = date.strftime("%Y") #citation: https://www.programiz.com/python-programming/datetime/strftime
        month = date.strftime("%m")
        day = date.strftime("%d")

        with open(sys.path[0] + "/patients/" + self.patient_id+".txt", 'r+') as f:
        #write the patient info to the new file in the proper format
            write_build = ""
            write_build += self.first_name + " " + self.middle_name + " " + self.last_name + "\n"
            write_build += month + "/" + day + "/"+ year + "\n"
            write_build += self.phone + "\n" + self.email + "\n" + self.address + "\n"

            f.seek(0)
            f.write(write_build)
            f.truncate()
            f.close()

class MedicalRecord:
    patient_id = "uninitialized"
    vaccine_history = "uninitialized"
    medication_history = "uninitialized"
    ailment_history = "uninitialized"
    family_history = "uninitialized"
    allergies = "uninitialized"
    surgeries = "uninitialized"

    def __init__(self,patient_id,vaccine_history,medication_history,ailment_history,family_history,allergies, surgeries):
        self.patient_id = patient_id
        self.vaccine_history = vaccine_history
        self.medication_history = medication_history
        self.ailment_history = ailment_history
        self.family_history = family_history
        self.allergies = allergies
        self.surgeries = surgeries

        new_medical_record = open(sys.path[0] + "/medical_records/" + self.patient_id + ".txt", 'w')
        self.write_medical_record_to_file(self.patient_id)
        new_medical_record.close()

    def set_vaccine_history(self, vaccine_history):
        self.vaccine_history = vaccine_history
        self.write_medical_record_to_file(self.patient_id)

    def set_medication_history(self, medication_history):
        self.medication_history = medication_history
        self.write_medical_record_to_file(self.patient_id)

    def set_ailment_history(self, ailment_history):
        self.ailment_history = ailment_history
        self.write_medical_record_to_file(self.patient_id)

    def set_family_history(self, family_history):
        self.family_history = family_history
        self.write_medical_record_to_file(self.patient_id)

    def set_allergies(self, allergies):
        self.allergies = allergies
        self.write_medical_record_to_file(self.patient_id)
    
    def set_surgeries(self, surgeries):
        self.surgeries = surgeries
        self.write_medical_record_to_file(self.patient_id)

    def get_vaccine_history(self):
        f = open(sys.path[0] + "/medical_records/" + self.patient_id + ".txt", 'r+')
        line_count = 0
        target = ""
        lines = f.readlines()

        for line in lines:
            line_count += 1
            if line_count == 2:
                target = line
                print(target)

        f.close()
        return target


    def get_medication_history(self):
        f = open(sys.path[0] + "/medical_records/" + self.patient_id + ".txt", 'r+')
        line_count = 0
        target = ""
        lines = f.readlines()

        for line in lines:
            line_count += 1
            if line_count == 5:
                target = line

        f.close()
        return target
    
    def get_ailment_history(self):
        f = open(sys.path[0] + "/medical_records/" + self.patient_id + ".txt", 'r+')
        line_count = 0
        return get_line_from_file(self, sys.path[0] + "/medical_records/" + self.patient_id + ".txt",8)

    def get_family_history(self):
        f = open(sys.path[0] + "/medical_records/" + self.patient_id + ".txt", 'r+')
        line_count = 0
        target = ""
        lines = f.readlines()

        for line in lines:
            line_count += 1
            if line_count == 11:
                target = line

        f.close()
        return target

    def get_allergies(self):
        f = open(sys.path[0] + "/medical_records/" + self.patient_id + ".txt", 'r+')
        line_count = 0
        target = ""
        lines = f.readlines()

        for line in lines:
            line_count += 1
            if line_count == 14:
                target = line
                print(target)

        f.close()
        return target
        

    def get_surgeries(self):
        f = open(sys.path[0] + "/medical_records/" + self.patient_id + ".txt", 'r+')
        line_count = 0
        target = ""
        lines = f.readlines()

        for line in lines:
            line_count += 1
            if line_count == 17:
                target = line

        f.close()
        return target

    
    def write_medical_record_to_file(self, patient_id):
        #navigate to the medical_records folder

        with open(sys.path[0] + "/medical_records/" + self.patient_id+".txt", 'r+') as f:
        #write the patient info to the new file in the proper format
            write_build = ""
            write_build += "Vaccine History:\n" + self.vaccine_history + "\n"
            write_build += "\nMedication History:\n" + self.medication_history + "\n"
            write_build += "\nAilment History:\n" + self.ailment_history + "\n"
            write_build += "\nFamily History: \n" + self.family_history + "\n"
            write_build += "\nAllergies: \n" + self.allergies + "\n"
            write_build += "\nSurgeries: \n" + self.surgeries + "\n"


            f.seek(0)
            f.write(write_build)
            f.truncate()
            f.close()

class Login:
    patient_id = "uninitialized"
    username = "uninitialized"
    password = "uninitialized"

    def __init__(self, patient_id, username, password):
        self.patient_id = patient_id
        self.username = username
        self.password = password

        new_login = open(sys.path[0] + "/logins/" + self.patient_id + ".txt", 'w')
        self.write_patient_to_file(self.patient_id)
        new_login.close()
    
    def set_username(self, username):
        self.username = username
        self.write_login_to_file(self, self.patient_id)

    def set_password(self, password):
        self.password = password
        self.write_login_to_file(self,self.patient_id)

    def get_patient_id(self):
        return self.patient_id

    def get_username(self):
        f = open(sys.path[0] + "/logins/" + self.patient_id + ".txt", 'r+')
        line_count = 0
        target = ""
        lines = f.readlines()

        for line in lines:
            line_count += 1
            if line_count == 1:
                target = line

        f.close()
        return target

    def get_password(self):
        f = open(sys.path[0] + "/logins/" + self.patient_id + ".txt", 'r+')
        line_count = 0
        target = ""
        lines = f.readlines()

        for line in lines:
            line_count += 1
            if line_count == 2:
                target = line

        f.close()
        return target

    def write_login_to_file(self, patient_id):
        with open(sys.path[0] + "/logins/" + self.patient_id+".txt", 'r+') as f:
        #write the patient info to the new file in the proper format
            write_build = ""
            write_build += self.username + "\n"
            write_build += self.password + "\n"

            f.seek(0)
            f.write(write_build)
            f.truncate()
            f.close()

class Identifier:
    patient_id = "uninitialized"
    ssn = "uninitialized"
    other_id = "uninitialized"

    def __init__(self, patient_id, ssn, other_id):
        self.patient_id = patient_id
        self.ssn = ssn
        self.other_id = other_id

        new_identifier = open(sys.path[0] + "/identifiers/" + self.patient_id + ".txt", 'w')
        self.write_login_to_file(self.patient_id)
        new_identifier.close()

    def set_ssn(self, ssn):
        self.ssn = ssn
        self.write_identifier_to_file(self.patient_id)

    def set_other_id(self, other_id):
        self.other_id = other_id
        self.write_identifier_to_file(self.patient_id)

    def get_patient_id(self):
        return self.patient_id

    def get_ssn(self):
        f = open(sys.path[0] + "/identifiers/" + self.patient_id + ".txt", 'r+')
        line_count = 0
        target = ""
        lines = f.readlines()

        for line in lines:
            line_count += 1
            if line_count == 1:
                target = line

        f.close()
        return target

    def get_other_id(self):
        f = open(sys.path[0] + "/identifiers/" + self.patient_id + ".txt", 'r+')
        line_count = 0
        target = ""
        lines = f.readlines()

        for line in lines:
            line_count += 1
            if line_count == 2:
                target = line

        f.close()
        return target



    def write_identifier_to_file(self, patient_id):
        with open(sys.path[0] + "/identifiers/" + self.patient_id+".txt", 'r+') as f:
        #write the patient info to the new file in the proper format
            write_build = ""
            write_build += self.ssn + "\n"
            write_build += self.other_id + "\n"

            f.seek(0)
            f.write(write_build)
            f.truncate()
            f.close()

class Appointments:
    date = datetime.datetime.now()
    time = "uninitialized"
    patient_id = "uninitialized"
    doctor = "uninitialized"
    reason = "uninitialzied"

    def __init__(self, year, month, day, time, patient_id, doctor, reason):
        self.date = datetime.date(year, month, day)
        self.time = time
        self.patient_id = patient_id
        self.doctor = doctor
        self.reason = reason

    