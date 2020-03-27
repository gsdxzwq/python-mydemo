# 极客时间03 09讲字符串
# 记录生肖，根据年份判断

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

year = int(input('输入年份'))
if (chinese_zodiac[year % 12]) == '狗':
    print('狗年运势。。。')

for cz in chinese_zodiac:
    print(cz)