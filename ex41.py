import random
import urllib.request 
import sys


WORD_URL = 'http://learncodethehardway.org/words.txt'
WORDS = []
 
 

PHRASES = {
        "class %%%(%%%)": "Make a class %%% that-is %%%.",
        "class %%%(object):\n\t def __init__(self,***)": "class %%% has __init__ that takes self and *** as parameters.",
        "class %%%(object):\n\t def ***(self,@@@):": "A class %%% has a function name *** and takes self and @@@ as argument.",
        "*** = %%%()" : "Set *** to an instance of a class %%%",
        "***.***(@@@)": "From *** call the function *** with the self and @@@ as parameters.",
        "***.*** = '***'": "from *** get the attribute *** and set it to '***'"
        }
#do they want to drill phrase first

PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == 'english':
    PHRASE_FIRST = True
    
# load up the word from the website

for word in urllib.request.urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())
    
    
def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))] 
                   
    other_names = random.sample(WORDS, snippet.count("***"))
    
    results = []
    param_names = []
    
    for i in  range(0,snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample.decode("ascii")(WORDS, param_count)))
        
    for sentence in snippet, phrase:
        result = sentence[:]
        
        #fake class name
        for word in class_names:
            result = result.replace("%%%",str(word),1)
        #facke other name
        
        for word in other_names:
            result = result.replace("***",str(word),1)
            
        #fake parameter list
        
        for word in param_names:
            result = result.replace("@@@",str(word),1)
            
        results.append(result)
    
    
    return results
    
    
try:
    while True:
        
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)
        
        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet,phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
            print(question)
            
            input("> ")
            print("Answer: %s\n\n"%answer)
            
            
except EOFError:
    print("\nBYE.....")
            