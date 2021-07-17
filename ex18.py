from sys import argv

script, f_file, t_file = argv

print("we will copy %s file to %s this file"%(f_file,t_file))

in_file = open(f_file)
in_data = in_file.read()


out_file = open(t_file,'w')
out_file.write(in_data)
out_file = open(t_file)
print(out_file.read())

in_file.close()
out_file.close()
