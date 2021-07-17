def split_words(stuff):
    """#print("This function will split the words for us")"""
    words = stuff.split(' ')
    return words
    
def sort_words(words):
   # print("this function will sort words for us")
    return sorted(words)
    
def first_words(words):
  #  print("This function will pop up first word")
    word = words.pop(0)
    print(word)
    
def sort_sentance(sentance):
    words = split_words(sentance)
    return sort_words(words)
    
def last_word(word):
 #   //this function will pop up last word 
    words = word.pop(-1)
    print(words)
    
def print_firtst_last(sentance):
#    this funtion print 
    word = split_words(sentance)
    first_words(word)
    last_word(word)
def print_first_last_sorted(sentance):
    word = sort_sentance(sentance)
    first_words(word)
    last_word(word)
    #this function print first and last sorted words