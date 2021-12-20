
print ("Print leap year between two given years")
print ("Enter current year")
currentYear = int(input())
print ("Enter last year")
endYear = int(input())
 
print ("List of leap years:")
for year in range(currentYear, endYear):
  if (0 == year % 4) and (0 != year % 100) or (0 == year % 400):
    print (year)
