#Word Break

def dictionaryContains(word):
    global dict
    return word in dict

def wordBreak(string):
    wordBreakUtil(string, len(string), "")

def wordBreakUtil(string, n, result):
    global output_name
    global counter
    for i in range(1, n + 1):
        prefix = string[:i]
        if dictionaryContains(prefix):
            if i == n:
                result += prefix
                if counter == 1:
                    with open(str(output_name) + ".txt","a+") as f:
                        f.write(result+"\n")
                    print(result)
                    counter=0
                    f.close()
                return
            wordBreakUtil(string[i:], n - i, result + prefix + " ")


if __name__ == "__main__":
    import argparse
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True,
                    help="input file")
    ap.add_argument("-o", "--output", required=True,
                    help="output file")
    ap.add_argument("-dic", "--dict", required=True,
                    help="dictionary file")
    args = vars(ap.parse_args())
    try:
        dict_name = args["dict"]
        with open(str(dict_name), "r") as fd:
            dict = fd.read().strip().split(",")
            dict = set(dict)
        input_name = args["input"]
        with open(str(input_name), "r") as fi:
            words = fi.read().split("\n")
            #print(words)
        output_name = args["output"]
        f = open(str(output_name)+".txt","w")
        f.close()
        counter = 1
        for word in words:
            wordBreak(word)
            counter = 1
    except:
        print("Enter the correct file name!")
