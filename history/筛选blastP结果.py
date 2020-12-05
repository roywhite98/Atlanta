# -*- coding: gbk -*-
from file2lines import R

filename = '123汇总.fa'
roy = R(filename)
roy.gene_extractor_0()
roy.gene_lenth(100, 300)
roy.show_gene_num()
roy.extract_species_name()
roy.export_gene_fasta()
