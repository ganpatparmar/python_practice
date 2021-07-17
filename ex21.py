from sys import argv #first import 
script, file = argv #declalre argv
def print_all(f):
    print(f.read())#1 defination of function(wh=ich print whole file)
def rewind_1(f):#rewinding a function
    f.seek(0)
    
def print_line(l_no,f):#secon defination which print a file line by line
    print(l_no,f.readline())
    
current_file = open(file)#then opening a fileprinting a first file 

print("First lets print whole file: \n")#calling a first function
print_all(current_file)
print("Now lets rewind. kind of a Tape.")#lets rewind a funtion
rewind_1(current_file)
#then print a funtion line by line
print("Now lets print whole file line by line")
current_line = 1
print("line 1 %s"%(print_line(current_line,current_file)))
current_line+=1
print_line(current_line,current_file)
current_line+=1
print_line(current_line,current_file)






