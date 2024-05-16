punctuation = "!()-[]{}:;'''""\,<>./?@#$^&*_''.'"

my_str= "Enter a string )((#((#hh))#("

no_punc = "Hello"
for char in my_str:
    if char not in punctuation:
        no_punc=no_punc+char


print(no_punc)