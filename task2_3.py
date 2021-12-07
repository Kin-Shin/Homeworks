def personal_data(name, surname, birthday, city, email, phone):
    return f'{name} {surname} {birthday} {city} {email} {phone}'


name = input('Enter your name ')
surname = input('Enter your surname ')
birthday = input('Enter your birthday ')
city = input('Enter your city ')
email = input('Enter your email ')
phone = input('Enter your phone number ')

print(personal_data(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone))
