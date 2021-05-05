#Word Break

def dictionaryContains(word):
    global dict
    return word in dict

def wordBreak(string):
    wordBreakUtil(string, len(string), "")

def wordBreakUtil(string, n, result):
    global output_name
    for i in range(1, n + 1):
        prefix = string[:i]
        if dictionaryContains(prefix):
            if i == n:
                result += prefix
                with open(str(output_name) + ".txt","a+") as f:
                    f.write(result+"\n")
                print(result)
                f.close()
                return
            wordBreakUtil(string[i:], n - i, result + prefix + " ")


if __name__ == "__main__":
    while True:
        try:
            dict_name = input("Enter the dictionary text file name:")
            with open(str(dict_name)+".txt", "r") as fd:
                dict = fd.read().strip().split(",")
                dict = set(dict)
            input_name = input('Enter the input text file name:')
            with open(str(input_name) + ".txt", "r") as fi:
                words = fi.read().split("\n")
                print(words)
            output_name = input('Enter the output text file name:')
            f = open(str(output_name)+".txt","w")
            f.close()
            break
        except:
            print("Enter the correct file name!")

    for word in words:
        wordBreak(word)
