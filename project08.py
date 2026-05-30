#file name reader example of directory
def file_reader():
    operator=input(" Enter file name which you right: ")
    lst=["newfile.py"] # example file name 
    if operator not in  lst:
        print("wrong file is not in directory")
    elif operator in lst:
       print(operator)
#File reading proce
    f=open(operator)
    data=f.read()
    f.close()
    print(data)

#File writing method 
def file_writee():
  user=input("Write in file: ")
  lst=("newfile.py")
  s=open("file.py","w")
  w=s.write(user)
  print(w)
  s.close()
file_reader()
file_writee()