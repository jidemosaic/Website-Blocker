import time
from datetime import datetime as dt

#This section stores the hosts paths, redirect ip address,website list, start and end time for blocking the websites in a variable.

w_hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
maclin_hosts_path = r"/etc/hosts"
redirect = "127.0.0.1"

#You can modify this list below by adding websites you might want to block or removing existing ones
website_list = ["facebook.com", "yahoomail.com"]

#You can change the start time (start_time) and end time (end_time) to a number in 2400hrs format. This is the time between which the script blocks the websites in the list.
start_time = 8 
end_time = 20  

while True:
	if dt(dt.now().year,dt.now().month,dt.now().day, start_time) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,end_time):
		print("This is a working hour. Please reconnect after 1600hrs")
		with open(w_hosts_path or maclin_hosts_path, "r+") as file:
			content = file.read()
		
			for website in website_list:
				if website in content:
					pass
				else:
					file.write( redirect + "    " + website + "\n" )
					
	else:
		with open(w_hosts_path or maclin_hosts_path, "r+") as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any (website in line for website in website_list):
					file.write(line)
			file.truncate()
		print("You are now in leisure hour")
		
	time.sleep(5)
		 
