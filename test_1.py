#@Time:2/23/20219:21 AM
#@Author: Mini(Wang Han)
#@Site:
#@File:test_1.py
string=["A","B","C","A","D","B","A","D","F"]
i_1=0
i_2=0
i_3=0
for i in range(0,len(string)):
    if i==0:
        string_single = [string[i]]
    elif string[i] in string_single:
        pass
    else:
        string_single .append(string[i])
for j in range(0, len(string_single)):
    if j == 0:
        for i in range(0, len(string)):
            if string[i]== string_single[j]:
                i_1 += 1
        i_2 = i_1
    else:
        i_1 = 0
        for i in range(0, len(string)):
            if string[i]== string_single[j]:
                i_1 += 1
        if i_1 > i_2:
            i_2 = i_1
            i_3 += 1
        else:
            pass
print("频率最高的数据项是：",string_single[i_3])





