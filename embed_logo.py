
import base64

# 读取图片
with open(r'c:\Users\lenovo\Desktop\dlou\校徽.png', 'rb') as f:
    img_data = f.read()
    base64_data = base64.b64encode(img_data).decode('utf-8')

# 读取HTML
with open(r'c:\Users\lenovo\Desktop\dlou\新建 文本文档.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 替换src属性
old_src = 'src="校徽.png"'
new_src = f'src="data:image/png;base64,{base64_data}"'
html = html.replace(old_src, new_src)

# 写入HTML
with open(r'c:\Users\lenovo\Desktop\dlou\新建 文本文档.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Logo嵌入成功！')
