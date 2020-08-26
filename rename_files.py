import os

def remove_first_characters(a):
    # negative values would mess up the indexing
    a = abs(a)
    for i in sorted(os.listdir(os.getcwd())):
        name = os.path.splitext(i)[0]
        # filetype 0 means that the file has no type, should be a folder in most cases
        filetype = os.path.splitext(i)[1] if len(os.path.splitext(i)[1]) > 0 else "0"
        
        if filetype != "0" and filetype != ".py" and len(name) - a > 0:
            os.rename(i, i[a::])


# remove the first 3 letters of every file in current directory that isnt a folder or a python script
remove_first_characters(3)
