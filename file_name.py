file=input("Enter file name: ")
a=file.endswith(".py")
b=file.endswith(".html")
c=file.endswith(".css")
d=file.endswith(".jpg")
e=file.endswith(".php")
if a:
    print("The extension of the file is:'python'")
elif b:
    print("The extension of the file is:'html file'")
elif c:
    print("The extension of the file is:'css file'")
elif d:
    print("The extension of the file is:'jpg file'")
elif e:
    print("The extension of the file is:'php file'")
else:
    print("enter valid file name")
    

