def checkleap(year):
 if ((year % 400== 0)or (year % 100 != 0)and (year  % 4 == 0)):
   print('leapyear')
 else:
     print( 'not leap')
year = int(input('enter year:'))
checkleap(year)
     
