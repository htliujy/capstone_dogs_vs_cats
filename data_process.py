import os
import shutil
import glob


def get_num_files(directory):
    """Get number of files by directory"""
    """获取文件个数，包括子文件夹？？"""
    if not os.path.exists(directory):
        return 0
    cnt = 0
    file_list =[]
    for r, dirs, files in os.walk(directory):
        for dr in dirs:
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
        if get_num_files(traindir) > 0:
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