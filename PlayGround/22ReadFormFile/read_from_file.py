
'''
read from file

Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!

'''

def main():
    dict_name = {}
    with open('nameslist.txt', 'r') as file_namelist:
        str_line = file_namelist.readline()
        while str_line:
            try:
                str_name = str_line.rstrip()
                num_count = dict_name[str_name]
            except KeyError:
                num_count = 0
            finally:
                dict_name[str_name] = num_count + 1
                str_line = file_namelist.readline()
    for item_dict in dict_name.items():
        print(item_dict)
    
def main2():
    dict_name = {}
    with open('nameslist.txt', 'r') as file_namelist:
        str_line = file_namelist.readline()
        while str_line:
            str_name = str_line.rstrip()
            if str_name in dict_name:
                dict_name[str_name] += 1
            else:
                dict_name[str_name] = 1
            str_line = file_namelist.readline()
    for item_dict in dict_name.items():
        print(item_dict)
    
            
if __name__ == '__main__':
    main2()




