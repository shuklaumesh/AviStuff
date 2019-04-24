def tables()
    input_one=input("This is a multiplication table whatever number you type it will give u answer.. ")
    input_two=input("What is the end za of the table? .. ")
    product = input_one
    var2=0
    while var2 < int(input_two)+1:
        print(str(product) + " * " + str(var2) + " = " + str(int(var2)*int(product)))
        var2 +=1
