from Classes import MedicalRecord, Patient
import os
import sys
from pathlib import Path
import datetime


#citation: https://djangocentral.com/check-if-a-directory-exists-if-not-create-it/p
logins_dir = ("logins")
patients_dir = ("patients")
appointments_dir = ("appointments")
medical_records_dir = ("medical_records")
identifier_dir = ("identifiers")

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

os.chdir(identifier_dir)


#citation: https://stackoverflow.com/questions/2967194/open-in-python-does-not-create-a-file-if-it-doesnt-exist

test_path = sys.path[0] + '/identifiers/next_open_id.txt'
if os.path.isfile(test_path):
    pass
else:
    file = open('next_open_id.txt', 'w')
    file.write("1111111111")
    file.close()

first = Patient('first','middle','last',1956,12,2,'444-444-4444','first@first.net','123 first street, first, firstistan')

first.set_first_name("Bob")

first_med = MedicalRecord(first.get_patient_id(),"covid 19 and the others", "lots of stuff", "a really loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong history I'm using to test the line length","some stuff here and there on both sides","none","none that I recall")
first_med.get_vaccine_history()

date = datetime.date.today()

appointments = {"8:00am":"open", "8:40am":"open","9:20am":"open","10:00am":"open","10:40am":"open","11:20am":"open","1:00pm":"open","1:40pm":"open","2:20pm":"open","3:00pm":"open","3:40pm":"open","4:20pm":"open"}

for i in range(180):
    print(str(date))
    date += datetime.timedelta(days=1)
    
    filename = str(date)
    weekday_check = date.weekday()
    if(weekday_check < 5): #citation: https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python
        f = open(sys.path[0] + "/appointments/" + filename + ".txt", 'w')
        for key, value in appointments.items(): 
            f.write('%s:%s\n' % (key, value))
        f.close()




