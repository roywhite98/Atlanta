class R():
	def __init__(self, filename):
		self.lines = []
		self.filename = filename
		# 把指定的文件按行存在lines列表中,并返回
		with open(self.filename)as file:
			self.lines = file.readlines()

		self.gene = {}

	def gene_extractor_0(self):
		# 提取基因序列
		gene_name = ''
		seq = ''
		for line in self.lines:
			if line:
				if line.startswith(">"):
					gene_name = line
					seq = ''
				else:
					seq += line
				self.gene[gene_name] = seq
		return(self.gene)

	def gene_extractor(self, gene_list, filename='gene_extractor.out'):
		# 提取对应的基因ID所对应的基因
		for gene_name in gene_list:
			if gene_name in self.gene.keys():
				with open(filename, 'a') as fw:
					fw.write(gene_name + '\n' + gene + '\n')

