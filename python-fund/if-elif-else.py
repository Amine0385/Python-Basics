year =int(input("year :"))
if year % 4 == 0:
    print(f"{year} is a leap year")  
elif year % 100 == 0 or year % 400 == 0 :
    print(f"{year} is not a leap year" )
else:
    print(f" {year} is not a leap year")