# 毕设
## 葡萄霜霉菌NLP家族鉴定
### evalue为default = 10，未筛选
+ megablastn方法->[megablastnresult(2hits）](https://github.com/roywhite98/Atlanta/blob/dev/blast%E7%BB%93%E6%9E%9C/megablastnresult)
+ blastn方法->[blastnresult(7hits)](https://github.com/roywhite98/Atlanta/blob/dev/blast%E7%BB%93%E6%9E%9C/blastnresult)
+ tblastn方法->筛选掉evalue>0的序列(11hits-3hits)->[tblastnresult(8hits)](https://github.com/roywhite98/Atlanta/blob/dev/blast%E7%BB%93%E6%9E%9C/tblastnresult)
### 经比对发现，由于blast基于传说中的种子扩展算法，得出的序列很可能不完整，因此进行基因组注释
>+ 同源注释：下载几个其他代表性动植物的完整的蛋白集, 使用 TblastN 将蛋白序列比对到初步组装结果的序列上，E-value的阈值为1e-5. 将不同蛋白的BLAST的hits用 Solar 软件进行合并。GeneWise 根据每个BLAST hit的对应基因区域预测完整的基因结构。
>同源预测软件通常利用GeneWise和GeneMoMa，前者是需要同源物种的蛋白序列，后者需要同源物种基因组序列及对应的GFF文件，目前小编已经抛弃GeneWise，使用最多的就是GeneMoMa，但是让小编十分头疼的是在准备GFF文件太花费精力，这个软件真的是挑肥拣瘦，必须满足其格式才能可以运行，目前从NCBI的Reseq和Ensemble上下载都可以，其他地方来的那就得还点时间写个脚本改下了。
>+ 转录组预测：用Tophat将RNA-seq数据比对到初步组装结果的序列上，然后用cufflinks组装转录本形成基因模型。
>转录组数据预测PASA软件是基于Unigene/EST序列进行预测软件，这个可能就需要拿到一个混样转录组数据首先进行无参组装，接下来根据Unigene组装结果在进行比对，通常用Gmap或Blat两种方法，最好三代全长转录本和二代一起来进行预测，这样可以使得找到的结构更为准确、可靠，此外PASA还有另外的一个功能就是可以用其预测可变剪切，俗称PASA修饰。
>+ 从头预测：先构建repeat-mask genome， 在这个基础上就用 August, Genescan, GlimmerHMM, Geneid 和 SNAP 预测编码区
### 用TBtools预测ORF，配合tblastn结果->新鲜出炉的NLP序列
1. 新鲜出炉的NLP序列，提取DNA序列->[预测ORF+blast结果NLP基因](https://github.com/roywhite98/Atlanta/blob/dev/%E9%A2%84%E6%B5%8BORF%2Bblast%E7%BB%93%E6%9E%9CNLP%E5%9F%BA%E5%9B%A0.fa)
2. 使用megaX翻译序列->[预测ORF+blast结果NLP基因.AA.fas](https://github.com/roywhite98/Atlanta/blob/dev/%E9%A2%84%E6%B5%8BORF%2Bblast%E7%BB%93%E6%9E%9CNLP%E5%9F%BA%E5%9B%A0.AA.fas)
3. 使用Clustal Omega进行序列比对，使用Jalview美化->![鉴定的序列.png](https://github.com/roywhite98/Atlanta/blob/dev/%E9%89%B4%E5%AE%9A%E7%9A%84%E5%BA%8F%E5%88%97.png)
4. 使用SignalP5.0进行信号肽预测，使用SecretomeP2.0进行非经典分泌预测->[序列信息.xls](https://github.com/roywhite98/Atlanta/blob/dev/%E5%BA%8F%E5%88%97%E4%BF%A1%E6%81%AF.xlsx)

## 多卵菌NLP基因家族鉴定
### NCBI搜集typeⅠ，typeⅡ，typeⅢ代表序列
+ **typeⅠ** Afu5g02100 = XP_748132.1 conserved hypothetical protein \[Aspergillus fumigatus Af293\]
+ **typeⅡ** PsojNIP = AM48170.1 necrosis-inducing protein \[Phytophthora sojae\]
+ **typeⅢ** NLPPcc = ACT13867.1 Necrosis inducing protein \[Pectobacterium carotovorum subsp. carotovorum PC1\]

### 进行blastp分析
使用BlastP方法对nr数据库进行比对，取identify>=80%的序列，evalue小于1e-5的序列，并人工筛选在100aa到300aa的序列。  
得到了三个输出结果，并将其合并在[123汇总.fa]中。
_整理了仓库_ 添加了几个文件夹

