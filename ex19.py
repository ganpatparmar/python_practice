
#defination of first function with *argv
def print_first(*argv):
    arg1, arg2 = argv
    print("Argumnet 1 : %s \n Argument 2 : %s"%(arg1,arg2))
#gefination of second function with two arguments
def print_again(arg1,arg2):
    print("Argument 1 : %s \n Argument 2 : %s "%(arg1,arg2))
#defination of third funtion with one argument
def print_one(arg1):
    print("Argument 1 : %s"%(arg1))
    
#defination of last function eith no arguments
def no_arg():
    print("This function has no arguments")
    
#function call
print_first("Ganpat","PArmar")
print_again("Ganpat","Parmar")
print_one("First")
no_arg()

#1. Did you start your function defi nition with def? yes
 #2. Does your function name have only characters and _ (underscore) characters? yes
 #3. Did you put an open parenthesis ( right after the function name? yes
 #4. Did you put your arguments after the parenthesis ( separated by commas? yes
 #5. Did you make each argument unique (meaning no duplicated names)?yes
 #6. Did you put a close parenthesis and a colon ): after the arguments?yes
 #7. Did you indent all lines of code you want in the function four spaces? No more, no less. Yes
 #8. Did you “end” your function by going back to writing with no indent (dedenting we call it)?yes
#And when you run (“use” or “call”) a function, check these things:
 #1. Did you call/use/run this function by typing its name?yes
 #2. Did you put the ( character after the name to run it?Yes
 #3. Did you put the values you want into the parenthesis separated by commas? yes
 #4. Did you end the function call with a ) character? yes
#Use these two checklists on the remaining lessons until you do not need them anymore. Finally, 
#repeat this a few times: “To ‘run,’ ‘call,’ or ‘use’ a function all mean the same thing.”  
    