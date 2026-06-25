try:
    num1, num2 = eval(input("Enter two numbers seperated by comas: "))
    result = num1/num2
    print("Result is : ", result)
    #print("Result is : ", result2) #this is the name error
    #code = "if True print('Yes')"
    #exec(code)

except ZeroDivisionError:
     print("Division by zero is not allowed")

except SyntaxError:
     print("Syntax error")

except ValueError:
     print("Please enter nuumeric value")

except NameError as ex:
     print("The name error exception is ", ex)

except:
     print("Some error occured")

else:
     print("no exception or no error")

finally:
     print("I will execute no matter what happens")