import sys
from stats import count_words 
from stats import count_letters
from stats import dict_sort

if (len(sys.argv) < 2) : 
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else :
    file_path = sys.argv[1]

def get_book_text (file_path) :
    with open (file_path) as f : 
        ch = f.read() 
        return ch

ch = get_book_text(file_path)

w = count_words(ch)
## L = count_letters(ch)
D = dict_sort(ch)
ch2 = """"""
for i in range (len(D)) : 
    ch2 = ch2 + str(D[i][0]) + ":" + " " + str(D[i][1]) + "\n" 


ch3 = f"""

============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}
----------- Word Count ----------
Found {w} total words
--------- Character Count -------
{ch2}
============= END ===============
"""

print(ch3)
