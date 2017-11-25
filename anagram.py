#!/bin/python
# -*- coding: UTF-8 -*-

import string
import optparse
import sys

def print_anagrams(anagram_file):
    """Print all permutations of anagrams from a file with one word on each line."""

    # Use has as anagram holder
    anagrams={}

    for line in anagram_file:
        # Get rid of withe spaces (carrage return and line shift)
        word = line.strip()

        # Make list out of the word to sort the letters
        word_list = list(word)
        word_list.sort()

        # Key is a sorted word
        key = string.join(word_list, "")
        
        # If key isn't in list, add placeholder
        if not anagrams.has_key(key):
            anagrams[key] = [] 
        
        # Add word to list
        anagrams[key].append(word)

    # Go through all elemnts in list
    for anagram in anagrams:
        anagram_list = anagrams[anagram]

        # If there is more than one word in list, it is an anagram
        if len(anagram_list) > 1:

            # Go through all permutations, unsorted
            for word in anagram_list:

                # Print all permutations                
                print word + " -> " + string.join([ a for a in anagram_list if word is not a ], ", ")

if __name__ == "__main__":
    usage = """%prog [-h] FILE"""
    description = """Print all permutations of anagrams in FILE."""
    version= '%prog 0.1'

    p = optparse.OptionParser(usage=usage, version=version, description=description)
    o, args = p.parse_args()

    if len(args) > 0:
        try:
            # Try to open the file read only
            anagram_file = file(args[0], mode="r")
        except:
            # Return error and exit with code 1
            print >> sys.stderr, "Error: '" + args[0] + "' don't exists\n"
            sys.exit(1)

        # Print anagrams
        print_anagrams(anagram_file)
    else:
        p.print_usage()

    # Return no problems
    sys.exit(0)