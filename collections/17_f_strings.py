'''
f-string newly introduced and it available from version 3.6 onwards.
It used for string formatting.
The old way to format a string is this.
'''

Name = "Ajju"
Villege = "Manjari"
Intro = "Hey I'm {} and I'm from {}."
print(Intro.format(Name, Villege))

print("-----------------------------------------------------------------------------")

'''
When we prefix the string with the letter 'f', the string become the f-string itself.
The f-string can be formatted in much same as the str.format() method.  
'''

Info = (f"Hey I'm {Name} and I'm from {Villege}.")
print(Info)
