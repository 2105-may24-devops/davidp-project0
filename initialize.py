import datetime
import os
import sys
#from pathlib import Path

from genericpath import isfile

from Classes import (Identifier, Login, MedicalRecord, Patient, get_address,
get_dob, get_email, get_first_name, get_last_name,
get_line_from_file, get_middle_name, get_phone,
get_unique_id, write_to_file,get_password,get_username,get_ailment_history,get_allergies,get_family_history,get_medication_history,get_surgeries,get_vaccine_history,get_other_id,get_ssn)

#citation: https://djangocentral.com/check-if-a-directory-exists-if-not-create-it/p
logins_dir = "logins"
patients_dir = "patients"
appointments_dir = "appointments"
medical_records_dir = "medical_records"
identifier_dir = "identifiers"
admin_login_dir = "admin_logins"
run_log_dir = "run_log"


sys.stderr.write(str(datetime.datetime.now().time()))

if not os.path.isdir(run_log_dir):
    os.makedirs(run_log_dir)
    print("created folder: ", run_log_dir)

run_log_file_path = sys.path[0]+"/run_log/run_log.txt"
f = open(run_log_file_path, 'a')
f.write(str(datetime.datetime.now().time()) + "\n")
f.close()

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
    file_path = sys.path[0] + "/appointments/" + filename + ".txt"
    
    if(weekday_check < 5): #citation: https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python
        if not os.path.isfile(file_path):
            f = open(sys.path[0] + "/appointments/" + filename + ".txt", 'w')
            for key, value in appointments.items(): 
                f.write('%s-%s\n' % (key, value))
            f.close()

def patient_menu(patient_id):
    dob_date_to_parse = get_dob(patient_id).split("/")
    dob_year = int(dob_date_to_parse[2])
    dob_month = int(dob_date_to_parse[0])
    dob_day = int(dob_date_to_parse[1])    
    this_patient = Patient(get_first_name(patient_id),get_middle_name(patient_id),get_last_name(patient_id),dob_year,dob_month,dob_day,get_phone(patient_id),get_email(patient_id),get_address(patient_id))
    
    this_patient.set_patient_id(patient_id)

    exit = 0
    while exit != 5:
        choice = input("select from the following options: \n(1) make an appointment \n(2) view medical record \n(3)"
        +" view your upcoming appointments \n(4) cancel an appointment \n(5) exit\n")

        if choice == "1":
            make_an_appointment(patient_id)
        elif choice == "2":
            view_medical_record(patient_id)
        elif choice == "3":
            view_upcoming_appointments(patient_id)
        elif choice == "4":
            cancel_an_appointmnet(patient_id)
        elif choice == "5":
            menu()
        else:
            print("please choose from the menu")

def patient_login():
    username_found = False
    password_found = False

    file_path = sys.path[0] + "/logins/"

    quit = False

    while not username_found and not quit:
        entered_username = input("please enter your USERNAME or type 'q' to quit\n")
        for file in os.listdir(file_path):
            test_username = get_line_from_file(file_path+file,1)
            test_username = test_username.strip()
            if test_username == entered_username:
                username_found = True
            elif entered_username == "q":
                quit = True
                menu()
        if not username_found:
            print("username not found, please try again") 
            
    while username_found and not password_found and not quit:
        entered_password = input("please enter your PASSWORD or type 'q' to quit\n")
        for file in os.listdir(file_path):
            test_password = get_line_from_file(file_path+file,2)
            test_password = test_password.strip()
            if test_password == entered_password:
                password_found = True
            elif entered_password == "q":
                quit = True
                menu()
        if not password_found:
            print("password not found, please try again") 

    if password_found and username_found:
        patient_id = file[:-4]
        patient_menu(patient_id)

def view_all_appointments():
    file_path = sys.path[0] + "/patients"
    for file in os.listdir(file_path):
        view_upcoming_appointments(file)
    admin_menu()

def cancel_an_appointment(patient_id, mode):
    found = 0
    appointment_date = ""
    while not found and appointment_date != "q":
        appointment_date = input("select a date for which to cancel (YYYY-MM-DD)\n")
        file_path = os.path[0] + "/appointments/" + appointment_date + ".txt"
        if os.path.isfile(file_path):
            found = True
        else:
            appointment_date = input("appointment not found for that date, please try again, make sure date format is (YYYY-MM-DD) or type 'q' to return to menu\n")
            if appointment_date == "q":
                if mode == "patient":
                    patient_menu()
                else:
                    admin_menu()

def admin_cancel_an_appointment():
    pass

def admin_view_medical_record():
    pass

def lookup_patient_id(gov_id):
    pass#file_path = sys.path[0] + "/identifiers/" + 



def admin_menu():
    choice = ""
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6":
        choice = input("Now logged in as admin. Please choose from the following options:\n(1) view all appointments\n(2)"
        +"cancel an appointment\n(3) view a medical record\n(4)lookup patient_id by Name and identifier\n(5)delete a patient\n(6) logout )\n")
        if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6":
            print("please choose from the menu options")
    if choice == "1":
        view_all_appointments()
    elif choice == "2":
        admin_cancel_an_appointment()
    elif choice == "3":
        admin_view_medical_record()
    elif choice == "4":
        lookup_patient_id()
    elif choice == "5": 
        delete_patient()
    elif choice == "6":
        menu()

    #cancel appointments
    #view medical records
    #lookup someone's patient number with appropriate identifiers
    #delete a patient

    
def view_open_appointments():
    file_path = sys.path[0] + "/appointments/"

    for file in os.listdir(file_path):
        date = file[:-4]
        print(date)
        f = open(file_path + file,'r+')
        lines = f.readlines()
        for line in lines:
            line_split = line.split("-")
            time = line_split[0]
            status = line_split[1]
            if status.strip() == "open":
                print(time)
        f.close()

def make_an_appointment_menu(patient_id, choice):
    if choice == "1":
        date = input("please select a date in the following format: YYYY-MM-DD\n")
        file_path = sys.path[0]+"/appointments/"+date+".txt"
        while not isfile(file_path):
            date = input("date is either not in range (weekdays in next 6 months) or is not in YYYY-MM-DD format, please try again\n")
            file_path = sys.path[0]+"/appointments/"+date+".txt"
        selected_day_appointments = []

        f = open(file_path,'r+')
        lines = f.readlines()
        for line in lines:
            line_split = line.split("-")
            time = line_split[0]
            status = line_split[1]
            if status.strip() == "open":
                selected_day_appointments.append(time)
        f.close()
        print("open appointments for " + date)
        for x in selected_day_appointments:
            print(x)
    elif choice == "2":
        view_open_appointments()
    elif choice == "3":
        date = input("please select a date in the following format: YYYY-MM-DD\n")
        file_path = sys.path[0]+"/appointments/"+date+".txt"
        while not isfile(file_path):
            date = input("date is either not in range (weekdays in next 6 months) or is not in YYYY-MM-DD format, please try again\n")

        f = open(file_path, 'r+')
        selected_days_current_appointments = {}
        lines = f.readlines()
        for line in lines:
            line_split = line.split("-")
            time = line_split[0]
            status = line_split[1]
            status = status.strip()
            selected_days_current_appointments[time] = status
        time_found = False
        quit = False
        time = "---"
        while not time_found and not quit:
            while not time in selected_days_current_appointments:
                time = input("please select an open time in the example format 9:00am or type 'q' to quit\n")
                time_found = True
            if time == "q":
                quit = True
                patient_menu(patient_id)
            status = selected_days_current_appointments[time]
            if status.strip() == "open":
                selected_days_current_appointments[time] = patient_id
        f.close()
        f = open(file_path, 'w')
        for key, value in selected_days_current_appointments.items():
            f.write('%s-%s\n' % (key, value))
        f.close()
        print("appointment made for " +date+ " at " + time + "cancelled")
    
def make_an_appointment(patient_id):
    exit = 0
    choice = ""
    
    while choice != "4":
        choice = input("please choose from the following items:\n(1) view open appointments on given day\n(2) "
        +"view all open appointments\n3(3) make an appointment\n(4)return to patient menu\n")
        make_an_appointment_menu(patient_id, choice)

def view_medical_record(patient_id):
    file_path = sys.path[0] + "/medical_records/"
    for file in os.listdir(file_path):
        f = open(file_path + patient_id + ".txt", 'r+')
        lines = f.readlines()
        for line in lines:
            print(line)

def view_upcoming_appointments(patient_id):
    upcoming_appointments = {}
    file_path = sys.path[0] + "/appointments/"

    for file in os.listdir(file_path):
        f = open(file_path + file, 'r+')
        lines = f.readlines()
        for line in lines:
            split_line = line.split("-")
            time = split_line[0]
            status = split_line[1].strip()
            if patient_id == status:
                upcoming_appointments[file[:-4]] = time

    for x in upcoming_appointments:
        print(x, upcoming_appointments[x])

def cancel_an_appointmnet(patient_id):
    date = input("please select a date in the following format: YYYY-MM-DD\n")
    file_path = sys.path[0]+"/appointments/"+date+".txt"
    while not isfile(file_path):
        date = input("date is either not in range (weekdays in next 6 months) or is not in YYYY-MM-DD format, please try again\n")

    f = open(file_path, 'r+')
    selected_days_current_appointments = {}
    lines = f.readlines()
    for line in lines:
        line_split = line.split("-")
        time = line_split[0]
        status = line_split[1]
        status = status.strip()
        selected_days_current_appointments[time] = status
    time_found = False
    quit = False
    time = "---"
    while not time_found and not quit:
        while not time in selected_days_current_appointments:
            time = input("please select an open time in the example format 9:00am or type 'q' to quit\n")
            time_found = True
        if time == "q":
            quit = True
            patient_menu(patient_id)
        status = selected_days_current_appointments[time]
        if status.strip() == patient_id:
            selected_days_current_appointments[time] = "open"
    f.close()
    f = open(file_path, 'w')
    for key, value in selected_days_current_appointments.items():
        f.write('%s-%s\n' % (key, value))
    f.close()
    print("appointment on " +date+ " at " + time + "cancelled")
    patient_menu(patient_id)

def admin_login():
    username_success = False
    password_success = False

    file_path = sys.path[0]+"/admin_logins/admin_login.txt"

    while not username_success or not password_success:
        username_input = input("please enter your admin username\n")
        password_input = input("please enter your admin password\n")

        if username_input == get_line_from_file(file_path,1).strip():
            username_success = True
        if password_input == get_line_from_file(file_path, 2).strip():
            password_success = True
        
        if not username_success or not password_success:
            choice = input("incorrect login \n(1) try again\n(2) return to main menu\n")
            if choice == "2":
                menu()
    admin_menu()

def register_new_patient():
    patient_id = get_unique_id()
    print("Welcome to Central Medical Clinic. You will be prompted to provide some information in order to set up your profile\n"+
    "Pressing enter will move to move to the next item.")
    first_name = input("first name: \n")
    middle_name = input("middle name: \n")
    last_name = input("last name: \n")
    correct_format = False
    birth_date = ""
    dob_year = ""
    dob_month = ""
    dob_day = ""
    while not correct_format:
        birth_date = input("date of birth: (format YYYY-MM-DD) \n")
        test = birth_date.split("-")
        count = 0
        for i in test:
            count+=1

        if count == 3:
            dob_year = test[0]
            dob_month = test[1]
            dob_day = test[2]
        if count == 3 and len(birth_date) == 10 and dob_year.isnumeric() and dob_month.isnumeric() and dob_day.isnumeric():
            dob_year = int(dob_year)
            dob_month = int(dob_month)
            dob_day = int(dob_day)
            if dob_month > 0 and dob_month < 13 and dob_day > 0 and dob_day < 32:
                correct_format = True #at least they used the dashes
        else:
            print("Please use format YYYY-MM-DD for date of birth")
    phone = input("phone: \n")
    email = input("email: \n")
    address = input("address: \n")

    new_patient = Patient(first_name,middle_name,last_name,dob_year,dob_month,dob_day,phone,email,address)

    vaccine_history = input("please indicate vaccine histroy or write \"not sure\"\n")
    medication_history = input("please list current medications\n")
    ailment_history = input("please list any significant health issues you have experienced\n")
    family_history = input("please describe pertinent hereditory family medical history\n")
    allergies = input("please list all known allergies\n")
    surgeries = input("please describe any surgeries you have undergone\n")

    new_medical_record = MedicalRecord(patient_id,vaccine_history,medication_history,ailment_history,family_history,allergies,surgeries)

    correct_input = False
    ssn = ""
    other_id = ""
    
    while not correct_input:
        choice = input("do you have a social security number? (y/n)\n").lower()
        if choice == "y" or choice == "n":
            correct_input = True
    
    if choice == "y":
        ssn = input("please enter your social security number\n")
        other_id = "N/A"
    else:
        ssn = "N/A"
        other_id = input("In a single line, please enter another type of governemt ID and state the ID-type\n")
    
    new_identifier = Identifier(patient_id,ssn,other_id)

    print("your patient ID is " + patient_id)

    new_patient.set_patient_id(patient_id)
    new_patient.write_patient_to_file(patient_id)

    username_valid = False
    username = ""
    
    path = sys.path[0] + "/logins/"

    while not username_valid:
        username = input("Please select a username\n")

        found = 0

        for file in os.listdir(path):
            test_username = get_line_from_file(path+file,1)
            if username == test_username.strip():
                found = 1
        if not found:
            username_valid = True
        else:
            print("username already exists\n")
    
    password_valid = False

    while not password_valid:
        password = input("please select a password at least 8 characters long\n")
        if len(password) >= 8:
            password_valid = True
    
    new_login = Login(patient_id,username,password)

    menu()

def delete_patient_info(patient_id):
    file_path = sys.path[0]+"/patients/"+ patient_id + ".txt"

    if os.path.exists(file_path):
        os.remove(file_path)

def delete_medical_records(patient_id):
    file_path = sys.path[0]+"/medical_records/"+ patient_id + ".txt"

    if os.path.exists(file_path):
        os.remove(file_path)


def delete_identifier(patient_id):
    file_path = sys.path[0]+"/identifiers/"+ patient_id + ".txt"

    if os.path.exists(file_path):
        os.remove(file_path)


def delete_login(patient_id):
    file_path = sys.path[0]+"/logins/"+ patient_id + ".txt"

    if os.path.exists(file_path):
        os.remove(file_path)

def delete_patient():
    found = 0
    test_path = sys.path[0] + "/patients/"
    patient_id = ""
    while not found and patient_id != "q":
        patient_id = input("please enter a patient ID")
        if os.path.isfile(test_path + patient_id + ".txt"):
            found = 1
        else:
            patient_id = input("patient not found, please try again or type 'q' to go back to admin menu")
            if patient_id == "q":
                admin_menu()
    delete_patient_info(patient_id)
    delete_medical_records(patient_id)
    delete_identifier(patient_id)
    delete_login(patient_id)
    admin_menu()
        
def menu():
    print("Welcome to Central Medical Clinic\n")
    patient_id = ""
    login_choice = " "
    while login_choice != "p" and login_choice != "a" and login_choice != "r" and login_choice != "e":
        login_choice = input("Please choose from the following options:\n (P) patient login\n(A) admin login\n(R) register as a new patient\n(E) exit\n")
        login_choice = login_choice.lower()

    if login_choice == "p":
        patient_login()
    elif login_choice == "a":
        admin_login()
    elif login_choice == "r":
        patient_id = register_new_patient()
    else:
        return
menu()




