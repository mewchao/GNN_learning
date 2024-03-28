import numpy
import pandas as pd
import networkx as nx


def print_graph():
    edges=pd.DataFrame()
    edges['source']=  [1,1,1,2,2,3,3,4,4,5,5,5]
    edges['target']=  [2,4,5,3,1,2,5,1,5,1,3,4]
    edges['weights']= [1,1,1,1,1,1,1,1,1,1,1,1]

    G=nx.from_pandas_edgelist(edges,source='source',target='target',edge_attr='weights')
    # 度数
    print(nx.degree(G))
    # 连通分量
    print(list(nx.connected_components(G)))
    # 图直径
    print(nx.diameter(G))
    # 度中心性
    print(nx.degree_centrality(G))
    # 特征向量中心性
    print(nx.eigenvector_centrality(G))
    # Between Centrality 中介中心性
    print(nx.betweenness_centrality(G))
    # closeness 紧密中心性
    print(nx.closeness_centrality(G))
    # pagerank()
    print(nx.pagerank(G))
    # HITS  HITS hubs and authorities values
    print(nx.hits(G))