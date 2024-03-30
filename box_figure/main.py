import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import collections

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

    # Series类型的数据 其中包含唯一值的计数。
    # 这个Series对象的索引是唯一值，值是它们出现的频数
    merged_counts0 = excel_data0['Local Arr Time'].value_counts()
    merged_counts1 = excel_data1['Local Arr Time'].value_counts()

    # 对 merged_counts 按照索引排序
    # merged_counts = merged_counts.sort_index()

    # 将 Series 对象转换为字典
    merged_counts_dict0 = merged_counts0.to_dict()
    merged_counts_dict1 = merged_counts1.to_dict()

    # 去掉键值中的小数点
    merged_counts_dict0 = {str(k).replace('.0', ''): v for k, v in merged_counts_dict0.items()}
    merged_counts_dict1 = {str(k).replace('.0', ''): v for k, v in merged_counts_dict1.items()}

    # 假设merged_counts_dict0是一个字典，其中的键值需要在前面补0确保为四位数
    merged_counts_dict0 = {k.zfill(4): v for k, v in merged_counts_dict0.items()}
    merged_counts_dict1 = {k.zfill(4): v for k, v in merged_counts_dict1.items()}

    # 将所有的键转换为字符串类型
    merged_counts_dict0 = {str(k): v for k, v in merged_counts_dict0.items()}
    merged_counts_dict1 = {str(k): v for k, v in merged_counts_dict1.items()}

    # 打印转换后的字典
    print(merged_counts_dict0)
    print(merged_counts_dict1)

    # 创建一个新的空字典用于存储处理后的结果
    processed_dict = {}

    # 遍历原始字典，将具有相同开头两个数字的键的值合并到新的键内
    for key, value in merged_counts_dict0.items():
        prefix = key[:2]  # 提取开头两个数字作为新的键
        if prefix in processed_dict:
            if isinstance(value, list):
                processed_dict[prefix].extend(value)
            else:
                processed_dict[prefix].append(value)  # 如果值不是列表，则将其作为单个元素添加到集合中
        else:
            if isinstance(value, list):
                processed_dict[prefix] = value
            else:
                processed_dict[prefix] = [value]  # 如果值不是列表，则创建一个包含单个元素的列表

    for key, value in merged_counts_dict1.items():
        prefix = key[:2]  # 提取开头两个数字作为新的键
        if prefix in processed_dict:
            if isinstance(value, list):
                processed_dict[prefix].extend(value)
            else:
                processed_dict[prefix].append(value)  # 如果值不是列表，则将其作为单个元素添加到集合中
        else:
            if isinstance(value, list):
                processed_dict[prefix] = value
            else:
                processed_dict[prefix] = [value]  # 如果值不是列表，则创建一个包含单个元素的列表

    # 打印处理后的结果
    print(processed_dict)

    # 使用OrderedDict按照索引排序
    processed_dict = collections.OrderedDict(sorted(processed_dict.items()))

    # 使用字典创建DataFrame
    df = pd.DataFrame({k: pd.Series(v) for k, v in processed_dict.items()})

    # 设置横坐标数字标签的大小
    plt.xticks(fontsize=10)
    # 添加标题
    plt.title('Boxplot')

    # 画箱线图
    df.boxplot()
    plt.show()


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    draw()