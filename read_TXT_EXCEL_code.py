#將py檔轉成exe，參考文獻:https://pypi.org/project/auto-py-to-exe/   開啟執行檔指令:"auto-py-to-exe"
import tkinter as tk
from tkinter import filedialog #tkinter為模組 filedialog:是指從指定的 module_name 模組中導入的要使用的函數名稱，可以直接使用要使用的函數，而不需要寫明模組名
import pandas as pd
import json
import re

#-----------------------------------------------------開啟 讀取TXT or EXCEL(內容轉到文字檔裡)-----------------------------------------------------
def open_file():
    # 创建一个Tkinter根窗口，不会显示出来
    root = tk.Tk()
    root.withdraw()

    # 使用filedialog来选择文件
    file_path = filedialog.askopenfilename()

    if file_path:
        # 获取文件后缀名
        file_extension = file_path.split('.')[1].lower()

        if file_extension == 'txt':
            # 如果是txt文件，使用open()函数读取内容
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    print(content)
                file.close() #釋放文件
            except Exception as e:
                print(f"無法讀取文件：{str(e)}")

        elif file_extension in ['xls', 'xlsx']:
            # 如果是Excel文件，使用pandas库读取内容
            try:
                #讀取EXCEL內容時，需pip install openpyxl
                df = pd.read_excel(file_path)

                # 將 DataFrame 轉換為格式化的字串
                formatted_data = df.to_string(index=False)

                #刪除不必要的內容 type=set
                str_replace = {'Unnamed: 0','Unnamed: 2','Unnamed: 3','NaN'}
                for a in str_replace:
                    formatted_data = formatted_data.replace(a,'')

                #EXCEL內容轉換到文字檔裡
                array_formatted_data = formatted_data.split('\n')
                formatted_data = '' #抓取每列處理完的內容總攬
                array_colums = [] #取得欄位總攬
                for i, line in enumerate(array_formatted_data):
                    if i == 4:
                        array_colums = re.sub(r'\s+', ' ', line).strip().split(' ') #strip() 為去除頭尾空白   re.sub = replace
                        continue
                    elif i > 3 and i < len(array_formatted_data)-3: 
                        item_count = 0 #計數欄位取到哪
                        get_process_data = '' #取得處理後的data             
                        str = re.sub(r'\s+', ' ', line).strip()
                        array_str = str.split(' ')                           
                        for j, data in enumerate(array_str):
                            if j > 0 and j < len(array_str)-2: #len(array_str)-2 目的為抓取完整的產品名稱
                                if j == 1:
                                    get_process_data += array_colums[item_count] + ':' + data + ' '
                                    item_count += 1
                                else:
                                    get_process_data += data + ' '
                            else:
                                get_process_data += array_colums[item_count] + ':' + data + ' '
                                item_count += 1

                        formatted_data += get_process_data + '\n\n'
                    else:
                        # 使用正則表達式將多個連續空白取代成一個空白
                        formatted_data += re.sub(r'\s+', ' ', line).strip() + '\n'

                file_txtpath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")], title='儲存位置')

                if file_txtpath:
                    # 將格式化的字串寫入文字檔
                    with open(file_txtpath, 'w', encoding='utf-8') as txt_file:
                        txt_file.write(formatted_data)

                    print(f'資料已儲存至文字檔：{file_txtpath}')

                #orient='records'表示每行作為一個JSON對象，indent=2表示縮進為2個空格。
                # 然後，我們使用json.loads()將JSON字符串解析為Python數據結構，並使用json.dumps()對其進行格式化，再使用print()打印出整齊的JSON內容。

                # 將DataFrame轉為JSON格式字符串
                # json_str = df.to_json(orient='records', indent=2)
                # # 使用json.dumps()對JSON字符串進行格式化
                # formatted_json = json.dumps(json.loads(json_str), ensure_ascii=False, indent=2)
                # print(formatted_json)
            except Exception as e:
                print(f"無法讀取Excel文件：{str(e)}")

        else:
            print("不支持的文件格式")


open_file()
# ----------------------------------------------------------------------------------------------------------------------------------------------------




#-----------------------------------------------------------計算List元素裡平均值-----------------------------------------------------------------------

# def mean_cal(data_list):
#     sum = 0
#     for i in data_list:
#         sum += i
    
#     if sum == 0:
#         print(f'{data_list} 平均值為0')
#         return False
#     else:
#         return sum / len(data_list)

#     # for i in data_list:
#     #     if type(i) == int or type(i) == float:
#     #         sum += i
#     #     else:
#     #         print(f'請輸入int or float格式，不規則變數為{i}，', type(i))
#     #         return False
    


# def create_list(list_len):
#     my_list = []
#     p = True
#     while p is True:
#         try:
#             num = int(input(f'請輸入數字{len(my_list) + 1}/{list_len}:'))
#             my_list.append(num)
#             if len(my_list) == list_len:
#                 p = False
#         except Exception as e:
#             error_message = str(e)
#             print("抓取到异常：", error_message)
#             return None

#     return my_list


# input_num = create_list(3)
# if input_num is not None:    
#     mean = mean_cal(input_num)
#     if mean is not False:
#         print(f'list={input_num}，平均值:{mean}')

# input() # 等待用户按下回车键   
# ---------------------------------------------------------------------------------------------------------------------------------------- 