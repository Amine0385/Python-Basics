while True :
    x = float(input ("put your first number :"))
    c = str(input("put your operation :"))
    y = float(input ("put your second number :"))
    if c in ("+"):
        print(x + y)
    elif c in ("-"):
        print(x - y)
    elif c in ("*"):
        print(x * y)
    elif c in ("**"):
        print( x ** y)
    elif y in {0}:
        print(f" dividing by 0 is not possible")
    elif c in ("/"):
        print(x / y)
    else:
        print(f"erreur please enter a correct operation like: (+ - * ** /)")