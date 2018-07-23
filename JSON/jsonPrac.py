import json

'''
json.load(f): Load JSON data from file 
json.loads(s): Load JSON data from a string usually from a server
json.dump(j, f): Write JSON object to a file 
json.dumps(j): Output json object as string
'''

# json.load(f) example and convert the json into a dictionary
with open('movie_1.json','r') as json_file:
    movie = json.load(json_file)

print(movie)

# json.loads(s) use it if json data arrives in the form of a string common in client server applications
value = """
    {
        "title": "Tron Legacy",
        "composer": "Daft Punk",
        "release year": 2010,
        "budget": 17000000,
        "actors": null,
        "won_oscar": false
    }"""

tron = json.loads(value)
print("\n")
print(tron)

# json.dumps() used to convert a dictionary to a valid JSON string 
print()
dump = json.dumps(movie)
print(dump)

# json.dump() create a new object convert to json and write to a file
movie2 = {
    "title":"Minority report",
    "director": "Steven Spielberg",
    "composer": "John Williams",
    "actors" : ["Tom Cruise", "Colin Farell"],
    "is_awesome" : True,
    "budget": 102000000,
    "cinematographer" : "Janusz Kami\u0144ski"
    }


with open("movie_2.json",'w', encoding = "utf-8") as mov:
    json.dump(movie2, mov, ensure_ascii= False)