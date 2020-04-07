# 烦死我了，拿这个东西写个毕设吧。
## evalue为default = 10，未筛选
+ megablastn方法->megablastnresult(2hits）
+ blastn方法->blastnresult(7hits)
+ tblastn方法->tblastnresult(11hits)
## 经比对发现，由于blast基于传说中的种子扩展算法，得出的序列很可能不完整，因此进行基因组注释
+ 同源注释：下载几个其他代表性动植物的完整的蛋白集, 使用 TblastN 将蛋白序列比对到初步组装结果的序列上，E-value的阈值为1e-5. 将不同蛋白的BLAST的hits用 Solar 软件进行合并。GeneWise 根据每个BLAST hit的对应基因区域预测完整的基因结构。
同源预测软件通常利用GeneWise和GeneMoMa，前者是需要同源物种的蛋白序列，后者需要同源物种基因组序列及对应的GFF文件，目前小编已经抛弃GeneWise，使用最多的就是GeneMoMa，但是让小编十分头疼的是在准备GFF文件太花费精力，这个软件真的是挑肥拣瘦，必须满足其格式才能可以运行，目前从NCBI的Reseq和Ensemble上下载都可以，其他地方来的那就得还点时间写个脚本改下了。
+ 转录组预测：用Tophat将RNA-seq数据比对到初步组装结果的序列上，然后用cufflinks组装转录本形成基因模型。
转录组数据预测PASA软件是基于Unigene/EST序列进行预测软件，这个可能就需要拿到一个混样转录组数据首先进行无参组装，接下来根据Unigene组装结果在进行比对，通常用Gmap或Blat两种方法，最好三代全长转录本和二代一起来进行预测，这样可以使得找到的结构更为准确、可靠，此外PASA还有另外的一个功能就是可以用其预测可变剪切，俗称PASA修饰。
+ 从头预测：先构建repeat-mask genome， 在这个基础上就用 August, Genescan, GlimmerHMM, Geneid 和 SNAP 预测编码区
## 用TBtools预测ORF，配合tblastn结果->新鲜出炉的NLP序列