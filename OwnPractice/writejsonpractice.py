import json

person = {}

person['Family'] = {

    'Coyle': [{

        'firstname': 'Pat',
        'job': 'Manager'
        },

        {
        'firstname': 'Mitty',
        'job': 'Handyman'
        }],

    'Fellman': [{

        'firstname': 'Russ',
        'job': 'Handyman'
        },

        {
        'firstname': 'Karen',
        'job': 'Cleaner'
        }]
    }

with open('data.txt', 'w') as outfile:
    json.dump(person, outfile)
