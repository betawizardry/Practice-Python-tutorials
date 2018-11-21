#reverse string word order
#identify spaces,log where they occur in the string
#and then print words between them in reverse order

def reverse_words_order(userstring):
    """reverses the order of words in a string but the words themselves remain
in the correct order"""
    userstring += ' '
    count = 0
    wordlist = []
    for x in range(0,len(userstring)):
        if ord(userstring[x]) == 32:
            wordlist.append(userstring[count:x])
            count = x+1
    wordlist = wordlist[::-1]
    rev_userstr = ''
    for a in range(0,len(wordlist)):
        rev_userstr += ' '
        rev_userstr += wordlist[a]
    #print(rev_userstr[1:]) #for testing
    return rev_userstr[1:]

#reverse_words_order('this sentence is a palindrome a is sentence this') #for testing
