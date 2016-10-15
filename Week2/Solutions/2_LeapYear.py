#tim nam nhuan
#Author: Minh Nguyen
#date: 10/15/2016

year=int(raw_input('What year:'))
if year%400==0:
    print year,'is a leap year'
elif year%4==0 and year%100!=0 :
    print year,'is a leap year'
else:
    print year,'is not a leap year'
