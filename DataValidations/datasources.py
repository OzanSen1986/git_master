import json

json_str = '{"name": "Alice", "middle_name": null, "age": 35, "profession":"Manager"}'

try:
    data = json.loads(json_str)
    if data['age'] <= 35:
        print('Age limit is not allowed to view the content.')
    else:
        print('Data Valid')
except (SyntaxError, ValueError, ZeroDivisionError, KeyError) as e:
    print(f'No data exists to be shown on the web!')
    print(f'Error Code: {e}')

print(type(data))
print(f'json_str has age: {data["age"]}')


