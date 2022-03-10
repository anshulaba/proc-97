
introString=input("Enter you introduction: ")
print(introString)

characterCount=0
wordCount=1

for i in introString:
    characterCount=characterCount+1
   
    if(i==" "):
        wordCount=wordCount+1
        
print("Number of word in the string is: ",wordCount)
print("Number of character in the string is: ",characterCount)


