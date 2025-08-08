# #what is string name = 'vivek'
# name = "vivek" 0 to ... and -1 to ... from back
# name = '''vivek'''
# string is imutable
# [:4]=[0:4]
# [1:]=[1:len]

name='Vivek'
sl_name= name[0:3]  #o upto 3
char1=name[1]

print(name)
print(sl_name)
print(char1)

#sliving with skip

print(name[0:5:2])

#Function of string

print(len(name))

print(name.endswith("vek"))
print(name.startswith("vek"))

print(name.count("v"))
print(name.capitalize())

print('viv' in name)

print("vi,v,ek".split(','))
print("vi.v.ek".split('.'))
",".join(['h','i'])

",".join(['a', 'b'])

# escape seq char  \n, \t, \\, \', \""