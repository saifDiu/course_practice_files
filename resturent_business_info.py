
#Resturent Business User Information and Food Menu Details and Calculate Bill

customer_name=input("Customer Name:")
customer_phone_no=input("Phone No:")


print("==Input Food Menu Price==")
rice=int((input("Rice(Tk):")))
vegetable=int((input("Mixer Vegetable (Tk):")))
fish=int((input("Fish(Tk):")))
beef=int((input("Beef(Tk):")))
cold_drinks=int((input("Cold Drinks(Tk):")))

total_bill=rice+vegetable+fish+beef+cold_drinks
print("Total Bill is=", total_bill)



