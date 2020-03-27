import sys

print("hello world")

x = 'runoob'
sys.stdout.write(x + '\n')

x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()

print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)