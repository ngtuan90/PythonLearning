# Phan mem de chuyen doi nhiet do tu do F qua do C va nguoc lai
# Author: Minh Nguyen
# Date: 10/15/2016

# nhap input
temp=float(raw_input('Enter a temperature'))
convert=raw_input('Convert to (F)ahrenheit or (C)elsius? ')
if convert=='F' or convert=='f':
    tempf = (9.0 / 5) * temp + 32
    print temp,' C = ',tempf,' F'
elif convert=='C' or convert=='c':
    tempc = (5.0/9)*(temp-32)
    print temp,' F = ',tempc,' C'
else:
    print 'you type wrong, please type again'
