#12、简述with方法打开处理文件帮我我们做了什么？
#打开文件在进行读写的时候可能会出现一些异常状况，如果按照常规的f.open
#写法，我们需要try,except,finally，做异常判断，并且文件最终不管遇到什么情况，都要执行finally f.close()关闭文件，
# with方法帮我们实现了finally中f.close
#（当然还有其他自定义功能，有兴趣可以研究with方法源码）
f = open("./three.txt","w")
try:
    f.write("hello world")
except:
    pass
finally:
    f.close()