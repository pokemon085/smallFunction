# 從px轉rem
# input txt file output txt file
import re

def px_to_rem(value):
    base = 14
    rem_value = round((float(value) / base),2)
    if rem_value.is_integer():
        return str(int(rem_value))+'rem'
    return str(rem_value)+'rem'

def lineHandler(css_string):
    if line.strip().startswith(('border-radius', 'border', 'filter')):
        return line

    pattern = re.compile(r'(\d+(\.\d+)?)px')
    return pattern.sub(lambda match: px_to_rem(match.group(1)), css_string)


path = 'text.txt'
output = 'output.txt'
output_file = open(output, 'w')
f = open(path, 'r')

for line in f.readlines():
    textTrim=line.strip()

    if len(textTrim)!=0:
        result =lineHandler(textTrim)
        output_file.write(result + '\n')
        print(result)

f.close()
output_file.close()






