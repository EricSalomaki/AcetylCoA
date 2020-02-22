#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 10:50:42 2018

@author: ericsalomaki
"""

with open ("/Users/ericsalomaki/Desktop/AcetylCoA_Evolution/Pfam/Rename_Fastas.txt", "r") as annotation:
    anotation_dict = {}
    for line in annotation:
        line = line.split("\t")
        if line: #test whether it is an empty line
            anotation_dict[line[0]]=line[1:]
        else:
            continue

# really should not parse the fasta file by myself. there are
# many parsers already there. you can use module from Biopython
ofile = open ("/Users/ericsalomaki/Desktop/AcetylCoA_Evolution/Pfam/PF13380_CoA_binding/PF13380_CoA_binding_ncbi.target.newheaders.faa", "w")

with open ("/Users/ericsalomaki/Desktop/AcetylCoA_Evolution/Pfam/PF13380_CoA_binding/PF13380_CoA_binding_ncbi.target.faa", "r") as myfasta:
    for line in myfasta:
        if line.startswith (">"):
            line = line[1:] # skip the ">" character
            line = line.split()
            if line[0] in anotation_dict:
                new_line = ">" + "".join(anotation_dict[line[0]])
                ofile.write ( new_line )
            else:
                ofile.write ( ">"+ "".join(line) )
        else:
            ofile.write(line)


ofile.close() # always remember to close the file.

