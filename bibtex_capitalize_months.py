"""
This script parses the bibtex file aspecified by sys.argv[1] and removes the curly braces from month entries.
It is meant to fix the bibtex files produced by Mendeley reference manager.

Created on 3 August 2016
@author: Jure Sokolic
"""
import os
import re
import sys


def parse_bibtex(file_string, file_out_suffix='_correct'):
    """The function parses the .bib file and removes curly braces from the month entries.

    :Example:

    month={jan}

    is be replaced by

    month=jan.

    :param file_string: String specifying the original bibtex file.
    :param file_out_suffix: Suffix added to the name of the original bibtex file to generate the name of the updated file.
    :return: This function has no return statement.
    """
    file_name, file_extension = os.path.splitext(file_string)
    assert file_extension == ".bib", \
        "Expected file extension is .bib. Supplied file has the extension: " + file_extension
    print "Parsing file: " + file_string

    file_out_string = file_name + file_out_suffix + file_extension

    fin = open(file_string, 'r')
    fout = open(file_out_string, 'w')

    for line in fin:
        if line[0:5] == 'month':
            line_fixed = re.sub('{', '', line)
            line_fixed = re.sub('}', '', line_fixed)
            fout.write(line_fixed)
            # debug
            # print line
            # print line_fixed
        else:
            fout.write(line)

    fin.close()
    fout.close()
    print "Updated files at: " + file_out_string


if __name__ == '__main__':
    bibtex_file = sys.argv[1]
    parse_bibtex(bibtex_file)
