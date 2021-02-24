# frequent_item_search
在网络搜索中，如何找到频繁查询？即如何找到在数据流中出现频率最高的数据项：
1）讨论例子：给定这组以字母为标志的查询："A","B","C","A","D","B","A","D","F"，假设内存中有3个存放技术的空间，如何找到出现最频繁的查询？
2）给其算法的基础


1.计算不重复的项集，记为string_single
2.for j in string_single:
    计算string_single第一项的频率i_1
    i_2=i_1
    i_3 = [j]
    计算string_single第二项到len(string_single)项的频率i_1
    if  i_2<i_1:
        i_2=i_1
        i_3 = [j]
if  i_2=i_1:
        i_3.append(j)
3.去除i_3中的重复项
4. for i in i_3:
   print("频率最高的数据项是："，string_single[i])
