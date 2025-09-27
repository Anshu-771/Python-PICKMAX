# Practice 1

#Q3
# Write a Python program to convert text to speech using pyttsx3 library.
import pyttsx3

ruju = pyttsx3.init()

ruju.say('''
hello Everyone,
welcome to python programming.
It is me Python Pick(by Anshu)...
''')

ruju.runAndWait()

#for more details visit https://pypi.org/project/pyttsx3/