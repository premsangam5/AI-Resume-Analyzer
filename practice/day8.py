'''file = open("resume.txt", "r")

content = file.read()

print(content)

file.close()'''




'''
with open("resume.txt", "r") as file:
    content = file.read()

print(content)'''

'''
with open("resume.txt", "r") as file:

    for line in file:
        print(line.strip())'''



'''
try:
    with open("resume.txt", "r") as file:
        resume = file.read()

    print("===== RESUME ANALYZER =====")
    print(resume)

except FileNotFoundError:
    print("Resume file not found!")'''




try:
    with open("res.text","r") as file:
        res=file.read()
    print("===== RESUME ANALYZER =====")    
    print(res)

except FileNotFoundError:
    print("Resume file not found!")    
