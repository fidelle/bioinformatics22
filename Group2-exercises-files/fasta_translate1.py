
import sys
filehandle=sys.stdin
fasta = {}
seq=''
for line in filehandle:
    line = line.rstrip("\n") #rstrip removes trailine \n
    if not line:#line is empty
        continue
    if line.startswith(">"):
        seq_name = line[1:]#gets first line without \n
        fasta[seq_name] = ['']
        continue
    seq= seq+line
    #fasta[seq_name][-1] += sequence #sets as last element value 
seqdict={seq_name:seq}
#sys.stdout.write(seqdict)
print(seqdict)

