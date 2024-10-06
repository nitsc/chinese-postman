import networkx as nx
import matplotlib.pyplot as plt

# 创建图
def create_graph(num_nodes, edges):
    G = nx.Graph()

    # 添加用户输入的边
    G.add_edges_from(edges)
    
    return G

# 解决邮差问题，返回欧拉路径
def solve_postman_problem(G):
    if nx.is_eulerian(G):
        # 如果图是欧拉图，直接获取欧拉路径
        path = list(nx.eulerian_circuit(G))
    else:
        # 如果不是欧拉图，使用 networkx 的中国邮差问题算法
        path = list(nx.eulerian_circuit(nx.eulerize(G)))
    return path

# 可视化邮差问题的解决方案
def visualize_graph(G, path):
    pos = nx.spring_layout(G)  # 为图生成一个布局

    # 绘制节点和边
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10, font_weight='bold')
    nx.draw_networkx_edges(G, pos, edgelist=path, edge_color='r', width=2)

    plt.title("Postman Problem Visualization")
    plt.show()

# 打印最短路径
def print_shortest_path(G, source, target):
    try:
        shortest_path = nx.shortest_path(G, source=source, target=target)
        print(f"Shortest path from {source} to {target}: {shortest_path}")
    except nx.NetworkXNoPath:
        print(f"No path between {source} and {target}.")

# 用户输入图的点数和边
def get_user_input():
    # 输入节点数
    num_nodes = int(input("请输入节点数: "))
    
    # 输入边信息
    edges = []
    print(f"请输入边信息 (例如: 0 1 表示节点0和节点1之间有边):")
    while True:
        edge_input = input("输入一条边 (或按Enter键结束输入): ")
        if edge_input == "":
            break
        u, v = map(int, edge_input.split())
        edges.append((u, v))
    
    return num_nodes, edges

# 主程序
def main():
    num_nodes, edges = get_user_input()  # 获取用户输入
    G = create_graph(num_nodes, edges)  # 创建图
    path = solve_postman_problem(G)  # 解决邮差问题
    print("Eulerian Path or Circuit:", path)

    # 获取源节点和目标节点，打印最短路径
    source = int(input("请输入起点节点: "))
    target = int(input("请输入终点节点: "))
    print_shortest_path(G, source, target)

    visualize_graph(G, path)  # 可视化结果

if __name__ == "__main__":
    main()
