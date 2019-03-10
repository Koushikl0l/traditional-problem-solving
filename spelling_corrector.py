import re

def do_mac(Word):
    check_cor_or_not=_whet_corr(Word)
    if(check_cor_or_not==False):
            word=Word
            res_list=[]
            letters    = 'abcdefghijklmnopqrstuvwxyz'
            splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
            deletes    = [L + R[1:]               for L, R in splits if R]
            transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
            replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
            inserts    = [L + c + R               for L, R in splits for c in letters]

            #i have to extend all the list in a single list
            res_list=deletes+transposes+replaces+inserts
            do_search(res_list)
    else:
        print(Word)
    
def _whet_corr(word):
    #check whether the word is correct or not
    with open('words.txt','r') as fp:
       text=fp.read()
       fp.close()   
       Word=text.split('\n')
    #check word available in our dataset or not
    if[each for each in range(len(Word)) if Word[each]==word].__len__()!=0:
        return True
    else:
        return False
    
    
def do_search(res):
    #open a dictionary and match these words
    with open('words.txt','r') as fp:
       text=fp.read()
       fp.close()   
       word=text.split('\n')
       res_list=[each for each in res for i in range(len(word)) if word[i]==each]
    print(res_list)
           

if __name__=="__main__":
    do_mac('fuke')
    
