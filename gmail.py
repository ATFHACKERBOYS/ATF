import random
import os
import sys

"\033[1;92m"
os.system("figlet GMAIL")
print("[Coder] : {<°°Dead Devil°°>} ")
print("[FB] : www.facebook.con/page/Dead Devil")
print("<=====================>")



atf=str(input("Enter Your Amount: "))
num="abcdefghijklmnopqrstuvwxyz1234567890"
for i in range(10):
	passwordlen=6
	passwrd="".join(random.sample(num,passwordlen))
	print(passwrd+"@gmail.com")