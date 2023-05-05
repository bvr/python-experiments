# from https://www.pythonforbeginners.com/basics/working-with-toml-files-in-python

import toml

data = {
    "employee": {
        "name": "John Doe",
        "age": 35
    },
    "job": {
        "title": "Software Engineer",
        "department": "IT",
        "years_of_experience": 10
    },
    "address": {
        "street": "123 Main St.",
        "city": "San Francisco",
        "state": "CA",
        "zip": 94102
    }
}

with open("employee.toml","w") as file:
    toml.dump(data,file)
