#4、字典如何删除键和合并两个字典
#del和update方法
dic = {'name':'lc','age':'18'}
del dic ['name']
print(dic)
#

dic1 = {'name':'lc'}
dic2 = {'age':'18'}
dic1.update(dic2)
print (dic1)