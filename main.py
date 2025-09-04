#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = open("./Input/Names/invited_names.txt","r")
names_list = names.readlines()

for i in range(0,len(names_list)):
    names_list[i] = names_list[i].strip()


letter = open("./Input/Letters/starting_letter.txt","r")
temp =letter.read()

for name in names_list:
    demo = open("./Output/ReadyToSend/"+i+".txt","w")
    demo.write(temp.replace("[name]",name))
    demo.close()

