#Yuval Bar
#206011355

##Task 1
def read_line(n = None, file = None):
    path = "C:/temp/"
    if type(n) == int and n>=1:
        try:
            fname = str(path + file)
            data = open(fname)
            count = 0
            for line in data:
                count += 1
            if count >= n:
                import linecache 
                line = linecache.getline(fname,n)
                return line
            else:
                return "line " + str(n) + " doesn't exist"
        except:
            return "file not found"
    else:
        return "invalid input detected"


##Task 2
def longest_words(file):
    try:
        mylist = []
        mydict = {}
        splits = ".,\/-+=_"
        path = "C:/temp/"
        fname = str(path + file)
        data = open(fname)
        for line in data:
            import re
            words = re.split(r"[\b\W\b]+", line)
            for word in words:
                mydict[word] = mydict.get(word,len(word))
        mydict_sorted = sorted([(v,k) for k,v in mydict.items()],reverse = True)
        top5 = mydict_sorted[0:5]
        for w in top5:
            mylist.append(w[1])
        return mylist
    except:
        print("file not found")
        return []

