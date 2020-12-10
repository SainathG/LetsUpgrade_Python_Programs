x = ('key1', 'key2', 'key3')
y = 2
dict1 = dict.fromkeys(x, y)  # The  method returns a dictionary with the specified keys and the specified value
print(dict1)

z=('1','2','3','4')
dict2=dict.fromkeys(x,z)
print(dict2)

m = {
  "Key1": "Python",
  "Key2": "Java",
  "Key3": "Ruby"
}

print(m.get("Key1"))       # Gets value for the particular key

m.update({"Key2": "C++"})  # Updates the particular key related value
print(m)

m.pop("Key1")              # Removes the particular key along with value.
print(m)

print(m.keys())            # Get the keys information

n = m.copy()               # Copies the dictionary
print(n)

m.clear()                  # Clear the dictionary
print(m)
