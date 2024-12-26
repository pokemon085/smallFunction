import re
from colorMap import baseColor, backgroundColor  # 匯入色碼對應表

color_regex=r'#([a-fA-F0-9]{3,6})'

def replace_color(match,property_name):
    color_code = f"#{match.group(1).lower()}"
    if property_name in ['color']:
        # 查詢 baseColor 對照表
        return baseColor.get(color_code, color_code)
    elif property_name in ['background-color', 'background']:
        # 查詢 backgroundColor 對照表
        return backgroundColor.get(color_code, color_code)
    else:
        # 如果屬性名稱不匹配，返回原色碼
        return color_code

def process_css_line(line):
    print(line)
    if 'color:' in line:
        property_name = 'color'
    elif 'background-color:' in line:
        property_name = 'background-color'
    elif 'background:' in line:
        property_name = 'background'
    else:
        return line  # 如果沒有找到相關屬性，返回原行

    # 替換色碼
    return re.sub(color_regex, lambda match: replace_color(match, property_name), line)
    


path = 'text.txt'
output = 'output.txt'
output_file = open(output, 'w')
f = open(path, 'r')

for line in f.readlines():
    textTrim=line.strip()

    if len(textTrim)!=0:
        # 替換色碼
        result = process_css_line(textTrim)
        output_file.write(result + '\n')
        print(result)

f.close()
output_file.close()

