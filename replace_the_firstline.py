#!/Users/zhanghuimin/anaconda3/bin/python3
import sys
with open(sys.argv[1], 'r') as fastq, open(sys.argv[2], 'r') as newnames,open(sys.argv[3], 'w') as newfastq:
    for num, line in enumerate(fastq,1):
        if num % 4 ==1:
            newname = newnames.readline()
            newfastq.write(newname)
        else:
            newfastq.write(line)
    fastq.close()
    newnames.close()
    newfastq.close()

