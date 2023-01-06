# -*- coding: utf-8 -*-
#not a working piece of code: doesn't take into account certain specific edge cases
import sys
from nltk.tokenize import sent_tokenize

def main():
    #opens source file and rewrites file with each sentence having a new line
    f = open(sys.argv[1], "r")
    new = open(sys.argv[1][:-4] + "_output.txt", "w")
    sentences_as_lst = sent_tokenize(f.read())
    print(sentences_as_lst)
    for line in sentences_as_lst:
        new.write(line + "\n")
    f.close()
    new.close()
    return new



main()