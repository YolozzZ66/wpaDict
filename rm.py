# 打开文件
file = open('wpaDict.txt', 'r')

# 读取文件内容到列表中
lines = file.readlines()

# 关闭文件
file.close()

# 去除重复行
lines = list(set(lines))

# 创建新的文件
new_file = open('wpaDict1.txt', 'w')

# 写入去重后的内容
new_file.writelines(lines)

# 关闭文件
new_file.close()