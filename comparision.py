#Comparision

def compareFiles(output,e_output):
    count = 0
    for i in range(len(output)):
        if output[i]==e_output[i]:
            count+=1
    print("Total outputs : %d"%len(output))
    print("The count of matching outputs : %d"%count)

if __name__ == "__main__":
    import argparse

    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-e_o", "--e_output", required=True,
                    help="expected output file")
    ap.add_argument("-o", "--output", required=True,
                    help="output file")
    args = vars(ap.parse_args())
    try:
        lines1,lines2 =[],[]
        output_name = args["output"]
        with open(str(output_name), "r") as fo:
            lines1 = fo.read().split("\n")
        expected_output_name = args["e_output"]
        with open(str(expected_output_name), "r") as fe:
            lines2 = fe.read().split("\n")
        compareFiles(lines1, lines2)
    except:
            print("file not found!")
