#Which_Fantasy_Hero_Are_You
 

Wizard = 0
Swordsman = 0
Fighter = 0
Shapeshifter = 0
Dark_Mage = 0

question1 = int(input('How do you approach new challenges?\n 1) I take my time and plan ahead\n 2) Do now, think later!\n 3) I let someone else figure it out for me..\n 4) I adapt based on the situation\n'))
question2 = int(input('How do you like to spend your time?\n 1) Studying and learning new things\n 2) Testing my strength and endurance\n 3) Quietly crafting or reading\n 4) Helping others\n'))
question3 = int(input('Whats your ideal date?\n 1)A cute craft night\n 2) A fun outdoor activity! \n 3)Quiet and calm evening at home...alone\n 4) Surprise me, just dont be boring\n'))
question4 = int(input('What’s most important to you?\n 1) Being the smartest in the room\n 2) Being a good leader\n 3)Time to myself \n 4) Freedom'))
question5 = int(input('Which best describes your attitude toward power?\n 1) Knowledge is power\n 2) No guts, no glory \n 3) I dont care for power\n 4) Being able to change and adapt\n'))


if question1 == 1:
  Wizard +=1
  Swordsman +=1
elif question1 == 2:
  Fighter +=1
  Swordsman +=1
elif question1 == 3:
  Dark_Mage +=1
elif question1 == 4:
  Shapeshifter +=1
else:
  print('wrong input')

if question2 == 1:
  Wizard +=1
  Dark_Mage +=1
elif question2 == 2:
  Fighter +=1
elif question2 == 3:
  Swordsman +=1
elif question2 == 4:
  Shapeshifter +=1
else:
  print('wrong input')

if question3 == 1:
  Wizard +=1
  Shapeshifter +=1
elif question3 == 2:
  Fighter +=1
elif question3 == 3:
  Swordsman +=1
  Dark_Mage +=1
elif question3 == 4:
  Shapeshifter +=1
  Fighter +=1
else:
  print('wrong input')


if question4 == 1:
  Wizard +=1
elif question4 == 2:
  Fighter +=1
  Swordsman +=1
elif question4 == 3:
  Dark_Mage +=1
elif question4 == 4:
  Shapeshifter +=1
else:
  print('wrong input')


if question5 == 1:
  Wizard +=1
  Swordsman +=1
elif question5 == 2:
  Fighter +=1
elif question5 == 3:
  Dark_Mage +=1
elif question5 == 4:
  Shapeshifter +=1
  Fighter +=1
else:
  print('wrong input')

classes = {
  'Wizard':Wizard,
'Swordsman':Swordsman,
'Fighter': Fighter,
'Shapeshifter':Shapeshifter,
'Dark_Mage':Dark_Mage
}
your_class = max(classes, key=classes.get)

print(f'Congradulations! You are a: {your_class}')

