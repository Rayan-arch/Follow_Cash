# This is a simple version of a program to spy your salary from work.
# Hope you will like it and use it.
# Try to focus on your hour work day.
# Calculate your payouts by attaching price / hour and taxes.
from json import load, dump
from datetime import datetime, date
from time import sleep
from sys import exit


people = []
try:
    with open('data.json') as file:
        people = load(file)
except FileNotFoundError:
    print('None file found....')
    print('Run setup.py file')
    print('-' * 48)
    sleep(5)
    exit()


first_name, last_name = input("What's your full name? ").split(' ')
new = int(input('Are you new? [1]yes/[0]no'))

while True:
    choice = input('Chouse your way.\n [R]ead data or [W]rite new data... ').lower()
    if choice in ['q', 'quit', 'exit', 'e']:
        print('Goodbye.')
        break

    # For now only check if there are any data
    if choice == 'r':
        print(f'{first_name} {last_name} worked:')
        for person in people:
            if first_name.lower() == person['first_name'].lower() and last_name.lower() == person['last_name'].lower():
                for items in person['hours']:
                    print(items)
            else:
                print("It's your first time.")
    # If you want do add new data, do all steps
    elif choice == 'w':
        p_hour = float(input('How much do you get per hour? '))
        start = input('Input day start work [dd-mm-yyyy]: ')
        end = input('Input day end work [dd-mm-yyyy]: ')
        start = datetime.strptime(start, '%d-%m-%Y')
        end = datetime.strptime(end, '%d-%m-%Y')
        work_days = end - start
        work_days = work_days.days
        time_work = float(input('How long did you work [h/day]? '))

        # Check if you have any extra hours for you
        if time_work > 8:
            extra_time = input('Was in thouse hours an extra pay hours?[y/n] ').lower()
            if extra_time == 'y':
                price_extra = float(input('How much extra[%] do you get for those hours? '))
            else:
                price_extra = p_hour

            extra_time = time_work - 8
        else:
            extra_time = 0
            price_extra = 0
        time_work = time_work - extra_time
        total = (work_days +1)* time_work * p_hour + extra_time * price_extra

        # Create space (list) for data that user will fill, and then add it to new file
        day_log = {
            'added': str(date.today()),
            'start': str(start)[:11],
            'end': str(end)[:11],
            'days': work_days,
            'hours': time_work,
            'extra_time': extra_time,
            'extra_price': price_extra,
            'total': total
        }

        # TODO:
        #     - finish counting his extra salary, <
        #     - if they dont pay him for those extra hours, <
        #     - save every thing to json file using list day_log, <
        #     - formating for thode data (who,work where?, price for a day, day he start, day he ended, total days, total price(including extra pay)), <
        #     - sort every thing to a functions,
        #     - create new files for that,
        #     - create testing cases,
        #     - remember to use sebuging in pycharm

        if new:
            with open('data.json', 'w') as file:
                people.append(
                    {
                        'id': len(people),
                        'first_name': first_name,
                        'last_name': last_name,
                        'rate': p_hour,
                        'hours': day_log
                    }
                )
                dump(people, file)
        else:
            for index, person in enumerate(people):
                if person['first_name'].lower() == first_name.lower() and person['last_name'].lower() == last_name.lower():
                    with open('data.json', 'w') as file:
                        people[index]['hours'].append(day_log)
                        dump(people, file)
        print('Done.')
        print('-'*48)
    else:
        print("Don't know how to read this.\nPlease try again.")

