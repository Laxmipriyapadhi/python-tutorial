## Create and write something in a file and then read the file and print the content, using with statement.

with open ("log.txt", "w")as file:
        file.write("hello,this is log text.")
with open("log.txt", "r")as file:
        content =  file.readlines()
        print(content)

