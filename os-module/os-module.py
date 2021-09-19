import os
from posixpath import basename

# # get the current working directory
# print(os.getcwd())

# # change directory
# os.chdir('~/Downloads')

# # list the files in the directory
# print(os.listdir())

# # create a new directory
# os.mkdir('folder-name')

# # create a directory and also the subdirectories in it
# os.makedirs('folder/subfolder')

# # remove the folder
# os.rmdir('folder')

# # remove the folder and also the folder in the subdirectoy
# os.removedirs('folder/subfolder')

# # check if is dir
# print(os.path.isdir('/var/www/html'))

# # check if is file
# print(os.path.isfile('/var/www/html/index.txt'))
home_path = os.environ.get('HOME')
bash_aliases_path = os.path.join(home_path, '.bash_aliases')
shell_programs_path = os.path.join(home_path, 'shell_programs')

print(os.path.exists(home_path))

if os.path.exists(bash_aliases_path):
    print(f'{os.path.basename(bash_aliases_path)} already exists in {bash_aliases_path}.')

file = 'test.txt'
open(file, 'a').close()

cmd = 'ls'
print(os.getcwd())
os.system(cmd)