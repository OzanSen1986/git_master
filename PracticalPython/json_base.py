# JSON = JavaScript Object Notation

import json

json_string = '''
    {
        "students": [
            {
               "id": 1,
               "name": "Tim",
               "age": 21,
               "full-time": true     
            },
            {
               "id": 2,
               "name": "Joe",
               "age": 33,
               "full-time": false     
            },
            {
               "id": 3,
               "name": "William",
               "age": 45,
               "full-time": true     
            },
            {
               "id": 4,
               "name": "Daniel",
               "age": 23,
               "full-time": false     
            }
        ]
    }
'''

data = json.loads(json_string)

print(data['students'][3])

    
        






