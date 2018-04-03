#!/usr/bin/python
import sys
skip_words = ["2018","might","trade","back","percent","email","called","around","between","tech","going","company","New","York","you're","said,","against","including","March","whether","information","including","public","help","few","then","Times","off","firm","re-enterYou","work","through","use","United","still","see","verify","think.By","use","million","still","see","first","newsletter","subscribe","told","may","much","because","In","get","many","them","select","--","take","know","says","such","think","many","clicking","address.","him","box.Invalid","users","former","him","years","used","made","being","think","these","any","time","-","down","now","way","me","where","He","there","did","2018,","even","new","last","interested","my","if","so","feedback","two","just","page.","Tell","But","do","must","Ms.","no","said.","Please","It","robot","those","only","most","make","to.View","was","my","if","so","just","while","go","the","to","a","of","and","in","that","on","for","is","with","Was","by","as","from","it","at","said","are","not","has","have","he","an","this","The","be","Mr.","his","you","about","had","who","I","or","its","their","more","what","they","were","your","but","would","will","which","been","all","she","her","up","after","than","also","we","like","one","us","can","over","could","other","when","into","out","how","some","our","and","And","before","A","since","want"]
for line in sys.stdin:
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word in skip_words:
            continue;
        print(word+"\t1")
