#@Time:2/23/20219:21 AM
#@Author: Mini(Wang Han)
#@Site:
#@File:test_1.py
string=["A","B","C","A","D","B","A","D","F"]
#string=["F","E","C","A","D","B","A","D","A","D","B","B"]
i_1=0
i_2=0
i_3=[]
for i in range(0,len(string)):
    if i==0:
        string_single = [string[i]]
    elif string[i] in string_single:
        pass
    else:
        string_single .append(string[i])
for j in range(0, len(string_single)):
    i_1 = 0
    if j == 0:
        for i in range(0, len(string)):
            if string[i]== string_single[j]:
                i_1 += 1
        i_2 = i_1
        i_3 = [j]
    else:
        for i in range(0, len(string)):
            if string[i]== string_single[j]:
                i_1 += 1
        if i_1 > i_2:
            i_3 =[j]
            i_2 = i_1
            i_0=j
        elif i_1 ==i_2:
            i_3.append(j)
i_3=list(set(i_3))
for i in i_3:
    print("频率最高的数据项是：",string_single[i])





