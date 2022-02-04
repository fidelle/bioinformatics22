
import sys
'''translate a multiple-gene fasta file and print in fasta format'''

filehandle=sys.stdin

fasta = {}
genseq=''
for line in filehandle:
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
def translation(codonfile,multigenes_fasta):
    #fastafile=open('outputmulti.sh','w')

    codons_list = codonfile.readlines()
    #codon pairs
    codonpairs={}
    for count in range(0,len(codons_list)):
        cols=codons_list[count].rstrip().split("\t")
        codonpairs[cols[0]]=cols[1]
        
    for k,v in multigenes_fasta.items():
        seq_name=">"+k
        seq=v
        protein=''

        for i in range(0,len(seq),3):
            codon=seq[i:i+3]
            if codon in codonpairs:
                protein+=codonpairs[codon]
        
        sys.stdout.write(seq_name+'\n'+protein+ '\n')

    
    return 

f2cod=open('codon_table.txt','r')

translation(f2cod,fasta)
