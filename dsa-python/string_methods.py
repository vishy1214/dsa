import datetime

string1 = "HelloWorld"
string2 = "Hospital"
string3 = "wonderFul CITY"

print(string1.casefold())
print(string2.center(2,"-"))

print(string1[1:]) #elloWorld
print(string2[::-1]) # latipsoH  -- reverses the entire string

print(f'{string1 !r} is a {string3}')  #string formatting

print(f'{"~"*10} Rolling starts {"~"*10}' )   #~~~~~~~~~~ Rolling starts ~~~~~~~~~~

today = datetime.date.today().strftime("%A")
print(' hi {0}, are you available on {1}'.format('vishwa',today))
print(' hi {}, are you available on {}'.format('vishwa',today))