#this code allows users input information and gets a predictive response on their covid19 status. 
Full_name = input('what is your name: ')
resident = input('where are you from: ')
marital_status = input('what is you marital status: ')
activity = input('were you at a social gathering recently: ')
contact = input('were you in contact with a recently infected person in the gathering: ')
feel = input('how are you feeling: ')
#covid19 symptoms
symptoms = ['fever', 'coughing', 'tiredness', 'loss of smell']
print(' ')

print('Hi, My name is Harrison. i am here to help you. Please fill the details below.')
print(' ')
print(f'Name - {Full_name}\nResident - {resident}\nMarital Status - {marital_status}\nAttended social activity in the last few weeks - {activity}\nPhysical contact with a suspected person - {contact}')
print(' ')
#if functions: if user inputs an item in the symptoms(list)
if feel in symptoms:
    print(f'Hello {Full_name}, please see a doctor')
else:
    print(f'Hi {Full_name}\nplease, Keep staying safe. Always wash your hands thoroughly and wear a nose mask.')
print(" ")
print(f'Cheers,\nDr. Harrison')