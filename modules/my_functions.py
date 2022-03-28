import os
import itertools #used to flat out list of lists
def get_file_names(folderpath, out='output.txt'):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    dir_list = os.listdir(folderpath)

    print(dir_list)
    #['.ipynb_checkpoints', 'modules', 'output.txt']
    output_file = folderpath + "/" + out
    
    with open(output_file, 'w') as file_object:
        for file_name in dir_list:
            entry = str(file_name) + "\n"
            file_object.write(entry)
            
def get_all_file_names(folderpath,out='output_files.txt'):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
    all_file_names = []
    for dirpath, dirnames, filenames in os.walk(folderpath):
        #print(
        #f"Root: {dirpath}\n"
        #f"Subdirectories: {dirnames},\n"
        #f"File: {filenames} \n \n"
        #)
        all_file_names.append(filenames)
        
    output_file = folderpath + "/" + out
    all_file_names_final = list(itertools.chain.from_iterable(all_file_names))#flatten out list
    print(all_file_names_final)
    with open(output_file, 'w') as file_object:
        for file_name in all_file_names_final:
            entry = str(file_name) + "\n"
            file_object.write(entry)
            print(entry)
    
        
    
def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""
    for file_name in file_names:
        with open(file_name) as file_object:
            content = file_object.readlines()
            
            for line in content[:1]:
             print(line)
              
            
        

def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""

def write_headlines(md_files, out='output.txt'):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""


 