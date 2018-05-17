import os
import shutil
import glob


def get_subdir_filenum(super_path):  
    """Get number of files by super directory"""
    """获取所有子目录下的文件个数"""
    if not os.path.exists(super_path):
        return 0
    cnt = 0
    file_list =[]
    for r, dirs, files in os.walk(super_path):
        print(dirs)
        for dr in dirs:
            print("nothing")
            cnt += len(glob.glob(os.path.join(r, dr + "/*")))
    return cnt   

def split_image(origindatadir,traindir,overload = False):
    """Move dogs and cats image to separate directory"""
    """origindatadir: from where to import train_data"""
    """traindir: where to save the split data """
    """overload: if True and traindir and data already exist, delete traindir and split origin data again"""
    if not os.path.exists(origindatadir):
        return
    cats_dir = traindir+'/cats'
    dogs_dir = traindir+'/dogs'
    if not os.path.exists(traindir):
        os.mkdir(traindir)
        os.mkdir(cats_dir)
        os.mkdir(dogs_dir)
    else:
        #print(traindir)
        if get_subdir_filenum(traindir) > 0:
            if overload:
                shutil.rmtree(traindir)
                os.mkdir(traindir)               
                os.mkdir(cats_dir)
                os.mkdir(dogs_dir)
            else:
                print("Destination directory already exist:",traindir)
                return
    #开始复制
    filenames = os.listdir('train')
    for file in filenames:
        if str(file).startswith('cat'):
            shutil.copyfile(origindatadir+'/'+file, cats_dir+'/'+file) 
        elif str(file).startswith('dog'):
            shutil.copyfile(origindatadir+'/'+file, dogs_dir+'/'+file) 