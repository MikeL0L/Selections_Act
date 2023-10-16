
year = int(input('Enter year: '))
zodiac = (year - 1000) % 12
if zodiac == 0:
    print(year, 'is the year of the Rat')
elif zodiac == 1:
    print(year, 'is the year of the Ox')
elif zodiac == 2:
    print(year, 'is the year of the Tiger')
elif zodiac == 3:
    print(year, 'is the year of the Rabbit')
elif zodiac == 4:
    print(year, 'is the year of the Dragon')
elif zodiac == 5:
    print(year, 'is the year of the Snake')
elif zodiac == 6:
    print(year, 'is the year of the Horse')
elif zodiac == 7:
    print(year, 'is the year of the Sheep')
elif zodiac == 8:
    print(year, 'is the year of the Monkey')
elif zodiac == 9:
    print(year, 'is the year of the Rooster')
elif zodiac == 10:
    print(year, 'is the year of the Dog')
elif zodiac == 11:
    print(year, 'is the year of the Pig')
else:
    print('Invalid Year')