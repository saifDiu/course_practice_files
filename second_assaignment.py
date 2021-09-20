#Step-1

product_name=(str(input("Enter Your Product Name:")))
product_name_lenth=(len(product_name))
print("Data Lenth=", product_name_lenth)
#Step-2

if product_name_lenth>10:
    print("condition=",product_name_lenth+10)
else:
    print("condition=",product_name_lenth-10)
#Step-3
country_name="Bangladesh"
print("Indexing value=",(country_name[2]+country_name[5]+country_name[7]+country_name[8]))

#Step-4
book_name="array,lol, taza"
print("Starts With condition=",book_name.startswith('p'))




