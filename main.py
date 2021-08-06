# This is a simple version of a program to spy your salary from work.
# Hope you will like it and use it.
# Try to focus on your hour work day.
# Calculate your payouts by attaching price / hour and taxes.
from json import load, dump
from datetime import datetime


person = []
first_name, last_name = input("What's your full name? ").split(' ')
file_name = first_name + last_name + '.json'

while True:
    choice = input('Chouse your way.\n [R]ead data or [W]rite new data... ').lower()
    # For now only check if there are any data
    if choice == 'r':
        try:
            with open(file_name) as data:
                person = load(data)
                print(f'{first_name} {last_name} worked:')
                for hours in person:
                    print(f'{hours}')
        except FileNotFoundError:
            print('None file found....')
            print('-' * 48)

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
        total = work_days * p_hour + extra_time * price_extra
        # Create space (list) for data that user will fill, and then add it to new file
        day_log = {
            'start': start,
            'end': end,
            'days': work_days,
            'hours': time_work,
            'rate': p_hour,
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

        with open(file_name, 'w') as data:
            person = load(data)
            person.append(day_log)
            dump(person,data)


    elif choice in ['q', 'quit', 'exit', 'e']:
        print('Goodbye.')
        break
    else:
        print("Don't know how to read this.\nPlease try again.")
