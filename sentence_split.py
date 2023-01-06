# -*- coding: utf-8 -*-
import re
import sys
alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"
digits = "([0-9])"

def main():
    #opens source file and rewrites file with each sentence having a new line
    f = open(sys.argv[1], "r")
    new = open(sys.argv[1][:-4] + "_output.txt", "w")
    sentences_as_lst = split_into_sentences(f.read())
    for line in sentences_as_lst:
        new.write(line + "\n")
    f.close()
    new.close()
    return new

def split_into_sentences(text):
    text = " " + text + "  "
    #get rid of indentation
    text = text.replace("    ", "")
    text = text.replace("\n\n", "<nline>")
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    text = re.sub(digits + "[.]" + digits,"\\1<prd>\\2",text)
    if "..." in text: text = text.replace("...","<prd><prd><prd>")
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    if "e.g." in text: text = text.replace("e.g.","e<prd>g<prd>")
    if "i.e." in text: text = text.replace("i.e.","i<prd>e<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    text = re.sub(digits + "[.]" + digits,"\\1<prd>\\2",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("．",".<stop>")
    text = text.replace("？", "?<stop>")
    text = text.replace("！", "!<stop>")
    #switch all placeholder periods back to "."
    text = text.replace("<prd>",".")
    text = text.replace("<nline>", "\n")
    text = text.replace("’ ", "’\n")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    temp = []
    for s in sentences:
        stripped = s.strip()
        if stripped != '':
            temp.append(stripped)
    sentences = temp
    return sentences


main()