'''
#to read from the file

f =open("harry.txt","r")
content = f.read()

print(content)

f.close()
'''

'''
#over Ride all the data
f= open ("john.txt","w")

String="""john is a person with pandas Knowwlge"""
f.write(String)

f.close
'''

'''
f= open ("john.txt","a")

String="""john is a person with pandas Knowwlge,and he is from Myosreee"""
f.write(String)

f.close

'''

#to read the file content line by line

f=open("harry.txt", "r")

for line in f:
    print(line)

f.close()



