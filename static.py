name: str = "Talha"; # make it static string type
# name: str = 45; # gives error

print(type(name)) #class;
print(id(name)) # address;
# print(dir(name)) # gives all available methods


# multi-line string
# 1. back-slash at the end of line
multi = 'Talha'\
        ' '\
        'Bhai'
print(multi)
# 2. Quotation marks (Single)
multi = '''Pyton
is
good'''
print(multi)

multi = """ Javascript
is also
good
"""
print(multi)

# boolean
boolean : bool = True;

print(type(boolean));
print(id(boolean));
# print(dir(boolean))


# List
mylist : list[str] = ['a','b','c'];
print(mylist);
print(type(mylist));
print(id(mylist));


# Tuple
mytuple: tuple[str,str,str] = ('a','b','c');
print(mytuple);
print(type(mytuple));


# Dictionary
mydictionary: dict[str,str] = {
    "name": "Tala",
    "age" : "23"
};

print(mydictionary);
print(type(mydictionary));