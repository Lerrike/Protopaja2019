def data_parse(line): #example line: 26.7.2019.11.10.54#x/10#y/5#Breathing/33#Heart/85
    data_list = [0,0,0,0] #[x, y, breathing, heart]
    
    for i in range (0, len(line)):
        if line[i] == 'x':
            if line[i+3].isdigit() == True:
                data_list[0] = line[(i+2):(i+4)]
            else:
                data_list[0] = line[i+2]
                
        if line[i] == 'y':
            if line[i+3].isdigit() == True:
                data_list[1] = line[(i+2):(i+4)]
            else:
                data_list[1] = line[i+2]
                
        if line[i] == 'g':
            if line[i+3].isdigit() == True:
                data_list[2] = line[(i+2):(i+4)]
            else:
                data_list[2] = line[i+2]
        
        if line[i] == 'H':
            if len(line)-(i+9) == 0:
                data_list[3] = line[(i+6):(i+9)]
            else:
                data_list[3] = line[(i+6):(i+8)]
    
    return data_list
