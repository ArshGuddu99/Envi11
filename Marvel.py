# main code
import random   #for randomly choosing two superheroes
import Superheroes
import Rating
import Calculate
i=0
print'To beat Thanos - 8'
print'list of Superheroes'
while(i<=11):
    print Superheroes.superheroes[i]    #lists the available superheroes
    i+=1
    y = random.randint(0, 11)   #generates random integer between 0 and 11
    z = random.randint(0, 11)   #generates random integer between 0 and 11
    while(z==y):
        z=random.randint(0, 11) #ensures that the random numbers are different
print'Your two superheroes are\n'
print Superheroes.superheroes[y]
print Superheroes.superheroes[z]
print'Complete the team by entering two more superheroes\n'
string1=raw_input()
string2=raw_input()
count1=0
while count1<=11 and string1!=Superheroes.superheroes[count1]:  #compares with the list of superheroes
    count1+=1
count2=0
while count2<=11 and string2!=Superheroes.superheroes[count2]:
    count2+=1
a=Rating.strength(y)
b=Rating.strength(z)
c=Rating.strength(count1)
d=Rating.strength(count2)
Effective_Strength= Calculate.average(a,b,c,d)
print'Effective strength of superhero team:',Effective_Strength
if Effective_Strength>=8:
    print'Congratulations'
else:
    print'You Lose'
print'End of game'