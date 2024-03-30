# 导入包
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# -------设置支持中文----------------------#
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置简黑字体
mpl.rcParams['axes.unicode_minus'] = False
# -------自定义坐标轴刻度格式----------------#


def draw():
    # 读取Excel文件，没有属性名
    excel_data = pd.read_excel(io="D:\excel\XIAMEN.xlsx", header=None)

    # 指定属性名列表
    column_names = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5', 'Column6']  # 用实际的属性名替换这些示例属性名

    # 将属性名赋给DataFrame
    excel_data.columns = column_names

    value_counts = excel_data['Column5'].value_counts()

    print(value_counts)

    # 频数数据
    wind_data = {
        '东北风3级': 214,
        '东北风4级': 156,
        '东南风2级': 103,
        '西南风3级': 100,
        '东北风2级': 75,
        '东风2级': 73,
        '西南风2级': 72,
        '东北风5级': 55,
        '东风3级': 54,
        '南风2级': 47,
        '南风3级': 26,
        '东南风1级': 20,
        '东南风3级': 13,
        '西南风4级': 10,
        '东北风1级': 10,
        '东北风微风': 8,
        '西南风1级': 7,
        '东风1级': 6,
        '东北风6级': 6,
        '西北风2级': 5,
        '西风2级': 4,
        '西北风1级': 4,
        '南风微风': 3,
        '北风2级': 3,
        '南风4级': 3,
        '南风1级': 2,
        '西北风3级': 2,
        '东风4级': 2,
        '北风3级': 2,
        '东南风4级': 2,
        '西南风微风': 2,
        '西风5级': 1,
        '东风微风': 1,
        '西风3级': 1,
        '北风1级': 1,
        '西风1级': 1,
        '西北风4级': 1
    }

    # 创建空的 DataFrame
    df = pd.DataFrame(index=['微风', '1级', '2级', '3级', '4级', '5级', '6级'],
                      columns=['E', 'NE', 'N', 'NW', 'W', 'SW', 'S', 'SE'])
    """
    N   S   E  W   NE  NW   SE   SW
微风  0   3   1  0    8   0    0    2
1级  1   2   6  1   10   4   20    7
2级  3  47  73  4   75   5  103   72
3级  2  26  54  1  214   2   13  100
4级  0   3   2  0  156   1    2   10
5级  0   0   0  1   55   0    0    0
6级  0   0   0  0    6   0    0    0
    """
    # 使用正则表达式填充 DataFrame
    for key, value in wind_data.items():
        match = re.match(r'(.+风)(\d+级|微风)', key)
        if match:
            direction = match.group(1)
            level = match.group(2)

            if direction == '东北风':
                direction = 'NE'
            elif direction == '东南风':
                direction = 'SE'
            elif direction == '西南风':
                direction = 'SW'
            elif direction == '西北风':
                direction = 'NW'
            elif direction == '东风':
                direction = 'E'
            elif direction == '南风':
                direction = 'S'
            elif direction == '西风':
                direction = 'W'
            elif direction == '北风':
                direction = 'N'

            df.loc[level, direction] = value
    # 填充缺失值为0
    df = df.fillna(0)
    print(df)

    N = 8  # 风速分布为8个方向
    theta = np.linspace(0, 2 * np.pi, N, endpoint=False)  # 获取8个方向的角度值
    # print('theta:')
    # # 该数组包含了从0到2π之间均匀间隔的角度值
    # print(theta)
    width = (np.pi) / N  # 绘制扇型的宽度，可以自行调整
    labels = list(df.columns)  # 自定义坐标标签为 N ，SN， ……

    # 开始绘图
    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, projection='polar')
    i = 1
    for idx in df.index:
        # 每一行绘制一个扇形
        # 使用loc选择整行或整列数据
        # selected_row = data.loc['X']  # 选择整行数据
        # selected_column = data.loc[:, 'A']  # 选择整列数据
        radii = df.loc[idx]  # 每一行数据
        # 每个条形的中心角度由 theta 决定，长度或高度由 radii 决定，宽度由 width 决定，
        # 底部位置由 bottom 决定，标签由 label 决定，刻度标签由 tick_label 决定。
        bars = ax.bar(theta, radii, width=width, bottom=0.0, label=idx, tick_label=labels, alpha=0.7, align='edge')
        # 打数据标注
        for bar, radius in zip(bars, radii):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height, f'{radius}', ha='center', va='bottom')

    plt.title('我的家乡-厦门-风玫瑰图示意图')
    plt.legend(loc=4, bbox_to_anchor=(1.15, -0.07))  # 将label显示出来， 并调整位置
    plt.show()

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    draw()
