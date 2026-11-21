"""def greet(ame,name):
    print("hello world",ame)
    print("hello world",name)
greet("prem","raj")"""
'''
def add(a,b):
    return a+b
result=add(10,20)
print(result)'''
'''
def countskill(skills):
    total=len(skills)

    return total
skills=["puthon","java","c++"]
result=countskill(skills)
print(result)'''



"""

def candidate(name,branch,skills):
    print("\n===candidate profile===")
    print("Name:", name)
    print("Branch:", branch)
    print("\n skills")
    for skill in skills:
        print("--",skill)

def countskills(skills):
    return len(skills)

name=input("enter your name :") 
branch=input("enter your branch :")
skills=["java","python","c++"]
def display_candidate(name, branch, skills):
    candidate(name, branch, skills)

display_candidate(name,branch,skills)
total=countskills(skills)
print("\n",total)
    """



'''

def display_candidate(name, college, skills):
    print("\n===== CANDIDATE PROFILE =====")
    print("Name:", name)
    print("College:", college)

    print("\nSkills:")

    for skill in skills:
        print("-", skill)


def count_skills(skills):
    return len(skills)


name = input("Enter your name: ")
college = input("Enter your college: ")

skills = ["Java", "Python", "SQL"]

display_candidate(name, college, skills)

total = count_skills(skills)

print("\nTotal skills:", total)'''



'''
def welcome():
    print("Welcome to AI Resume Analyzer")
welcome()'''



'''
def calculatematch(match,total):

    percentage =(match/total)*100
    return percentage
result=calculatematch(5,10)
print(str(result)+"%")'''


'''
candidate = {
    "name": "prem",
    "college": "ABC University",
    "skills": ["Python", "Java", "SQL"]
}
print(candidate.get("name"))
candidate["cgpa"] = 6.6
print(candidate)
skills = {"Python", "Java", "SQL", "Python"}

print(skills)
skills = ["Python", "Java", "Python", "SQL", "Java"]

unique_skills = set(skills)

print(unique_skills)'''







'''
resume={
    "name":"prem",
    "college":"nsec",
    "branch":"ece",
    "skills":{"python","java","c++","python"}
}
print(resume["name"])
for key, value in resume.items():
    print(key,":",value)

resume["cgpa"]=6.6
resume["skills"].add("sql")
print(resume)'''










