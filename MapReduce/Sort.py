import sys
with open("tmp/map_out.txt",'r') as input:
    lines = input.readlines()
    sortedlines = sorted(lines)
    with open("tmp/reduce_in.txt",'w') as output:
        for line in sortedlines:
            output.write(line)
    output.close()
input.close()
