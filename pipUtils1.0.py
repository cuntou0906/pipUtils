#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:cuntou0906
@file: pipUtils1.0.py
@time: 2020/11/27
"""

#############################################################################
# 使用注意事项：

# 1、务必将所有导入语句连在一起写 包括 import ** as *** ，from *** import *** 两种语法
# 2、自定义的包不会导入哦 因为根本不可以pip安装
# 3、使用时 只需要指定 某个py文件名和 导入语句所在行数的范围   （73 -74行）
# 4、特别注意包名是否存在替换 -- 按85行模板直接添加即可
# 5. 把该文件放在工程的根目录


#改进：
#（1）该脚本仅仅是 pip 某个文件所需的包，而且需要指定 包名所在的行（import语句、from语句）
#      因为这样效率更高，特别是对于大文件的时候
# (2) 另一种方式：搜索整个工程的py文件，对于每个文件 依次2找到所需安装的包名 然后逐个安装
#      这种全自动的方式对于大文件 效率会慢些，查包名需要遍历所有py文件
#      某个文件查找包名的方法：==》
#       直接找某一行是否以import或者from开头 直接读取第二个字符串（注意要去掉.之后的，参考该脚本的方法）
#      （1）import ** as *** ：找import的后面的（“ ”分割）
#      （2）from *** import ***
# (3) 还可以把存在的包排除掉，不pip，还可以确定安装的版本

#############################################################################

import os                                              # 执行pip指令

def getpackage(path,lines):
    # 以只读模式打开文件，如果打开失败有error输出
    index = 1
    PackageName = []
    try:
        f = open(path, 'r',encoding='UTF-8')
        while(1):
            if index>=lines[0]:
                if index<=lines[1]:
                    str = f.readline()
                    # print("当前第",index,"行：",str)
                    strsplit = str.split()    # 分割字符串
                    str2 = strsplit[1]
                    loc = str2.find(".")   # 找到 . 的位置
                    if loc==-1:
                        PackageName.append(str2)
                    else:
                        PackageName.append(str2[0:loc])
                    pass
                else:
                    break
            else:
                str = f.readline()
            pass
            index = index + 1
    # 要用finally来关闭文件！
    finally:
        if f:
            f.close()
            pass
        pass
    return PackageName

#############################################################################

# 这里需要改：
# 首先是文件名path： 安装path.py 文件里的 import的包
# 导入包语句所在path中的行数范围：lines，为一个列表
#  如果使用Pycharm 直接打开文件看左侧的行号，就可以得到最大值和最小值

#############################################################################
path = 'Pack.py'                                       # 路径名称
lines = [9,13]                                         # import语句所在的行

PackageName = getpackage(path,lines)
# print(PackageName)

#############################################################################
# 因为很多包的名字和 import时候不一致 所以 这里需要替换
# 例如opencv 在import时候是cv2  但是 在安装时候是 opencv-python
# 这里需要额外添加   目前仅发现这个包 不一致  如果还有 只需要添加到这里就可以啦
# 添加方式 直接仿照下面这一行的代码就可以

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
    print("------------------正在安装" + str(PackageName[index]) + " ----------------------")
    print(comand + "\n")
    os.system(comand)

os.system("pip list")    # 显示所有的包



