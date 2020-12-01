#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:cuntou0906
@file: pipUtils2.0.py
@time: 2020/11/27
"""

#############################################################################
# 使用注意事项：

# 1、注意  要忽略的当前文件夹！！！！一般都是环境配置的目录 不需要pip  仿造69-70行代码
# 2、自定义的包不会导入哦 因为根本不可以pip安装
# 3、特别注意包名是否存在替换 -- 按76行模板直接添加即可  （105行）
# 4. 把该文件放在工程的根目录

# 改进：
# (1) 还可以把存在的包排除掉，不pip，还可以确定安装的版本

#############################################################################

import os

def getpackage(path):
    # 以只读模式打开文件，如果打开失败有error输出
    # PackageName = []
    try:
        f = open(path,mode= 'r',encoding='UTF-8')
        str = f.readline()
        while(str):
           # print("当前第 行：",str)
           strsplit = str.split()    # 分割字符串
           # print(strsplit)
           if len(strsplit) >=2:
               if (strsplit[0] == "import") or (strsplit[0] == "from"):
                   str2 = strsplit[1]
                   loc = str2.find(".")  # 找到 . 的位置
                   if loc == -1:
                       PackageName.append(str2)
                   else:
                       PackageName.append(str2[0:loc])
                       pass
               else:
                   pass
           str = f.readline()

    # 要用finally来关闭文件！
    finally:
        if f:
            f.close()
            pass
        pass
    # return PackageName


CurAllDir = [dir for dir in os.listdir("./")]
CurDir = []
CurFil = []
for index in CurAllDir:
    if os.path.isdir('.\\'+index):
        CurDir.append(".\\"+index)
        pass
    else:
        CurFil.append("./"+index)
    pass



#############################################################################
# 注意要忽略的文件夹！！！ 只支持当前文件夹！！！ 要忽略的直接这里按摩板添加就可以啦

CurDir.remove(".\\venv")     # 去除部分目录  主要是venv环境目录
CurDir.remove(".\\.idea")     # 去除部分目录  主要是venv环境目录

#############################################################################

# print(CurDir)  # 当前需要pip 的目录
# print(CurFil)  # 当前需要pip 的文件


PackageName = []   # 保存所有包名

for dir in CurDir:  # 对每个文件夹处理
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".py"):
                # print(os.path.join(root, file))
                filename = str(os.path.join(root, file)).replace("\\","/")
                # print(filename)
                getpackage(str(os.path.join(root, file)))
                pass
            pass
        pass
    pass
# print(PackageName)

for dir in CurFil:   # 对当前目录下文件处理
    getpackage(dir)
    pass
# print(PackageName)

#############################################################################
# 因为很多包的名字和 import时候不一致 所以 这里需要替换
# 例如opencv 在import时候是cv2  但是 在安装时候是 opencv-python
# 这里需要额外添加   目前仅发现这个包 不一致  如果还有 只需要添加到这里就可以啦
# 添加方式 直接仿照下面这一行的代码就可以   !!!欢迎补充

PackageName = ['opencv-python' if i =='cv2' else i for i in PackageName]

#############################################################################


PackageName = list(set(PackageName))   # 去除重复的包名
print("所需安装的包：" ,PackageName)
print("总共需要安装  " ,len(PackageName),"  个包")

#############################################################################
# 阿里云 http://mirrors.aliyun.com/pypi/simple/
# 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
# 豆瓣(douban) http://pypi.douban.com/simple/
# 清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
# 中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/

#############################################################################
jingxiangstr = "https://pypi.tuna.tsinghua.edu.cn/simple/"  # 镜像源
for index in range(len(PackageName)):
    # 这里就直接pip安装了 不管之前是否有装过
    # 还可以先获取所有已经安装的包名字 然后判断是否已经装过了
    # 如果已经装过包 那么去查找可能很慢 还不如 直接装

    comand = "pip install " + PackageName[index] +" -i "+jingxiangstr
    # 正在安装
    print("------------------正在安装"+str(PackageName[index])+" ----------------------")
    print(comand+"\n")
    os.system(comand)

os.system("pip list")    # 显示所有的包


