import json


#Simple JSON Data
data = ''' {
    "name" : "ABCD",
    "phone" : {
        "type" : "intl",
        "number" : "12345"
    },
    "email" : {
        "hide" : "yes"
    }
}
'''

info = json.loads(data)
print("Name:", info['name'])
print("Phone Number:", info['phone']['number'])
print("Email Attribute:", info['email']['hide'])

#Nested JSON Data

studentdetails = ''' [
   { 
    "id" : "1234",
    "number" : "2",
    "name" : "ABCD"
   },
   { 
    "id" : "1200",
    "number" : "5",
    "name" : "MNOP"
   } 
]
'''

studentslist = json.loads(studentdetails)
print('Student Coun:', len(studentslist))

for student in studentslist :
    print("Student ID:", student["id"])
    print("Student Serial Number:", student["number"])
    print("Student Name:", student["name"])


data = ''' {
    "users": [
        {
            "status": {
                "text": "@jazzychad I just bought one .__."
            },
             "location": "San Francisco, California",
             "screen_name": "leahculver",
             "name": "Leah Culver"
}   ]   }
'''

x = json.loads(data)
print('Data:', x['users'][0]['name'])