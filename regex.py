import regex

#grep word_to_search filepath
# grep -i word_to_search filepath    //no case match
# grep l.rts filepath     //  '.' is  a wild card
# grep ^thon  filepath      //   all word that ends with thon
# grep cat$ filepath      // all words ending with cat



import re
search="hello ia m    ashar"
#print(re.search("as",search))    #<re.Match object; span=(14, 16), match='as'>
#print(re.search("^haaa",search))
#print(re.search("ha$",search))
#print(re.search("e..o",search))    #<re.Match object; span=(1, 5), match='ello'>
#print(re.search(r"[a-z]llo","hello"))    # wild card  [a-z][A-Z][0-9]



print(re.search(r"Py.*n","Python programmin"))
# import re
# def check_punctuation (text):
#   result = re.search(r"[^a-zA-Z0-9 ]", text)
#   return result != None

# print(check_punctuation("This is a sentence that ends with a period.")) # True
# print(check_punctuation("This is a sentence fragment without a period")) # False
# print(check_punctuation("Aren't regular expressions awesome?")) # True
# print(check_punctuation("Wow! We're really picking up some steam now!")) # True
# print(check_punctuation("End of the line")) # False

