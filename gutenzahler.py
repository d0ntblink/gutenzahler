#!/usr/bin/python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plotter
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from sys import argv

# constants

# variables
fetch_mode = False
read_mode = False
pie_graph = False
bar_graph = False
total_num_letters = 0
# alphabet dictionary
abcd = "abcdefghijklmnopqrstuvwxyz"
alphabet_dict = {}
for letter in abcd:
    alphabet_dict[letter.upper()] = 0
    
def print_help():
    print(
'''
\n\ngutenzahler is a python program for analyzing english alphabet frequency in a text.

Usage:
to read and analyze a local file:
    gutenzahler.py --read <file format> <file target location>
to read and analyze a book on Gutenberg Corpus:
    gutenzahler.py --fetch <bookid on gutenberg>

NOTE: I highley recommend using the fetch mode as the program will clean up the 
text and generate a more accurate resaults    

Arguments:
    --help: displays this message
    --read: reads local files
    --fetch: reads titles available on Gutenberg.org
    --pie:  generates a pi graph of the alphabet letters
    --bar: generates a bar graph of the alphabet letters
Accepted file formats:
    txt
    html (WIP)
    epub (WIP)
    
Example:
    gutenzahler.py --fetch 10010 --bar
    gutenzahler.py --read txt "/home/user/Hansel and Gretel.txt" --pie --bar
    gutenzagler.py --read txt $PWD/lol.txt
''')

while True:
    try:
        for argum in argv:
            if argum == "--help":
                print_help()
                break
            elif argum == "--fetch":
                fetch_mode = True
                bookid_to_fetch = argv[argv.index("--fetch")+1]
            elif argum == "--read":
                read_mode = True
                file_format = argv[argv.index("--read")+1]
                file_to_read = argv[argv.index("--read")+2]
            elif argum == "--bar":
                bar_graph = True
            elif argum == "--pie":
                pie_graph = True
    except:
        print('invalid arguments!!')
        print_help()
        break

    if read_mode and fetch_mode:
        print('You cant use --read and --fetch at the same time.')
        print_help()
        break
    if read_mode == False and fetch_mode == False:
        print('invalid arguments!!')
        print_help()
        break

    if fetch_mode:
        file_text = strip_headers(load_etext(int(bookid_to_fetch))).strip() 
    elif read_mode:
        if file_format == "txt":
            file = open(file_to_read, "r")
            file_text = file.read()
        else:
            print("Currenty only plain text files are supported.")
            break

    for letter in file_text:
        if letter.upper() in alphabet_dict:
            alphabet_dict[letter.upper()] += 1
            total_num_letters += 1

    for letter, count in alphabet_dict.items():
        print("%2.4f%% of the letter are the letter %s" % (((count/total_num_letters)*100), letter))

    if bar_graph:
        plotter.bar(alphabet_dict.keys(), height=alphabet_dict.values())
        plotter.show()
    if pie_graph:
        plotter.pie(alphabet_dict.values(), labels=alphabet_dict.keys())
        plotter.show()

    break