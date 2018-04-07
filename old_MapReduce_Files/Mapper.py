import sys
with open("tmp/map_in.txt","r") as ifile:
    with open("tmp/map_out.txt","w") as f:
        for line in ifile:
            line = line.strip()
            words = line.split(" ")
            for word in words:
                f.write(word+"\t1")
                f.write("\n")
        f.close();
    ifile.close();
