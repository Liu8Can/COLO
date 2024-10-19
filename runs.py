import csv
import re
from bs4 import BeautifulSoup

# 读取 HTML 文件
with open('test.html', 'r', encoding='utf-8') as file:
    content = file.read()

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(content, 'html.parser')

# 找到所有带有 aria-label 属性的 div 标签
divs = soup.find_all('div', attrs={'aria-label': True})

# 初始化 CSV 数据
csv_data = []

# 遍历所有 div 标签
for div in divs:
    # 获取 aria-label 的值
    aria_label = div['aria-label']
    
    # 使用正则表达式分隔字符串，保留分隔符（即 ',' 和 '-'）
    values = re.split(r'[,-]+', aria_label)

    # 将提取到的值添加到 CSV 数据中
    csv_data.append(values)

# 将数据写入 CSV 文件
with open('output.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    
    # 写入 CSV 数据
    writer.writerows(csv_data)

print("数据已成功提取并保存到output.csv中！")
