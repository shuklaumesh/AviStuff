askBasicQuestion = True
while True:
    if askBasicQuestion==True:
        input_one=input("This is a multiplication/division/addition table whatever number you type it will give u answer... ")
        input_two=input("What is the length of the table? ... ")
    input_three=input("Do u want to use multiplication or division or addition or subtraction or exponents( *or/or+or-or** )")
    if input_three == "*":
        var2=0
        while var2 < int(input_two)+1:
            print(str(input_one) + " * " + str(var2) + " = " + str(int(var2)*int(input_one)))
            var2 +=1
        askBasicQuestion = True
    elif input_three == "/":
        var2=1
        while var2 < int(input_two)+1:
            print(str(input_one) + " / " + str(var2) + " = " + str(int(input_one)/int(var2)))
            var2 +=1
        askBasicQuestion = True
    elif input_three == "+":
        var2=0
        while var2 < int(input_two)+1:
            print(str(input_one) + " + " + str(var2) + " = " + str(int(var2)+int(input_one)))
            var2 +=1
        askBasicQuestion = True
    elif input_three == "-":
        var2=0
        while var2 < int(input_two)+1:
            print(str(input_one) + " - " + str(var2) + " = " + str(int(input_one)-int(var2)))
            var2 +=1
        askBasicQuestion = True
    elif input_three == "**":
        var2=0
        while var2 < int(input_two)+1:
            print(str(input_one) + " ** " + str(var2) + " = " + str(int(input_one)**int(var2)))
            var2 +=1
        askBasicQuestion = True
    else:
        print("Invalid Operation")
        askBasicQuestion = False
