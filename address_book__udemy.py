"""This is an address book"""
#group of lists
#This is coantact1's details list
umeshList = ["Full Name: Umesh Shukla", "Email Address: umeshdataman@hotmail.com", "Second Email Address: umeshdataman@gmail.com", "Current Address: 7320 Gallagher Dr, Apt. 210 Edina, MN 55435", "Phone Number: +1(612)-876-6924", "Skype: umeshdataman@hotmail.com"]
#This is coantact2's details list
aviList = ["Full Name: Avi Shukla", "Email Address: aavart.shukla@outlook.com", "Current Address: 7320 Gallagher Dr, Apt. 210 Edina, MN 55435", "Phone Number: None, is a 8-year old", "Skype: aavart.shukla@outlook.com"]
#This is coantact3's details list
jyotiList = ["Full Name: Jyoti Misra", "Email Address: jyotimisra20@gmail.com", "Second Email Address: jyoti_m20@yahoo.com", "Third Email Address: jyoti.misra@hotmail.com", "Current Address: 7320 Gallagher Dr, Apt. 210 Edina, MN 55435", "Phone Number: +1(952)-594-0242", "Skype: jyoti.misra@hotmail.com"]
#This is coantact3's details list
mamaList = ["Full Name: Deepak Misra"]
 
#dictionary using data of lists
address_book = {}
address_book["Pappa"] = umeshList
address_book["Avi"] = aviList
address_book["Mamma"] = jyotiList
address_book["Mama"] = mamaList

#print statements
##print(address_book)
inp1=input("Which contact do you want?")

if inp1 == '
