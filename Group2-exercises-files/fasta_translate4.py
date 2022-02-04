'''translate a multiple gene fasta file containing missing and unknown nucleotides and print Fasta format'''
import sys 

messy=sys.stdin

fasta = {}
genseq=''
for line in messy:
    line = line.rstrip("\n") #rstrip removes trailine \n
    if not line:#line is empty
        continue
    if line.startswith(">"):
        name = line[1:]#gets first line without \n
        if name in fasta:
            fasta[name].append('')
        else:
            fasta[name] = ['']
            genseq=''
        continue
    genseq = genseq+line
    #print(fasta[name][-1])
    fasta[name]= genseq #sets as last element value 


hardcodonfile=open('codon_table_hard.txt','r')
codons_list = hardcodonfile.readlines()
codonpairs={}

for count in range(0,len(codons_list)):
    cols=codons_list[count].rstrip().split("\t")
    colscodons=cols[2].split(',')
    for i in colscodons:
        codonpairs[i]=cols[1]


for k,v in fasta.items():
        seq_name=">"+k
        seq=v
        protein=''

        for i in range(0,len(seq),3):
            codon=seq[i:i+3]
            if 'X' in codon:
               # print('fix this')
                sys.stderr.write('Invalid: '+ codon +' ,')
            if codon in codonpairs:
                 protein+=codonpairs[codon]
        sys.stdout.write(seq_name+'\n'+protein+ '\n')



