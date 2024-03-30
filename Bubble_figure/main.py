import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
def Bubble():
    # 导入数据
    midwest = pd.read_csv(r'./midwest_filter.csv')

    # 预设图像各种信息
    large = 22
    med = 16
    small = 12
    params = {'axes.titlesize': large,  # 子图上的标题字体大小
              'legend.fontsize': med,  # 图例的字体大小
              'figure.figsize': (med, small),  # 画布大小
              'axes.labelsize': med,  # 标签的字体大小
              'xtick.labelsize': med,  # x轴标尺的字体大小
              'ytick.labelsize': med,  # y轴标尺的字体大小
              'figure.titlesize': large}  # 整个画布的标题字体大小
    plt.rcParams.update(params)  # 设定各种默认属性
    plt.style.use('dark_background')  # 设置整体风格
    sns.set_style('white')  # 设置整体背景风格

    # 准备标签列表与颜色列表
    categories = np.unique(midwest['category'])
    colors = [plt.cm.tab10(i / float(len(categories) - 1)) for i in range(len(categories))]

    # 布置画布
    fig = plt.figure(figsize=(14, 8), dpi=120, facecolor='w', edgecolor='k')

    for i, category in enumerate(categories):
        plt.scatter('area', 'poptotal', data=midwest.loc[midwest.category == category, :]
                    , s=midwest.loc[midwest.category == category, 'percasian'] * 500  # 需要对比的属性
                    , c=np.array(colors[i]).reshape(1, -1)  # 点的颜色
                    , edgecolors=np.array(colors[i]).reshape(1, -1)  # 点的边缘颜色
                    , label=str(category)  # 标签
                    , alpha=0.7  # 透明度
                    , linewidths=.5)  # 点的边缘线的宽度

    # 装饰图像
    plt.gca().set(xlim=(0.0, 0.12), ylim=(0, 90000),
                  xlabel='Area', ylabel='Population')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.title('Bubble Plot Encircling', fontsize=22)

    lgnd = plt.legend(fontsize=12)
    plt.show()  # 显示图像


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    Bubble()
    # 列出可用的样式
    # print(plt.style.available)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
