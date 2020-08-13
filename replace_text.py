import os,sys
import time

fname = __file__
runfile = fname.replace("\\","/")

# 检查文件是否包含需要查找的字符串
def check(name,msg):
    try:
        with open(name) as f:
            res = f.readlines()
            for i in range(len(res)):
                if msg in res[i]:
                    return True
    except Exception as e:
        with open(name,encoding="unicode_escape") as f:
            res = f.readlines()
            for i in range(len(res)):
                if msg in res[i]:
                    return True
    return False


# 进行替换内容
def readfile(name,msg,newmsg):
    try:
        with open(name) as f, open(name+".bak","w") as f1:
            res = f.readlines()
            for i in range(len(res)):
                if msg in res[i]:
                    res[i] = res[i].replace(msg,newmsg) 
                f1.write(res[i])
            f.close()
            f1.close()
            os.remove(name)
            os.rename(name+".bak",name)  
    except Exception as e:
        with open(name,encoding="unicode_escape") as f,open(name+".bak","w",encoding="unicode_escape") as f1:
            res = f.readlines()
            for i in range(len(res)):
                if msg in res[i]:
                    res[i] = res[i].replace(msg,newmsg) 
                f1.write(res[i])
                
            
            f.close()
            f1.close()
        os.remove(name)
        os.rename(name+".bak",name)  


# 遍历目录
def getfolder(path,msg,newmsg):
    nums = 0
    repir = []
    for root,dirs,files in os.walk(path):
        if ".git" in root:
            pass
        else:
            for i in files:
                name = root+"/"+i
                if name.endswith(("gif","png","jpg","ttf","xlsx")) :
                    pass
                elif i == os.path.basename(__file__) :
                    pass
                elif check(name,msg):
                    nums +=1
                    repir.append(name)
                    res = readfile(name,msg,newmsg)
    print("共修改{}个文件，文件列表：{}".format(nums,"".join(repir)))

    
if __name__ == '__main__':
    getfolder(os.getcwd(),"github.com/lxn","github.com/xuchengzhi")