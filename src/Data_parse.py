#Parses the data from a string into a list of size 4.
def data_parse(line): #example line: Nimi/Samuel#26.7.2019.11.10.54#x/10#y/5#Breathing/33#Heart/85
    data_list = [0,0,0,0,0] #[x, y, breathing, heart]
    parts = line.split("#")
    print(line)
    data_list[0] = parts[1].split("/")[1]
    data_list[1] = parts[2].split("/")[1]
    data_list[2] = parts[3].split("/")[1]
    data_list[3] = parts[4].split("/")[1]
    data_list[4] = parts[5].split("/")[1]
    
    return data_list
