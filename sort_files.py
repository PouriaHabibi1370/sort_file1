import os     #for make a folder
import glob   # for see everything in folder

file_list = glob.glob("*")
file_set = set()

for each_file in file_list:          #Processing in the folder   
  try:
    extension = each_file.split('.')[1]
    file_set.add(extension)
      
  except:
    continue  
   
def creat_folder():               # make folders with file extension 
  for ext in file_set:
    if ext == 'py':
      continue
    try:
      os.makedirs(ext+"_folder")
    except:
      continue


def move_files():              # files displacement 
  for each_file in file_list:
    try:
      extension = each_file.split('.')[1]
      os.rename( each_file,extension+"_folder/"+each_file)

    except:
      continue
creat_folder()
move_files()
