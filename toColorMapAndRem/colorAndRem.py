
#顏色對應加上轉rem 用在行動版
from allFunction import *

def run_main_script():
    path = 'text.txt'
    output = 'output.txt'
    output_file = open(output, 'w')
    f = open(path, 'r')

    for line in f.readlines():
        textTrim = line.strip()

        if len(textTrim) != 0:
            # 替換色碼
            colorToVal = ColorProcessor().process_css_line(textTrim)
            # to rem
            result= UnitConverter().lineHandler(colorToVal)
            output_file.write(result + '\n')
            print(result)

    f.close()
    output_file.close()