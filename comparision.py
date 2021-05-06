#Comparision

def compareFiles(output,e_output):
    count = 0
    for i in range(len(output)):
        if output[i]==e_output[i]:
            count+=1
    print("Total outputs : %d"%len(output))
    print("The count of matching outputs : %d"%count)

if __name__ == "__main__":
    while True:
        try:
            lines1,lines2 =[],[]
            output_name = input("Enter the output file name:")
            with open(str(output_name) + ".txt", "r") as fo:
                lines1 = fo.read().split("\n")
            expected_output_name = input("Enter the expected output file name:")
            with open(str(expected_output_name) + ".txt", "r") as fe:
                lines2 = fe.read().split("\n")
            break
        except:
            print("file not found!")

    compareFiles(lines1,lines2)