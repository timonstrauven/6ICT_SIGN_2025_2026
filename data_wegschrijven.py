f = open("mijndata.txt","w")

f.write("Dit is regel 1\n")
f.write("Dit is regel 2\n")

f.close()

f=open("mijndata.txt","a")

f.write("Dit is regel 3\n")
f.write("Dit is regel 4\n")

f.close()

f = open("mijndata.txt","r")

inhoud = f.read()
print(inhoud)

f.close()