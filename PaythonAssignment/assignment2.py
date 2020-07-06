age = input("Are you a cigarette addict older than 75 years old? : ").title().strip()=="Yes" 
chronic =input("Do you have a severe chronic disease? : ").title().strip()=="Yes"  
immune = input("Is your immune system too weak? : ").title().strip()=="Yes" 
if age or chronic or immune:
    print('You have a high death risk in case covid-19, stay home!')
else:
    print('You are safe from covid-19. But still, think the others and be cautious.')
