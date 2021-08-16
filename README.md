# Encrypt_text
Python Script to encrypt and decrypt text, modified to work with a companion iOS [Shortcut](https://routinehub.co/shortcut/9909/) hosted on [RoutineHub](https://routinehub.co).

It's intended to be run from the command line, taking at least three arguments, every argument after the third one will be concatenated to create the text to encrypt/decrypt. 

The first three arguments are, in order: key, encrypt or decrypt instruction, text. In the case of passing more, they will be concatenated with the third one.

For example:  
`python Encrython.py arg1 arg2 arg3 ...`  
`python Encrython.py 1000 encrypt THIS TEXT WILL BE ENCRYPTED`
