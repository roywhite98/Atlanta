with open("预测ORF+blast结果定位NLP序列.txt")as file:
	lines = file.readlines()
	for line in lines:
		if line.startswith('>'):
			with open('out','a') as fw:
				fw.write(line + lines[lines.index(line)+1])
