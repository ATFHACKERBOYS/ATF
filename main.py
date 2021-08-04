import os
import sys

logo='''ATF'''

print(logo)

while True:
	os.system("clear")
	print(" [1] SMS BOMBER\n [2] Gmail Genaretor\n [3] Password Genaretor\n [4] Number Genaretor")
	print("<==========================>")
	a=str(input("[<]select ypur option: "))
	os.system("clear")
	if a=="1":
		os.system("python3 data.py")
		a=input( )
	elif a=="2":
		os.system("python3 gmail.py")
		a=input( )
	elif a=="3":
		os.system("python3 sqlmap.py")
		a=input( )
	elif a=="4":
		os.system("python3 number.py")
		a=input( )
	else:
		print("[×] wrong value Enter")
		a=input( )
	os.system("clear")
				
	
