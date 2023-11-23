# RegEx (Regular Expression) is a sequence of characters that forms a search pattern
#                            can be used to check if a string contains the specified search pattern

import re

msg = "The rain is Spain"
print("Message:",msg)
print()

# searching the string to see if starts with "The" and ends with "Spain":
print("Searching specific patterns:")
x = re.search("^The.*Spain$", msg)
print(x)

if x:
    print("We Have A Match!")
else:
    print("We Do Not Have A Match!")


'''
RegEx Functions:
Function	Description
findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string


Metacharacters: characters with special meaning
Character	        Description	                                                                Example	
[]	                A set of characters	                                                        "[a-m]"	
\		            Signals a special sequence (can also be used to escape special characters)	"\d"
.		            Any character (except newline character)	                                "he..o"	
^		            Starts with	                                                                "^hello"	
$		            Ends with	                                                                "planet$"	
*		            Zero or more occurrences	                                                "he.*o"	
+		            One or more occurrences	                                                    "he.+o"	
?		            Zero or one occurrences	                                                    "he.?o"	
{}		            Exactly the specified number of occurrences	                                "he.{2}o"	
|		            Either or	                                                                "falls|stays"
()	                Capture and group


Special Sequences: is a \ followed by one of the characters in the list below, and has a special meaning:
Character	Description	                                                                        Example	
\A	        Returns a match if the specified characters are at the beginning of the string	    "\AThe"	
\\b	        Returns a match where the specified characters are at the beginning or at the end 
            of a word(the "r" in the beginning is making sure that the string is being treated 
            as a "raw string")	                                                                r"\\bain"
                                                                                                r"ain\\b"	
                                                                                                
\B	        Returns a match where the specified characters are present, but NOT at the 
            beginning (or at the end) of a word (the "r" in the beginning is making sure 
            that the string is being treated as a "raw string")	                                r"\Bain"
                                                                                                r"ain\B"	
\d	        Returns a match where the string contains digits (numbers from 0-9)	                "\d"	
\D	        Returns a match where the string DOES NOT contain digits	                        "\D"	
\s	        Returns a match where the string contains a white space character	                "\s"	
\S	        Returns a match where the string DOES NOT contain a white space character	        "\S"	
\w	        Returns a match where the string contains any word characters (characters from 
            a to Z, digits from 0-9, and the underscore _ character)	                        "\w"	
\W	        Returns a match where the string DOES NOT contain any word characters	            "\W"	
\Z	        Returns a match if the specified characters are at the end of the string	        "Spain\Z


Sets:  is a set of characters inside a pair of square brackets [] with a special meaning:
Set	        Description	
[arn]	    Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	    Returns a match for any lower case character, alphabetically between a and n	
[^arn]	    Returns a match for any character EXCEPT a, r, and n	
[0123]	    Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	    Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	        In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
'''

# Findall() Function: returns a list containing all matches
print("\nfindall():")
x = re.findall("ai", msg)
print(x)

print("\nIf no matches are found:")
print(re.findall("Portugal", msg))


# Search() Function: searches the string for a match, and returns a Match Object
print("\nsearch():")
x = re.search("\s", msg)

print("The first white-space character is located in position:", x.start())

# Split() Function: returns a list where the string has been split at each match
print("\nsplit():")
x = re.split("\s", msg)
print(x)

# maxsplit lets you control the number of occurrences/splits:
print("maxsplit of 1:")
print(re.split("\s", msg, 1))

# Sub() Function: replaces the matches with the text of your choice:
print("\nsub():")
print("Replaces all whitespace with: '9'")
print(re.sub("\s","9", msg))

# count lets you control the number of replacements:
print("count of 2:")
print(re.sub("\s","9", msg, 2))

# Match Object: is an object containing information about the search and teh result
print("\nMatch Object:")
print(re.search("ai", msg))

'''
.span()  returns a tuple containing the start-, and end positions of the match.
.string  returns the string passed into the function
.group() returns the part of the string where there was a match
'''
print('\n.span: returns a tuple containing the start-, and the end positions of the match')
x = (re.search(r"\bS\w+", msg))
print(x.span())

print('\n.string: returns the string passed into the function')
print(x.string)

print('\n.group: returns the part of the string where there was a match')
print(x.group())