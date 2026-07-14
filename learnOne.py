print("First test of \t learning python")

print("Your learning Path:" \
"\n\t -python basics " \
"\n\t -data engineering" \
" \n\t -Ai ")


info = "info@datawithbaraa.com"
support = "support@datawithbaraa.com"
web="www.datawithbaraa.com"

print("\n\nfor more info access:" + "\n" + info + " " + support + " " + web)



#input("How old are you ?")



number = 10
print(number.bit_length())

age = 20
height = 1.60
name = "Alexa"
student = True
ugly = None

print(age, height, name, student, ugly)
print(type(age), type(height), type(name), type(student), type(ugly))
print(len(name), len(str(student)), len(str(ugly)))




text= """
Python is loveable.
Python is easy.
many people use Python.
"""
# remember Its case sensitive language.
# i wrote p in a capital letter and the third one small letter. 
# so it was counting 2 python and not 3.
print(text.count("Python"))



price = "123,567"
print(price.replace(",", ".").replace("2", "9"))


# f-string = formatted
# instead of using too much + and stuff we can write like down:
print(f"My name is {name}, i am {age} years old ")
























