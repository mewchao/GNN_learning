import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def draw():

    # 使用converters参数将Local Arr Time列的数据类型指定为字符串
    excel_data0 = pd.read_excel(io="D:\excel\Report_1711440558703_JobId2876809.xlsx", skiprows=24,
                               converters={'Local Arr Time': str})

    excel_data1 = pd.read_excel(io="D:\excel\Report_1711440473329_JobId2876805.xlsx", skiprows=24,
                               converters={'Local Arr Time': str})


    # 指定属性名列表
    column_names = ['Arr Airport Code', 'Arr Airport Name', 'Local Arr Time', 'Frequency', 'Time series']

    # 将属性名赋给DataFrame
    excel_data0.columns = column_names
    excel_data1.columns = column_names

    # 对时间进行归并统计
    excel_data0['Merged Time'] = excel_data0['Local Arr Time'].str[:2]  # 提取前两个数字作为归并依据
    merged_counts0 = excel_data0['Merged Time'].value_counts()

    # 对时间进行归并统计
    excel_data1['Merged Time'] = excel_data0['Local Arr Time'].str[:2]  # 提取前两个数字作为归并依据
    merged_counts1 = excel_data1['Merged Time'].value_counts()

    # 合并两个 merged_counts
    merged_counts = merged_counts0.add(merged_counts1, fill_value=0)

    # 对 merged_counts 按照索引排序
    merged_counts = merged_counts.sort_index()

    plt.hist(merged_counts.index, weights=merged_counts.values, bins=len(merged_counts),edgecolor="r", histtype="bar",alpha=0.5)
    # 添加数据标签

    for i, v in enumerate(merged_counts.values):
        plt.text(i, v + 5, str(v), ha='center', fontsize=7)

    print(excel_data0)

    print(merged_counts)

    plt.xlabel('Local Arr Time')
    plt.ylabel('Frequency')
    plt.title('Histogram of Arr and Dep')
    plt.show()


if __name__ == '__main__':
    draw()

