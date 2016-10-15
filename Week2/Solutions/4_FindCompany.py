#Find company name in email
#Author:Minh Nguyen
#Date: 10/15/2016
email=raw_input("enter your email:")
a=email.find('@')
b=email.find('.')
c=email[a+1]
for i in range(a+2,b):
    c=c+email[i]
print c
