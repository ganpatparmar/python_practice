from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("We will copy %s file to %s file"%(from_file,to_file))


in_file = open(from_file)
in_data = in_file.read()

print("The input file is %d bytes long"% len(from_file))
print("Let's check weather the file exist or not? %s"%exists(from_file))
print("If you want to continue then press return else press CTR-C to exit")
input('>')
out_file = open(to_file,'w')
out_file.write(in_data)
print("Now we have closed the file.\n thanks for being here")
out_file = open(to_file)
print(out_file.read())

in_file.close()
out_file.close()
