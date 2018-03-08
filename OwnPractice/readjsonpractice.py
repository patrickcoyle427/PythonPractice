import json

with open('data.txt') as infile:

    data = json.load(infile)

    print(data['Family'])

    for k, v in data['Family'].items():

        print(k, ':', v)

    for info in data['Family']['Coyle']:

        print('First Name: ', info['firstname'])
        print('Job: ', info['job'], '\n')

    for info in data['Family']:

        print(info)
        print('')

        for person in data['Family'][info]:

            print('Name: ', person['firstname'])
            print('Job: ', person['job'])

            if person == data['Family'][info][-1]:
                
                print('')
