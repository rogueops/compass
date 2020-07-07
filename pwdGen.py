'''
ComPass
Python Complex Password Generator
Created By Nicore

GNU License 2020
Built 07-03-2020
'''
import random 
import string

#Ask user password length
size = int(input("Enter length of wanted password: "))

#Creating a combined list
bits = list(string.printable)

#shuffling combined list
random.shuffle(bits)

#Print new password
#print("Your new complex password of",size,"characters is: \n")
print("\nNew Password:",''.join(random.sample(bits,size )))
