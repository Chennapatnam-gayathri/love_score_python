name1=input("Enter your name: ")
name2=input("Enter your's love name ")
combine_string=name1+name2
name3=combine_string.lower()

t=name3.count("t")
r=name3.count("r")
u=name3.count("u")
e=name3.count("e")
true=t+r+u+e

l=name3.count("l")
o=name3.count("o")
v=name3.count("v")
e=name3.count("e")
love=l+o+v+e

love_score=int(str(true)+str(true))
if love_score<10 or love_score >90:
    print(f"your score is {love_score} and you go together like coke and mentors")
elif love_score>=40 or love_score <=50:
    print(f"your score is {love_score} and you are alright together")
else:
    print(f"your score is {love_score} ")
