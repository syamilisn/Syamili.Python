# -*- coding: utf-8 -*-
"""
Created on Sun May  3 15:47:22 2020

@author: shyam
"""
#Theme: Black Clover
#STRING MANIPULATIONS
#BOOLEAN VALUES

"""
1)STRING CONCATINATION/ADDITION

, appends spaces [exception: Can't be used in input statements]
+ gives no spaces
print("Hello",name,"-san ")----->Hello name -san
print("Hello"+name+"-san ")----->Helloname-san

2)BOOLEAN VALUES
Mind the difference----
if("True") returns true         String value
if("False") returns true        String value
if(True) returns true           Boolean value
if(False) returns false         Boolean value

3)Character Sequences
\n:nextline
\": one double quote
....

4)String manipulations: more than one can be used at a time
stringname.upper(): upper case      
.lower(): lower case
.isupper():  Checks if upper, returns boolean
.islower():   checks if lower, returns boolean           
len(stringname): string length 
.index(insert_char):  returns char's index no.     
.replace("orig. string","replace string")            
"""

name=input("Enter your name: ")
print("Hello",name,"-san ")
anime="Black Clover"
#String concatenation
interested = input("Do you like watching "+anime+"? Reply if yes otherwise press 'Enter' key\n")
#Here string is returned not boolean value.
if(interested):
    print("Welcome to Black Clover Fandom!!! \n")
else:
    print("Oh! Too bad. Please enjoy watching other anime series.\n")

print(anime,"Font style:")
#temporary upper case
print(anime.upper())
print(anime.upper().isupper())
print(len(anime),'\n')
#string is character array and can be accessed using indices
for i in range(len(anime)):
    print(anime[i],anime.index(anime[i]))
