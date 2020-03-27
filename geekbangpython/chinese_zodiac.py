# 极客时间03 09讲字符串
# 记录生肖，根据年份判断

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

print(chinese_zodiac[0:4])

print(chinese_zodiac[-1])

year = 2018
print(chinese_zodiac[year % 12])

print('狗' not in chinese_zodiac)

print(chinese_zodiac + 'abcd')
print(chinese_zodiac * 3)
