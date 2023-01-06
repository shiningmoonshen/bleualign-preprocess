# -*- coding: utf-8 -*-
import re
import sys

def main():
    #opens source file and rewrites file with each sentence having a new line
    punctuation = re.compile(r"([^\d+])(\.|\!|\?|;|。\n|\n|。|\！|\？|；|…)+")
    lines = []

    with open(sys.argv[1],'r',encoding="utf-8") as f:
        #lines = re.sub("\n", "", f.read())
        lines = punctuation.sub(r"\1\2<pad>", f.read())
        lines = [line.strip() for line in lines.split("<pad>") if line.strip()]


    new = open(sys.argv[1][:-4] + "_output.txt", "w")
    for line in lines:
        new.write(line + "\n")
    f.close()
    new.close()
    return new

main()





