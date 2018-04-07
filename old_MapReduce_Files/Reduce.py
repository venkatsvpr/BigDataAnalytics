import sys
word = None;
prev_word = None;
prev_count = 0;
input = open("tmp/reduce_in.txt",'r')
output = open("tmp/reduce_out.txt",'w')
for line in input:
    line = line.strip()
    word,count =  line.split('\t',1)
    count = int(count)
    if (prev_word == None):
        prev_word = word
        continue
    elif (prev_word == word):
        prev_count += count
    else:
        output.write(prev_word+"\t"+str(prev_count)+"\n")
        prev_word = word
        prev_count = count
output.write(prev_word+"\t"+str(prev_count))
output.close()
input.close()
