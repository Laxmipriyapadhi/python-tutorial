

with open ("log.txt", "w")as file:
        file.write("hello,this is log text.")
with open("log.txt", "r")as file:
        content =  file.readlines()
        print(content)

