import os
import shutil

frmdir="C:/Users/pragy/Downloads"
todir="C:/Users/pragy/OneDrive/Desktop/projects/Document_files"

lof=os.listdir(frmdir)


for fn in lof:
    root,ext=os.path.splitext(fn)
    if ext=='':
        continue
    else:
        if ext in ['.txt','.doc','.docx','.pdf']:
          
            path1= frmdir+'/'+fn
            path2= todir+'/Document_files'
            path3=path2+'/'+fn
            print(path1)
            print(path2)
            print(path3)
            if os.path.exists(path2):
                print("moving "+fn+"...")
                shutil.move(path1,path3)
            else:
                os.makedirs(path2)
                print("moving"+fn+"...")
                shutil.move(path1,path3)
               