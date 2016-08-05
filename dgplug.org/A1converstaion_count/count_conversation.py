'''
Assignment 1
Take the 4 logs from the top of https://dgplug.org/irclogs/2016/  and then try to find for each nick ever present in those files, who spoke with whom highest number of times.

Like: kushal spoke to avik 35 times
      avik spoke to gkadam 55 times

and like that, for all the nicks.

Algorithm
1  read file in log list
2  create nick name list
3  on every line check if second element substring is in list 
4     
'''

import os
import glob  #glob gave advantage of regular expression

name_list = []
name_combination = []

def main(file_name):
    global name_list
    global name_combination

    with open(file_name, 'r') as file1:
        for line in file1:
            #print line
            line_split = line.split(" ")
            line_split.pop(0)
            if line_split[0] not in name_list and line_split[0] != "[##" and line_split[0] != '*':
                name_list.append(line_split[0])
        name_list = map(lambda name: name.rstrip('>').lstrip('<'), name_list)

    #import ipdb;ipdb.set_trace();
    with open(file_name, 'r') as file1:
        for line in file1:
            from_name='' ; to_name = ''; new_combination = []; got_it = 0; 
            line_split = line.split(" ")
            line_split.pop(0)
            from_name = line_split[0].rstrip('>').lstrip('<').strip(' ')
            to_name = line_split[1].strip(' ')
            #check from name for [## or * like entries
            if from_name not in name_list:
                continue
            #search using regex whether to_name present in element[2]
            if to_name not in name_list:
                if to_name[:-1] not in name_list:
                    continue
                else: 
                    to_name = to_name[:-1]

            if from_name == to_name:
                continue

            #if no entry in combination list add first
            if name_combination == []:
                new_combination = [from_name, to_name, 1]
                name_combination.append(new_combination)
                continue
                
            for element in name_combination:
                if from_name in element and to_name in element:
                    element[2] = element[2] + 1
                    got_it = 1            

            if got_it == 0:
                new_combination = [from_name, to_name, 1]
                name_combination.append(new_combination)

if __name__ == "__main__":
    #    os.path.exists("/home/anjali/Documents/Python/dgplug.org/irclogs/2016/Logs-2016-07-27-16-37.txt")
    #    os.listdir(os.getcwd())
    log_files = glob.glob(os.getcwd() + "/Log*")
    for log_file in log_files:
        main(log_file)
    #print name_list
    for combo in name_combination:
        print combo
