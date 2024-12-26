#顏色map
from allFunction import *

def run_color_script():
    path = 'text.txt'
    output = 'output.txt'
    output_file = open(output, 'w')
    f = open(path, 'r')

    for line in f.readlines():
        textTrim = line.strip()

        if len(textTrim) != 0:
            # 替換色碼
            result = ColorProcessor().process_css_line(textTrim)
            output_file.write(result + '\n')
            print(result)

    f.close()
    output_file.close()

