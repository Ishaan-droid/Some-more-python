import os

def printListDirectory(list_path,directory_indent,file_indent):
    
    PATH = os.path.expanduser(list_path)
    directories = os.listdir(PATH)

    for dir in directories:
        if(os.path.isdir(PATH + f'/{dir}')):
            print(' ' * directory_indent + '- D ' + dir)
            printListDirectory(PATH + f'/{dir}',directory_indent + 1,file_indent + 1)

        if(os.path.isfile(PATH + f'/{dir}')):
            print(' ' * file_indent + '- F ' + dir)


printListDirectory('~/Desktop/input_directory',1,1)
