from twilio.rest import Client

import csv 
filename = "stats.csv"
rows = []

with open(filename, 'r') as csvfile: 
	csvreader = csv.reader(csvfile) 
	l=[]
	for row in csvreader:
		# print(row)
		for r in row:
			l.append(r)
			print(r)

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACCOUNT_SID'
auth_token = 'AUTH_TOKEN'
client = Client(account_sid, auth_token)

txt='Coronavirus live Statistics:\nTotal cases:'+l[1]+'\nNew cases: '+l[2]+'\nDeaths:         '+l[3]+'\nNew Deaths:  '+l[4]
message = client.messages \
                .create(
                     body=txt,
                     from_='+12052931***',
                     to='+1213275****'
                 )

print(message.sid)