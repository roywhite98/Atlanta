import re



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
					gene_name = line.strip()
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

	def gene_lenth(self, a, b):
		# 筛选位于a, b之间的序列
		for gene_name, gene_seq in list(self.gene.items()):
			if len(gene_seq) >= int(a) and len(gene_seq) <= int(b):
				pass
			else:
				del self.gene[gene_name]
		return(self.gene)

	def show_gene_num(self):
		# 展示基因文件包含多少个基因
		print('基因数: ' + str(len(self.gene)) + '\n')
	
	def export_gene_fasta(self):
		# 输出基因fasta文件
		with open(self.filename + '.out','w')as file:
			for gene_name, seq in self.gene.items():
				file.write(gene_name + "\n" + seq )

	def extract_species_name(self):
		# 提取物种名
		for gene_name in list(self.gene.keys()):
			string = gene_name 
			pattern = re.compile(r'^(\>[\w\.]+)\s([\w\-\s\W]+?)\[([\w]+[\s]*[A-Za-z]+).*\]$')
			a = pattern.match(string)
			self.gene[a.group(1) + '|' + a.group(3)] = self.gene.pop(gene_name)
		

