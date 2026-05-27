
# -*- coding: utf-8 -*-
import base64

# 读取图片并编码
with open('校徽.png', 'rb') as img_file:
    img_data = img_file.read()
    base64_str = base64.b64encode(img_data).decode('utf-8')

# 构建data URL
data_url = f'data:image/png;base64,{base64_str}'

# 读取HTML
with open('新建 文本文档.html', 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

# 替换
html_content = html_content.replace('src="校徽.png"', f'src="{data_url}"')

# 保存
with open('新建 文本文档.html', 'w', encoding='utf-8') as html_file:
    html_file.write(html_content)

print('成功！')
