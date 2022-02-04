'''translate a single gene Fasta file and print in fasta format use codon_table.txt'''
import sys 

def translation(codonfile,sequencefile):
    codons_list = codonfile.readlines()
    #codon pairs
    codonpairs={}
    for count in range(0,len(codons_list)):
        cols=codons_list[count].rstrip().split("\t")
        codonpairs[cols[0]]=cols[1]
    #sequence extraction
    seq=''
    for line in sequencefile:
        line = line.rstrip("\n") #rstrip removes trailine \n
        if not line:#line is empty
            continue
        if line.startswith(">"):
            seq_name = line#[1:]#gets first line without \n
            #fasta[seq_name] = ['']
            continue
        seq= seq+line
        #fasta[seq_name][-1] += sequence #sets as last element value 
    #sequence to protein
    protein=''

    for i in range(0,len(seq),3):
        codon=seq[i:i+3]
        if codon in codonpairs:
            protein+=codonpairs[codon]
        
#     fastafile=open('output.txt','w')
#     fastafile.write
    return (seq_name,protein)



f2cod=open('codon_table.txt','r')
f2gene=sys.stdin

res=translation(f2cod,f2gene)

#fastafile=open('output.sh','w')
#fastafile.write(res[0]+'\n'+res[1])

sys.stdout.write(res[0] +'\n'+res[1])

#fastafile.close()
