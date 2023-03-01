import json

dictionary = {'contacts': []}

while True:
    response = input('(1)add contact (2)print contacts (3)exit: ')
    if response == '1':
        person_name = input('Name: ')
        person_surname = input('Surname: ')
        person_phone = input('Phone: ')
        person_email = input('Email: ')

        person_contact = {
            'name': person_name,
            'surname': person_surname,
            'phone': person_phone,
            'email': person_email
        }
        dictionary['contacts'].append(person_contact)

    elif response == '2':
        for contact in dictionary['contacts']:
            print("---CONTACT---")
            print(f"{contact['name']} {contact['surname']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")        
        
    elif response == '3':
        print('Saving data....')
        with open('contacts.json', 'w', encoding='utf-8') as file:
            json.dump(dictionary, file, indent=4)
        print('Data saved.')
        print('Bye')
        exit()
    else:
        print('Please respond with 1, 2 or 3')


        # IZVEIDOSIM KONTAKTU APLIKĀCIJU IZMANTOJOT:
# Funkcijas
# Datu struktūras (JSON)
# File I/O

contacts = []

while(True):
    response = input('N-add new, P-print, E-exit: ')
    if response == 'N':
        name = input('Enter name: ')
        surname = input('Enter surname: ')
        number = input('Enter number: ')
        email = input('Enter email: ')

        contact = {
            'name': name, 
            'surname': surname, 
            'number': number,
            'email': email
        }

        contacts.append(contact)
        print(contacts)
    elif response == 'P':
        for contact in contacts:
            print(f"{contact['name']} {contact['surname']} {contact['number']} {contact['email']}")
    elif response == 'E':
        break