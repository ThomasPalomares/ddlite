#Usage: python preproc.py file_list.csv list_PMC.txt

import sys

file_list = sys.argv[1]
list_PMC = sys.argv[2]

file_hash={}

with open(file_list, 'r') as file_list_read:
	for line in file_list_read:
		splitted_line=line.split(',')
		file_hash[splitted_line[2]]=splitted_line[0]

with open(list_PMC, 'r') as file_PMC_read:
	with open('PMC_url_list.txt', 'w') as write_file:
		for line in file_PMC_read:
			write_file.write('ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/' + str(file_hash[line.rstrip()]) + '\n')


