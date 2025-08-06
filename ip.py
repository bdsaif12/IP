import os
import sys
import time

os.system ("clear")
print("\n\n\n")
a = "       ASSALAMU ALAIKUM\n"

for b in a:
	sys.stdout.write(b)
	sys.stdout.flush()
	time.sleep(0.1)
print("\n\n\n")


os.system ("clear")
print("\n\n\n")

a = "      \033[1;33m Method Loading....\n"

for b in a:
	sys.stdout.write(b)
	sys.stdout.flush()
	time.sleep(0.1)



name =input(" Your Name: ")

print("Hey "+name+"..Please Wait")

time.sleep(2)

os.system ("clear")
print("\n\n\n")

a = "       \033[1;32m Succesfully Loaded....\n"

for b in a:
	sys.stdout.write(b)
	sys.stdout.flush()
	time.sleep(0.1)
print("\n\n\n")
time.sleep(2)
os.system ("clear")



print ("""



\033[1;31m 


   _____       _       _   
  / ____|     (_)     | |  
 | |  __  __ _ _ _ __ | |_ 
 | | |_ |/ _` | | '_ \\| __|
 | |__| | (_| | | | | | |_ 
  \\_____|\\__,_|_|_| |_|\\__|
                           
                           

                                                      
 \033[1;36m======================================================                                                     
         
\033[1;32m NAME  : GAINT
GITHUB : GAINT404
THANK YOU SO MUCH 

\033[1;36m======================================================

                             
                                                                   """)




import requests


ip= input("Enter Your Ip Adress : ")

req= requests.get("http://ip-api.com/json/"+ip)


txt= req.json()

print(f"\033[1;32mCountry: {txt['country']}")
print(f"Country Code: {txt['countryCode']}")
print(f"Region: {txt['regionName']}")
print(f"City: {txt['city']}")
print(f"Lat: {txt['lat']}")
print(f"Lon: {txt['lon']}")
print(f"Query: {txt['query']}")
print(f"isp: {txt['isp']}")


#{'status': 'success', 'country': 'Bangladesh', 'countryCode': 'BD', 'region': 'C', 'regionName': 'Dhaka Division', 'city': 'Dhaka', 'zip': '1212', 'lat': 23.7891, 'lon': 90.4126, 'timezone': 'Asia/Dhaka', 'isp': 'grameenphone limited', 'org': 'grameenphone limited', 'as': 'AS24389 GrameenPhone Ltd.', 'query': '37.111.194.189'}



#txt= req.json()



