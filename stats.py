def count_words(ch) : 
    N_W = len(ch.split())
    return N_W 

def count_letters (ch) : 
    dict2 = {}
    ch = ch.lower()
    nr = 0
    ch2 = ''
    ch2 = ch2 + ch[0]
    for i in range (len(ch)) : 
        for j in range (len(ch2)) : 
            if ch[i] == ch2[j] : 
                nr = nr + 1
        if nr == 0 : 
            ch2 = ch2 + ch[i] 
            nr = 0 
        else : 
            nr = 0 
    for i in range (len(ch2)) : 
        n = 0 
        for j in range(len(ch)) : 
            if ch[j] == ch2[i] : 
                n = n + 1
        dict2[f'{ch2[i]}'] = n
        n = 0 

   ## return dict2




def dict_sort (ch) : 
    dict2 = {}
    dict3 = {}
    ch = ch.lower()
    nr = 0
    ch2 = ''
    ch2 = ch2 + ch[0]
    for i in range (len(ch)) : 
        for j in range (len(ch2)) : 
            if ch[i] == ch2[j] : 
                nr = nr + 1
        if nr == 0 : 
            ch2 = ch2 + ch[i] 
            nr = 0 
        else : 
            nr = 0 
    for i in range (len(ch2)) : 
        n = 0 
        for j in range(len(ch)) : 
            if ch[j] == ch2[i] : 
                n = n + 1
        dict2[f'{ch2[i]}'] = n
        n = 0 

    for i in range (len(ch2)) : 
        if ch2[i].isalpha() : 
            dict3[f'{ch2[i]}'] = dict2[f'{ch2[i]}'] 
    
    dict3 = sorted(dict3.items(), key=lambda item: item[1], reverse = True)
    
    return dict3

