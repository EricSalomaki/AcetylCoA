#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:35:44 2018

@author: ericsalomaki
"""
from operator import itemgetter
import pickle

#open file and read in the data to the file 'lines'
infile = open('/Users/ericsalomaki/Desktop/AcetylCoA_Evolution/Pfam/Pfam_Domains_With_Taxonomy.tsv')
lines = infile.readlines()
infile.close()

#create accession dictionary
acc_d = {}

for line in lines[1:]: # for every line after the first, do the following
    hits = line.strip().split('\t') #recognize tab delimitation
    hits[3] = float(hits[3]) #change from a string to a float (number with a decimal)
    hits[4] = float(hits[4]) #change from a string to a float (number with a decimal)
    hits[5] = int(hits[5]) #change from a string to a number
    hits[6] = int(hits[6]) #change from a string to a number
    hits[7] = int(hits[7]) #change from a string to a number
    try:
        acc_d[line.split()[2]].append(hits) #add the accession do accession dictionary
        acc_d[line.split()[2]] = sorted(acc_d[line.split()[2]], key=itemgetter(3)) #sort by evalue
    except KeyError:
        acc_d[line.split()[2]] = [hits]
        
#create dictionary of kept accessions and annotations
acc_d_kept = {}

for acc in acc_d: #iterate through the sorted acc_dictionary
    kept_hits = [acc_d[acc][0]] #Keep the first hit for each accession (highest evalue)
    for hit in acc_d[acc][1:]: #For each additional hit in the accession
        KEEP = True #keep that accession
        for kept in kept_hits: #for each kept accession/domain
            if (   (hit[6] < kept[5] and hit[5] < kept[5]) or (   hit[6] > kept[6] and hit[5] > kept[6]   )) and hit[4] > 1: #make sure it fits the conditions to not overlap with a domain with a higher evalue

                pass #for accessions that meet those criteria continue to keep
            else: #if they do not meet the criteria
                KEEP = False  #do not keep the domain assignment
        if KEEP == True and hit not in kept_hits: #for each domain assignment that is kept and not already in kept_hits
            kept_hits.append(hit) #add the domain to kept hits
    acc_d_kept[acc] = kept_hits #add kept_hits to the acc_d_kept dictionary

print acc_d_kept

acc_names = {} #make dictionary for all the taxonomy data associated with the domain hits

for acc in acc_d_kept: #iterate through the acc_d_kept dictionary
    acc_d_kept[acc] = sorted(acc_d_kept[acc], key=itemgetter(5)) #sort by starting location for each domain
    name = acc + '____' + acc_d_kept[acc][0][-3] + '__' + acc_d_kept[acc][0][-2] + '__' + acc_d_kept[acc][0][-1] + '__' #make the name include the chosen taxonomy information separated by underscores
    
    for i in acc_d_kept[acc]:
        name = name + '__' + i[0] #add the domain order information to the taxonomy information
    acc_names[acc] = name #assing the new name infomration for each sequence of interst to acc_names dictionary
    
print acc_names

    
for v in acc_names.values():    
    print v
###Now I need to print out v to a new file and use that to replace fasta headers
with open('/Users/ericsalomaki/Desktop/AcetylCoA_Evolution/Pfam/new_headers.txt','w') as new_headers:
    for value in acc_names.values():
        new_headers.write('{}\n'.format(value))
        
    
pickle.dump(acc_d_kept, open('kept_domains_dict.bin', 'wb'))
        
