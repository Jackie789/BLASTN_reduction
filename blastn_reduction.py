#!/usr/bin/env python3
import re

# Open and read in the BLASTN file
blast_name = '/home/filepath/example_blast.txt'
blast = open(blast_name)
blast_contents = blast.read()

# Uses regex to locate Query ID and Length within file
m = re.search(r"Query=(.+)", blast_contents) 
n = re.search(r"Length=(.+)", blast_contents)

# Prints Query ID and Length to STDOUT
print("Query ID:" + m.group(1))
print("Query Length: " + n.group(1))

# Splits files by '>'
blast_split = blast_contents.split(">") 

# Iterates through list, skips blast_split[0] because this first segment of the file is not used to locate Accession numbers, Length, and Score
for number in range(10):
	x = re.search(r"(.+\|.+?\|)", blast_split[number+1])
	y = re.search(r".+?Length=([0-9]+)", blast_split[number+1], re.DOTALL)
	z = re.search(r".+?Score *= *([0-9]+)", blast_split[number+1], re.DOTALL)
			
	print("Alignment #" + str(number+1) + ": Accession = " + x.group(1) + " (Length = " + y.group(1) + ", Score = " + z.group(1) + ")") 
	
# Query ID: Arf1
# Query Length: 614
# Alignment #1: Accession = ref|XM_005094338.1| (Length = 2377, Score = 1098)
# Alignment #2: Accession = gb|EU829582.1| (Length = 858, Score = 375)
# Alignment #3: Accession = ref|XM_005023737.1| (Length = 1939, Score = 372)
# Alignment #4: Accession = ref|XM_004088641.1| (Length = 3923, Score = 364)
# Alignment #5: Accession = ref|XM_004088640.1| (Length = 3898, Score = 364)
# Alignment #6: Accession = ref|XM_004088639.1| (Length = 4026, Score = 364)
# Alignment #7: Accession = ref|XM_003252207.1| (Length = 4128, Score = 364)
# Alignment #8: Accession = gb|EU829048.1| (Length = 750, Score = 364)
# Alignment #9: Accession = ref|NM_001133245.1| (Length = 3605, Score = 364)
# Alignment #10: Accession = ref|XM_003939112.1| (Length = 1417, Score = 359)	
