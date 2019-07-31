def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
        
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    for c in str1:
        if c in str2:
            str2 = str2.replace(c, "")
    return len(str2) ==0

print(is_permutation('ahjk', 'hajk'))

def string_reverser(our_string): # another way is in stack.py
    reversed_string = ""
    for letter in our_string:
        reversed_string = letter + reversed_string # If do += letter then it won't be reversed
    return reversed_string
    
print string_reverser("hello nancy")

def anagram_checker(str1, str2):
    if len(str1) != len(str2):
        # Clean strings
        str1 = str1.replace(" ", "").lower()
        str2 = str2.replace(" ", "").lower()
        
    if sorted(str1) == sorted(str2):
            return True
    return False

print anagram_checker('dff', 'f df')

    
def word_flipper(our_string):
    #First split the sentence by space
    our_array = our_string.split( )
    final_array = []
    for word in our_array:
        reversed_word = ""
        for letter in word:
            reversed_word= letter + reversed_word
        final_array.append(reversed_word)
    return ' '.join(final_array)
    
print word_flipper('This is a String')
    
def word_flipper2(our_string):
    word_list = our_string.split(" ")
    print "nancy"[::-1]
    for idx in range(len(word_list)):
        word_list[idx] = word_list[idx][::-1]

    return " ".join(word_list)
    
print word_flipper2('This is a String')

