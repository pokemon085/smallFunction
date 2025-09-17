#rem and map color function

import re
from colorMap import baseColor, backgroundColor  # 匯入色碼對應表

# 顏色處理類別
class ColorProcessor:
    def __init__(self, baseColor=baseColor, backgroundColor=backgroundColor):
        self.baseColor = baseColor
        self.backgroundColor = backgroundColor
        #取得色碼
        self.color_regex = r'#([a-fA-F0-9]{3,6})'

    def replace_color(self, match, property_name):
        color_code = f"#{match.group(1).lower()}"
        if property_name in ['color','fill']:
            # 查詢 baseColor 對照表
            return self.baseColor.get(color_code, color_code)
        elif property_name in ['background-color', 'background']:
            # 查詢 backgroundColor 對照表
            return self.backgroundColor.get(color_code, color_code)
        else:
            # 如果屬性名稱不匹配，返回原色碼
            return color_code

    def process_css_line(self, line):
        if 'color:' in line:
            property_name = 'color'
        elif 'background-color:' in line:
            property_name = 'background-color'
        elif 'background:' in line:
            property_name = 'background'
        elif 'fill' in line:
            property_name = 'fill'
        else:
            return line  # 如果沒有找到相關屬性，返回原行

        # 替換色碼
        return re.sub(self.color_regex, lambda match: self.replace_color(match, property_name), line)


# px to rem
# 單位轉換類別
class UnitConverter:
    def __init__(self, base = 14):
        self.base = base

    def px_to_rem(self,value):
        rem_value = round((float(value) / self.base),2)
        if rem_value.is_integer():
            return str(int(rem_value))+'rem'
        return str(rem_value)+'rem'


    def lineHandler(self,css_string):
        if css_string.strip().startswith(('border-radius', 'border', 'filter')):
            return css_string

        pattern = re.compile(r'(\d+(\.\d+)?)px')
        return pattern.sub(lambda match: self.px_to_rem(match.group(1)), css_string)

