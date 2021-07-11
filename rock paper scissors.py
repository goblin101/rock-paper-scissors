rock=0
paper=1
scissors=2
import random
list_options=["rock","scissors","paper"]
a=random.choices(list_options)
print("rock paper scissors game")
b=(input("select rock, paper or scissors: "))
# print(a,b)
if (b=="rock" and a[0]=="scissors")or(b=="paper" and a[0]=="rock")or(b=="scissors" and a[0]=="paper"):
    print("you win")
elif (b=="rock" and a[0]=="paper")or(b=="paper" and a[0]=="scissors")or(b=="scissors" and a[0]=="rock"):
    print("you lose")
elif (b=="rock" and a[0]=="rock")or(b=="paper" and a[0]=="paper")or(b=="scissors" and a[0]=="scissors"):
    print("draw")

else:
    print("error")
print("you chose "+b+" and the computer chose "+ a[0])
