with open('file.txt','r') as file:
    data = file.read()
    print(data)
    file.close()
countu=0
countl=0
countp=0
countlines=0
for alp in data:
    if alp.isupper():
        countu+=1
    elif alp.islower():
        countl+=1
    elif not (alp.isalpha() and alp.isdigit() and alp.isspace()):
        if alp != ' ' and alp != '\n':
            countp+=1
            print(alp)
with open('file.txt','r') as file:
    data= file.readlines()
    for line in data:
        countlines+=1

print("Number of uppercase letters: ",countu)
print("Number of lowercase letters: ",countl)
print("Number of punctuation marks: ",countp)
print("Number of lines: ",countlines)