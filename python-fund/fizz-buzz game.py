number = int(input("enter a number:"))
for i in range(1,number ):
    if i % 3 ==0 :
      print(f"fizz")
    elif i % 5 ==0:
      print(f"buzz")
    elif i % 5==0 or i % 3 ==0 :
        print(f"fizzbuzz")
    else:
      print(i)