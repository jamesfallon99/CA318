#def sol(words):
    #for word in words:
        #if len(word) <= 3:
            #words.remove(word)
    #return words

#print(sol(["jam", "james", "bob", "harry"]))

#https://stackoverflow.com/questions/4406389/if-else-in-a-list-comprehension
#[ expression for item in list if conditional ]
#for item in list:
    #if conditional:
        #expression

#def sol(words):
    #[words.remove(word) for word in words if len(word) <= 3 ]
    #return words

def sol(words):
    return [word for word in words if len(word) > 3]

print(sol(["jam", "james", "bob", "harry"]))

