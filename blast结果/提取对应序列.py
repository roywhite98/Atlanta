filename = "tblastnresult"
with open(filename)as file:
	lines = file.readlines()
	for line in lines:
		list = line.split()
		seqid = list[1]
		sstar = list[8]
		send = list[9]
		
		with open(filename + '.out', 'a')as fw:
			fw.write(seqid + '\t' + sstar + '\t' + send + '\n') 
