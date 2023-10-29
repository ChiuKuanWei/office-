import pandas as pd # load 數據很好用的工具包
import numpy as np # 數值運算的工具包
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


#---------------------------------------------------------以三天為單位，計算收盤價的移動平均-----------------------------------------------------------------------

# root = tk.Tk()
# root.withdraw()

# # 使用filedialog来选择文件
# file_path = filedialog.askopenfilename()

# if file_path:
#     df = pd.read_csv(file_path, encoding = 'utf-8')

#     # 計算收盤價的移動平均線  
#     # 數據:[1,2,3,4,5,6] , slide_wildow = 3 [[1,2,3 的平均],[2,3,4的平均],...]
#     # 方法一: 使用邏輯寫法去拼湊移動平均
#     df_close = df['收盤價']
#     my_data = df_close.values.tolist()
#     #print(my_data)
#     slide_wildow = 3 #以三天為單位，計算收盤價的移動平均
#     # step = 1
#     # my_data_roll = []
#     # for idx , v in enumerate(my_data):
#     #     if (idx + 1) >= slide_wildow :
#     #         w_data = my_data[idx-slide_wildow+step:idx+step]
#     #         w_data_mean = np.array(w_data).mean() #計算陣列元素裡的平均
#     #         my_data_roll.append(w_data_mean)
#     #         #print(my_data_roll)
#     #     else:
#     #         my_data_roll.append('None')
#     # len(my_data_roll)    
#     # round(my_data_roll[2],2)
#     # my_data_roll = [round(i,2) if type(i)!=str else 'NaN' for i in my_data_roll] 
#     #每走過my_data_roll每個元素,元素都要判斷!=str ,如果條件成立 直接回傳round(i,2), 否則回傳'NaN'
#     #df['slide_mean'] = my_data_roll # 把移動平均灌回指定欄位(若這個欄位沒有,就會自己創一個新的延伸欄位)

#     df['Slide_Mean'] = df_close.rolling(window=slide_wildow).mean() #此函示為計算收盤價的移動平均，把移動平均傳回指定欄位(若這個欄位沒有,就會自己創一個新的延伸欄位)

#     # 將空值顯示為"NULL"，inplace=True 參數用於在原有DataFrame上進行修改，而不返回新的DataFrame。如果不使用 inplace=True，則需要將修改後的結果賦值給新的欄位。
#     df['Slide_Mean'].fillna('NULL', inplace=True)

#     # 將每個平均值只保留小數點後兩位
#     # apply(): apply 方法用於應用一個函數到 DataFrame 的每一個元素。在這裡，我們將使用 lambda 函數來格式化每個 "Slide_Mean" 的值。
#     # apply()方法通常適用於 DataFrame 中的元素級別的操作，而這裡的 apply 方法對每個單獨的 "Slide_Mean" 的值進行了格式化，並將結果重新賦值給 "Slide_Mean" 欄位，這樣就完成了格式化的操作
#     # lambda x: '{:.2f}'.format(x) if x != 'NULL' else x: 這是一個 lambda 函數，它用於對 "Slide_Mean" 的每個元素進行格式化。
#     # lambda x:: 宣告了一個匿名函數，這個函數的參數是 x。
#     # '{:.2f}'.format(x): 這部分表示將 x 轉換為浮點數，並且保留兩位小數。
#     # if x != 'NULL' else x: 這是條件表達式 (ternary expression)，如果 x 不等於 'NULL'，則將 x 格式化為浮點數，否則保持 x 不變
#     df['Slide_Mean'] = df['Slide_Mean'].apply(lambda x: '{:.2f}'.format(x) if x != 'NULL' else x)

#     # 顯示讀取的DataFrame
#     print(df.to_string(index=False))
#     # 顯示row colums總數
#     print(df.shape)

#     file_excelpath = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[("Excel Files", ('*.xls', '*.xlsx'))], title='儲存位置')

#     if file_excelpath:  
#         # 判斷使用者選擇的副檔名，並將 DataFrame 儲存至相應的 Excel 檔案
#         if file_excelpath.split('.')[1] == 'xlsx':
#             df.to_excel(file_excelpath, index=False, engine='openpyxl')
#         else:  
#             df.to_excel(file_excelpath, index=False)
#         print(f'資料已儲存至文字檔：{file_excelpath}')

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------計算收盤價的移動平均，畫曲線圖-------------------------------------------------------------------------

my_font = fm.FontProperties(fname = './字體包/NotoSansTC-Black.otf') # 設定字體路徑

# win10
#plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False # 這行禁用了將減號（-）渲染為Unicode減號而不是連字符。這是必要的，因為有些字體可能不包含Unicode減號，這可能會導致繪圖中的顯示問題

#region 基本圖表範例
x = [1,3,5,7,5] # 定義一個 x 軸的數值陣列
fig = plt.figure() # 創建一個繪圖的 figure 物件
plt.plot(x) # 繪製線圖
# 設定 fontproperties 參數，指定字型
plt.title('這是圖表', fontproperties=my_font, fontsize=20)
plt.show()
#endregion

class df_plt:
    def __init__(self,csv_path='./stocks/stock_1.csv', window_size=3,target_column ='收盤價',save_path = './plot.jpg'):# __init__是固定寫法
        self.csv_path = csv_path
        self.window_size = window_size
        self.target_column = target_column
        self.save_path = save_path
    def df_generator(self):
        df = pd.read_csv(self.csv_path, encoding = 'utf-8')
        pd_roll = df[self.target_column].rolling(self.window_size).mean()
        def data_fliter(data):
            if type(data)!=str:
                return round(data,3)
            else:
                return data
        df[f'MA_{self.window_size}'] = pd_roll    
        df[f'MA_{self.window_size}'] = df[f'MA_{self.window_size}'].apply(data_fliter)  
        return df
    def plot(self):
#          ==========畫圖============
        df =self.df_generator()
        y1 = df[self.target_column].values.tolist()
        y2 = df[f'MA_{self.window_size}'].values.tolist()
        x = list(range(len(y1)))

        plt.figure(figsize=(10,5)) # 準備一張畫布
        # 添加圖層畫圖
        plt.plot(x,y1,
                 color='blue',
                 linestyle = '-',
                 linewidth = 1,
                 label = 'Close')
        plt.plot(x,y2,
                 color='green',
                 linestyle = '--',
                 linewidth = 1,
                 label = f'MA_{self.window_size}')
        plt.legend(loc = 'best')
        plt.xlabel('天數')
        plt.ylabel('收盤價')
        plt.xticks(rotation = -20)
        plt.title(f'close / MA{self.window_size} plot')
        plt.savefig(self.save_path)
        plt.show()
    def plot_bar(self):
        df =self.df_generator()
        y1 = df[self.target_column].values.tolist()
        x = list(range(len(y1)))
        plt.figure(figsize=(10,5)) # 準備一張畫布
        # 添加圖層畫圖
        plt.bar(x,y1,
                 color='blue',
                 linewidth = 1,
                 label = 'Close')
        plt.show()
    
DF_PLT= df_plt(csv_path='./stocks/stock_1.csv', 
               window_size=30,
               target_column ='收盤價',
               save_path = './plot.jpg')   
df = DF_PLT.df_generator()
df
DF_PLT.plot_bar()


# ------------------------------------------------------------------------------------------------------------------------------------------------------------