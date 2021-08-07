from json import load, dump

with open('data.json','w') as file:
    people = [{
                        'id': 1,
                        'first_name': 'Jan',
                        'last_name': 'Kowalski',
                        'rate': 1,
                        'brutto': 1,
                        'netto': 1,
                        'hours': [{
     "start": "01-01-2021",
     "end": "02-01-2021",
     "days": 1,
     "hours": 1,
     "extra_time": 0,
     "extra_price": 0,
     "total": 1
  }]
                    }]
    dump(people, file)