age = input("Are you a cigarette addict older than 75 years old? : ") 
chronic =input("Do you have a severe chronic disease? : ")  
immune = input("Is your immune system too weak? : ") 
if age.lower()[0] == 'y' and chronic.lower()[0] == 'y' and immune.lower()[0] == 'y':
    print('You have a high death risk in case covid-19, stay home!')
else:
    print('You are safe from covid-19. But still, think the others and be cautious.')
