def tenet(input_file_path: str, output_file_path: str):
    with open(input_file_path, "r") as file, open(output_file_path, "w") as output:
        string1 =''
        string = file.readline()
        for i in range(-1,-len(string)-1,-1):
            string1 += string[i]
        output.write(string1)
    with open(output_file_path,"r") as output:
        string1 = output.readline()
        print(string,'\n',string1)
