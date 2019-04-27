while True:
    input_one=input("This is a multiplication/division table whatever number you type it will give u answer.. ")
    input_two=input("What is the length of the table? .. ")
    getOut = 0
    while getOut==0:
        input_three=input("Do u want to use multiplication or division ( *or/ )")
        var2=1
        while var2 < int(input_two)+1:
            if input_three == "*":
                print(str(input_one) + " * " + str(var2) + " = " + str(int(var2)*int(input_one)))
            elif input_three == "/":
                print(str(input_one) + " / " + str(var2) + " = " + str(int(input_one)/int(var2)))
            else:
                print("Invalid Answer")
                break
            var2 +=1
            getOut=1
