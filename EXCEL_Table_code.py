
#region 取list平均值 平方 開根號

# def lot_mean_std(data_list):
#     #============取list平均值================
#     sum_ = 0
#     for i in data_list:
#         try:
#             l = int(str(i).replace(',',''))
#             sum_ = sum_ + l
#         except Exception as e:
#             print(f'錯誤訊息:{e}')  

#     meam = sum_/len(data_list)
#     #============取平方與開根號的值=================
#     std_ = 0
#     for j in data_list:

#         try:
#             j = int(str(j).replace(',',''))
#             d = (j-meam)**2 #**2為平方值
#             std_ = std_+d
#         except Exception as e:
#             print(f'錯誤訊息:{e}')

#     std_ = (std_/len(data_list))**0.5 #**0.5為開根號
#     return meam,std_

# def data_filter(data_list,th,d= 'up'): # data_filter(list的數據, 閥值, 閥值以上或以下='up' or 'down')
#     filter_list = []
#     for i in data_list:
#         if d =='up':# 當方法是以up 為條件下,再去過濾每一個i 是否大於th 
#             if i>th: # 數據確定是我要的
#                 filter_list.append(i)
#         if d =='down':# 當方法是以up 為條件下,再去過濾每一個i 是否大於th 
#             if i<th: # 數據確定是我要的
#                 filter_list.append(i)
#     meam,std_ = lot_mean_std(filter_list)            
#     return filter_list, meam,std_
        
# a = [1,2,3,4,5]
# filter_list, meam,std_ = data_filter(a,1,d = 'up')
# print(f'取條件符合的list:{filter_list},list平均值:{meam},開根號:{std_}')

#endregion


#region 畫EXCEL圖表 參考文獻搜尋:matplotlib
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)

# --------------------------設置圖表背景(漸變色)------------------------------
#direction: 漸變方向，取值範圍為 [0, 1]，默認值為 0.3。它決定了漸變的方向，0 表示水平漸變，0.5 表示對角漸變，1 表示垂直漸變。
#cmap_range: 顏色映射範圍，指定漸變的顏色範圍，默認值為 (0, 1)。它控制了漸變顏色的起始值和結束值。
#**kwargs: 其他關鍵字參數，用於傳遞給 imshow() 函數的其他參數。
def gradient_image(ax, direction=0.3, cmap_range=(0, 1), **kwargs):
    #計算了 phi，即漸層方向的角度（弧度表示）。然後使用 np.array() 函數建立一個二維陣列 v，它是漸層方向的單位向量。
    phi = direction * np.pi / 2
    v = np.array([np.cos(phi), np.sin(phi)])
    #建立了一個 2x2 的陣列 X，用於表示漸層的顏色。@ 表示矩陣乘法（點積），[1, 0] 和 [1, 1] 是漸層的兩個端點，[0, 0] 和 [0, 1] 是另一個端點。
    X = np.array([[v @ [1, 0], v @ [1, 1]],
                  [v @ [0, 0], v @ [0, 1]]])
    #調整了 X 中的值，以控制漸層顏色的範圍。將漸層的起始值調整為 a，將漸層的結束值調整為 b。
    a, b = cmap_range
    X = a + (b - a) / X.max() * X
    #X 是要繪製的圖像數據，interpolation='bicubic' 指定了插值方法，clim=(0, 1) 指定了色彩範圍為 [0, 1]，aspect='auto' 表示將圖像的長寬比例設定為自動調整。
    # **kwargs 是其他關鍵字參數，用於傳遞其他繪圖參數。
    im = ax.imshow(X, interpolation='bicubic', clim=(0, 1),
                   aspect='auto', **kwargs)
    return im
# ---------------------------------------------------------------------------

# x: 這是一個包含每個長方形的左邊緣 x 座標的數值陣列。這些數值決定了每個長方形在 x 軸上的位置。
# y: 這是一個包含每個長方形高度的數值陣列。這些數值決定了每個長方形的高度。
# width: 長方形的寬度。默認值為 0.5。
# bottom: 長方形的底部 y 座標。默認值為 0，意味著所有的長方形的底部都在 y 軸的 0 位置
def gradient_bar(ax, x, y, width=0.5, bottom=0):
    for left, top in zip(x, y):
        right = left + width
        gradient_image(ax, extent=(left, right, bottom, top),
                       cmap=plt.cm.Blues_r, cmap_range=(0, 0.8))

#用來建立一個新的圖表（Figure）以及座標軸（Axes）
fig, ax = plt.subplots()
#設定座標軸的範圍
ax.set(xlim=(1, 11), ylim=(0, 25))
ax.set_xticks(range(1, 11)) #設定 x 軸的刻度位置為從 1 到 10
ax.set_xticklabels(range(1, 11)) #將刻度標籤設定為對應的數字
ax.set_xlabel('item') #x軸內容描述
ax.set_ylabel('values') #y軸內容描述
#direction=1: 指定漸層的方向，這裡為垂直漸層。
#extent=(0, 1, 0, 1): 指定漸層圖像的位置和大小，這裡左下角座標為 (0, 0)，右上角座標為 (1, 1)，代表整個 ax 區域。
# transform=ax.transAxes: 指定漸層圖像的座標系，這裡 ax.transAxes 表示相對於 ax 的坐標系，也就是以 ax 的左下角為原點，右上角為 (1, 1)。
# cmap=plt.cm.RdYlGn: 指定漸層的顏色映射，這裡使用了紅黃綠三種顏色的映射。
# cmap_range=(0.2, 0.8): 指定漸層顏色的範圍，將漸層的起始值調整為 0.2，將漸層的結束值調整為 0.8。
# alpha=0.5: 指定漸層圖像的透明度，這裡設置為 0.5，即半透明。
gradient_image(ax, direction=1, extent=(0, 1, 0, 1), transform=ax.transAxes,
               cmap=plt.cm.Wistia, cmap_range=(0.2, 0.8), alpha=0.5)


#np.arange 是 NumPy（數值Python）庫中的一個函式，用於創建一個數值序列（array）
#範例:sequence1 = np.arange(4) print(sequence1)  # 輸出: [0 1 2 3]
#     創建一個包含 2 到 10（不包含 10）的數值序列，間隔為2     sequence2 = np.arange(2, 10, 2)  print(sequence2)  # 輸出: [2 4 6 8]

#start: 序列的起始值（包含在序列內），默認值為 0。
#stop: 序列的結束值（不包含在序列內）。
#step: 序列中每個元素之間的間隔（增量），默認值為 1。
#dtype: 設定生成的陣列的數據類型，默認值為 None，這將使 NumPy 根據輸入數據的類型自動選擇。
x = np.arange(1, 11, 1) + 0.15

y = []
for i in range(10,20):
    y.append(i)

#y = np.random.rand(10) 生成隨機數，用途是生成10個在區間 [0, 1] 內均勻分佈的隨機數所構成的一維陣列
gradient_bar(ax, x, y, width=0.7)
plt.show()

#endregion

#Streamlit是特別設計給機器學習與資料科學的開源框架 
#參考文獻 : https://medium.com/@yt.chen/%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E8%B3%87%E6%96%99%E7%A7%91%E5%AD%B8%E6%A1%86%E6%9E%B6%E6%87%89%E7%94%A8-streamlit%E5%85%A5%E9%96%80-1-d07478cd4d8

