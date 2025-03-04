with open("Files,Directories&paths/read.txt") as file:
    file = file.read()
    print(file)




with open("Files,Directories&paths/write.txt","w") as file:
    file = file.write("Hello Python!")
  

with open("Files,Directories&paths/write.txt","a") as file:
    file = file.write("\nHello Python!")