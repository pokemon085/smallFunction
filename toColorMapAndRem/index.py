#css 文字檔 轉顏色對應 or rem加顏色對應
#使用方式 python3 index.py color or python3 index.py main
import sys
from colorMapFunction import run_color_script
from colorAndRem import run_main_script

def main():
  print(sys.argv) #['index.py','color']
  print(len(sys.argv)) #2
  if len(sys.argv) < 2: #代表沒有帶入後面參數
    return
  
  #檔案帶進來的參數
  script_name = sys.argv[1].lower()

  if script_name == "color":
      print("執行 colorMapFunction.py 腳本...")
      run_color_script()
  elif script_name == "main":
        print("執行 colorAndRem.py 腳本...")
        run_main_script()
  else:
      print(f"未知的參數：{script_name}")
      print("請使用以下之一：color 或 main")

if __name__ == "__main__":
    main()