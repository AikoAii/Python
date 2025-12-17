# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

# ExampleGet your own Python Server
# You will get an error if you use double quotes inside a string that is surrounded by double quotes:

# txt = "We are the so-called "Vikings" from the north." //false
# To fix this problem, use the escape character \":

# Example
# The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."
print(txt)