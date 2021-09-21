patient_name=(str(input("Enter patient Name:"))).upper()
patient_address=(str(input("Enter patient Address:"))).upper()
patient_age=(int(input("Enter patient Age:")))
patient_weight=(int(input("Enter patient Weight:")))
patient_id=(int(input("Enter patient ID:")))

print("===Blood Test Report ===")
print("Welcome",patient_name.format())
if patient_id<=50000 :
  print("patient Name:",patient_name ,'\n' "patient Address:",patient_address,'\n' "patient ID:", patient_id,'\n' "patient Age:",patient_age,'\n'"patient weight:",patient_weight)
else:
  print("Data Not Found")
if patient_age>=60 and patient_weight>=90:
  print("Test Report:","Your Blood Presure is High")
else:
  print("Test Report:", "Your Blood Presure is Normal")




    




