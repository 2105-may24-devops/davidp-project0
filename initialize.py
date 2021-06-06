import datetime
import os
import sys
from pathlib import Path

from genericpath import isfile

from Classes import (Identifier, Login, MedicalRecord, Patient, get_address,
                     get_dob, get_email, get_first_name, get_last_name,
                     get_line_from_file, get_middle_name, get_phone,
                     get_unique_id, write_to_file)

#citation: https://djangocentral.com/check-if-a-directory-exists-if-not-create-it/p
logins_dir = "logins"
patients_dir = "patients"
appointments_dir = "appointments"
medical_records_dir = "medical_records"
identifier_dir = "identifiers"
admin_login_dir = "admin_logins"

if not os.path.isdir(logins_dir):
    os.makedirs(logins_dir)
    print("created folder: ", logins_dir)

if not os.path.isdir(patients_dir):
    os.makedirs(patients_dir)
    print("created folder: ", patients_dir)

if not os.path.isdir(appointments_dir):
    os.makedirs(appointments_dir)
    print("created folder: ", appointments_dir)

if not os.path.isdir(medical_records_dir):
    os.makedirs(medical_records_dir)
    print("created folder: ", medical_records_dir)

if not os.path.isdir(identifier_dir):
    os.makedirs(identifier_dir)
    print("created folder: ", identifier_dir)

if not os.path.isdir(admin_login_dir):
    os.makedirs(admin_login_dir)
    print("created folder: ", admin_login_dir)

test_path = sys.path[0] + '/admin_logins/admin_login.txt'

admin_username = "current_admin_username"
admin_password = "current_admin_password"
admin_login_write_string = admin_username + "\n" + admin_password

if os.path.isfile(test_path):
    pass
else:
    file = open(test_path, 'w')
    file.write(admin_login_write_string)
    file.close()

#os.chdir(identifier_dir)

#citation: https://stackoverflow.com/questions/2967194/open-in-python-does-not-create-a-file-if-it-doesnt-exist

test_path = sys.path[0] + '/identifiers/next_open_id.txt'
if os.path.isfile(test_path):
    pass
else:
    file = open(test_path, 'w')
    file.write("1111111111")
    file.close()

date = datetime.date.today()

appointments = {"8:00am":"open", "8:40am":"open","9:20am":"open","10:00am":"open","10:40am":"open","11:20am":"open","1:00pm":"open","1:40pm":"open","2:20pm":"open","3:00pm":"open","3:40pm":"open","4:20pm":"open"}

for i in range(180):
    #print(str(date))
    date += datetime.timedelta(days=1)
    
    filename = str(date)
    weekday_check = date.weekday()
    if(weekday_check < 5): #citation: https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python
        f = open(sys.path[0] + "/appointments/" + filename + ".txt", 'w')
        for key, value in appointments.items(): 
            f.write('%s-%s\n' % (key, value))
        f.close()

def patient_menu(patient_id):
    dob_date_to_parse = get_dob(patient_id).split("/")
    dob_year = dob_date_to_parse[0]
    dob_month = dob_date_to_parse[1]
    dob_day = dob_date_to_parse[2]    
    this_patient = Patient(get_first_name(patient_id),get_middle_name(patient_id),get_last_name(patient_id),dob_year,dob_month,dob_day,get_phone(patient_id),get_email(patient_id),get_address(patient_id))
    
    this_patient.set_patient_id(patient_id)

    exit = 0
    while exit != 5:
        choice = input("select from the following options: \n(1) make an appointment \n(2) view medical record \n(3) view your upcoming appointments \n(4) cancel an appointment \n(5) exit")

        if choice == "1":
            make_an_appointment(patient_id)
        elif choice == "2":
            view_medical_record(patient_id)
        elif choice == "3":
            view_upcoming_appointments(patient_id)
        elif choice == "4":
            cancel_an_appointmnet(patient_id)
        elif choice == "5":
            exit = 5
        else:
            print("please choose from the menu")

def patient_login():
    try_count = 0
    found = 0

    username = input("please enter your username")
    #find that username
    path = sys.path[0]+"/logins"

    test_username = ""
    found_patient_id = "not found"
    login_success = 0
    returned_patient_id = "unsuccessful login"

    try_username = "1"
    while try_username == "1":

        for file in os.listdir(path):
            test_username = get_line_from_file(file,0)
            if test_username == username:
                while try_count < 4:
                    try_count += 1
                    found = 1
                    password = input("please enter your password\n")
                    test_password = get_line_from_file(file, 1)
                    if test_password == password:
                        found_patient_id = file
                        login_success = 1
                        break
                    else:
                        password = input("incorrect password, please re-enter\n")
                if try_count > 3:
                    print("account temporarily locked due to multiple incorrect login attempts, please contact our office\n")
                break
        if not found:
            selection = ""
            while selection != "1" and selection != "2":
                selection = input("username not found\n(1) try entering again\n(2) exit")
                try_username = selection
        
        if login_success:
            patient_menu(found_patient_id)
            
def admin_menu():
    pass
    
def view_open_appointments():
    path = sys.path[0] + "/appointments/"
    open_appointment_list = {}

    for file in os.listdir(path):
        f = open(path + file, 'r+')
        lines = f.readlines()
        for line in lines:
            line_split = line.split("-")
            time = line_split[0]
            status = line_split[1]
            trunc = str(file)
            trunc = trunc[:-4]
            if status.strip() == "open":
                open_appointment_list[trunc] = time
        f.close()
    for x in open_appointment_list:
        print(x, open_appointment_list[x])


def make_an_appointment(patient_id):
    exit = 0
    choice = input("please choose from the following items:\n(1) view open appointments on given day\n(2) view all open appointments\n(3)return to patient menu")
    while choice != "1" and choice != "2" and choice != "3":
        choice = input("please select a menu option")
    if choice == "1":
        date = input("please select a date in the following format: YYYY-MM-DD")
        path = sys.path[0]+"/appointments/"+date
        while not isfile(path):
            date = input("date is either not in range (weekdays in next 6 months) or is not in YYYY-MM-DD format, please try again")
        selected_day_appointments = {}

        f = open(path, 'r+')
        lines = f.readlines()
        for line in lines:
            line_split = line.split("-")
            time = line_split[0]
            status = line_split[1]
            trunc = str(file)
            trunc = trunc[:-4]
            if status.strip() == "open":
                selected_day_appointments[trunc] = time
        f.close()
        print("open appointments for " + date)
        for x in selected_day_appointments:
            print(x, selected_day_appointments[x])
    elif choice == "2":
        view_open_appointments()
    else:
        patient_menu(patient_id)
        
    print("here are the open appointment slots")
    view_open_appointments()

def view_medical_record(patient_id):
    pass

def view_upcoming_appointments(patient_id):
    path = sys.path[0]+"/appointments/"

    appointment_list = {}

    for file in os.listdir(path):
        f = open(path + file, 'r+')
        lines = f.readlines()

        selected_day_appointments = {}

        for line in lines:
            line_split = line.split(":")
            time = line_split[0]
            status = line_split[1]

            if status == patient_id:
                appointment_list[file] = time         
    print(appointment_list)

def cancel_an_appointmnet(patient_id):
    print("here are your upcoming appointments: ")
    
    view_upcoming_appointments(patient_id)

    date_input = input("please type the date of your upcoming apointment in the format DD-MM-YYYY or press 1 to go back to patient menu")

    test_path = sys.path[0]+"/appointments/"+ date_input

    while not isfile(test_path) and date_input != "1":
        print("appointment not found or date entered incorrectly. Please try again or press 1 to go back to patient menu")
        date_input = input("please type the date of your upcoming apointment in the format YYYY-MM-DD or press 1 to go back to patient menu")

        if date_input == "1":
            patient_menu(patient_id)

    selected_day_appointments = {}

    f = open(test_path,'r+')
    lines = f.readlines()

    for line in lines:
        line_split = line.split(":")
        time = line_split[0]
        status = line_split[1]

        selected_day_appointments[time] = status

        cancelled = [k for k, v in selected_day_appointments.items() if v == patient_id] #citation: https://note.nkmk.me/en/python-dict-get-key-from-value/

        cancelled_time = cancelled[0]
        selected_day_appointments[cancelled_time] = "open"

    f.close()

    f = open(test_path,'r+')

    for key, value in selected_day_appointments.items(): 
        f.write('%s-%s\n' % (key, value))
    f.close()
    print("appointment on " + date_input + " cancelled")
    patient_menu(patient_id)


def admin_login():
    tries = 0
    username_success = 0
    password_success = 0
    exit = "0"
    while username_success == 0 and exit == "0":
        test_admin_username = input("enter your username or press 1 to exit")
        admin_username = get_line_from_file(sys.path[0] + "/admin_logins/admin_login.txt", 1)
        if test_admin_username == "1":
            exit = test_admin_username
        elif test_admin_username == admin_username:
            username_success == 1
        else:
            print("admin username not found, please try again")
    
    if username_success:
        while tries < 4 and exit == "0":
            tries += 1
            test_admin_password = input("enter your password or press 1 to exit")
            admin_password = get_line_from_file(sys.paht[0] + "/admin_lgins/admin_login.txt", 2)
            if test_admin_password == "1":
                exit = test_admin_password
            elif test_admin_password == admin_password:
                password_success = 1
            else:
                if(tries == 3):
                    print("account locked due to multiple unsuccessful attempts, please contact the office")
                else:
                    print("incorrect password, please try again")

        if username_success and password_success:
            admin_menu()

def register_new_patient():
    patient_id = get_unique_id()
    print("Welcome to Central Medical Clinic. You will be prompted to provide some information in order to set up your profile\n"+
    "Pressing enter will move to move to the next item.")
    first_name = input("first name: ")
    middle_name = input("middle name: ")
    last_name = input("last name: ")
    correct_format = False
    birth_date = ""
    dob_year = ""
    dob_month = ""
    dob_day = ""
    while not correct_format:
        birth_date = input("date of birth: (format YYYY-MM-DD) ")
        test = birth_date.split("-")
        count = 0
        for i in birth_date:
            count+=1
        if count == 3:
            correct_format = True #at least they used the dashes
            dob_year = test[0]
            dob_month = test[1]
            dob_day = test[2]
        else:
            print("Please use format YYYY-MM-DD for date of birth")
    phone = input("phone: ")
    email = input("email: ")
    address = input("address: ")

    new_patient = Patient(first_name,middle_name,last_name,dob_year,dob_month,dob_day,phone,email,address)

    vaccine_history = input("please indicate vaccine histroy or write \"not sure\"")
    medication_history = input("please list current medications")
    ailment_history = input("please list any significant health issues you have experienced")
    family_history = input("please describe pertinent hereditory family medical history")
    allergies = input("please list all known allergies")
    surgeries = input("please describe any surgeries you have undergone")

    new_medical_record = MedicalRecord(patient_id,vaccine_history,medication_history,ailment_history,family_history,allergies,surgeries)

    correct_input = False
    ssn = ""
    other_id = ""
    
    while not correct_input:
        choice = input("do you have a social security number? (y/n)").lower()
    
    if choice == "y":
        ssn = input("please enter your social security number")
        other_id = "N/A"
    else:
        ssn = "N/A"
        other_id = input("In a single line, please enter another type of governemt ID and state the ID-type")
    
    new_identifier = Identifier(patient_id,ssn,other_id)

    print("your patient ID is " + patient_id)

    username_valid = False
    username = ""
    
    path = sys.path[0] + "/logins"

    while not username_valid:
        username = input("Please select a username")

        found = 0

        for file in os.listdir(path):
            test_username = get_line_from_file(file,0)
            if username == test_username:
                found = 1
        if not found:
            username_valid = True
        else:
            print("username already exists")
    
    password_valid = False

    while not password_valid:
        password = input("please select a password at least 8 characters long")
        if len(password) >= 8:
            password_valid = True
    
    new_login = Login(patient_id,username,password)
        
def menu():
    print("Welcome to Central Medical Clinic\n")
    patient_id = ""
    login_choice = " "
    while login_choice != "p" and login_choice != "a" and login_choice != "r" and login_choice != "e":
        login_choice = input("Please choose from the following options:\n (P) patient login\n(A) admin login\n(R) register as a new patient\n(E) exit")
        login_choice = login_choice.lower()

    if login_choice == "p":
        patient_login()
    elif login_choice == "a":
        admin_login()
    elif login_choice == "r":
        patient_id = register_new_patient()
    else:
        return

view_open_appointments()

    

  




