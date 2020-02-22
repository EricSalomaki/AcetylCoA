import os
import sys
import glob


treefile = sys.argv[1]
alnfile = sys.argv[2]
outfile = sys.argv[3]


infile = open(treefile)
line = infile.read()
infile.close()
	
names = line.split('taxlabels')[1] ###split the infile on 'taxlabels' and keep the second split as the string called  names
names = names.split(';\nend;\n')[0] ### split the string 'names' on the ;\nend\n and keeps the first part as the string called names
names = names.split('\n') ###split the string names on hard returns looking like this - 'a\nb\nc\nd\n' into a list like this ['a', 'b', 'c', 'd']

tokeep = [] ### make a list called tokeep
print names ### print input list called names
while '' in names: ### while there are '' in a string in list names
	names.remove('') ### remove the ''
for name in names: ### for each string in the list names
	print(name) ### print the string
	if name.count('[&') != 0 : ### If the name count has any occurrences of "[&" (beginning of a color annotation from figtree) then pass through the following
		print ('%s' % (name)) ### print every string in names (those that have the color annotation) - also look into the .format function rather than the %s place holder
		newname = name.split('[&')[0] ### make list newname from the strings in list name that had the color annotation, but removed the annotation (so those we want to remove without the color indication)
		print(newname) ### print out the newname (those we want to remove)
		while newname.count("'") != 0: ### while there are strings in newname that have occurrences of "'" more than zero
			newname = newname.replace("'", "") ### replace the apostrophe with nothing
    		tokeep.append(newname.strip()) ### add newname with whitespace removed to the list tokeep

print(tokeep) ### print the list tokeep
print(len(tokeep)) ### print the number of strings in the list tokeep

infile = open(alnfile) ### open system argument 2 - the alignment 
line = infile.read() ### read infile in as line
infile.close() ### close infile
seqs = line.split('>')[1:] ### split line on >, keep everything after the first split (which was an empty space due to split always breaking into two - first > had nothing before it)
seq_d = {} ### make an empty directory called seq_d

for seq in seqs: ### for every string in list seqs
	seq_d[seq.split()[0].replace('-','')] = ''.join(seq.split('\n')[1:]) ### make seq_d of key seq first part with "-" removed (sequence name) and value

print seq_d


out = open(outfile, 'w')

for i in tokeep:
	prd = seq_d[i]

for seq in seqs:
	name = seq.split('\n')[0]
        name.split('-')[0]
#        name.split(':')[0]
        name.split(';')[0]
        name.split('(')[0]
        name.split(')')[0]
	if name in tokeep:
		out.write('>%s\n%s\n' % (seq.split('\n')[0], ''.join(seq.split('\n')[1:])))
