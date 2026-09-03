
edges =[[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]

# 주는 edges 자체가 adjacent list

# 세 개 이상과 연결된 경우 고려할 필요 없음.
# 왜냐면 기존 리스트에서 둘 이상 연결되지 않음.
# 둘 이하인 경우 두 개 이상으로 뻗은 아이 중에 돌아오지 않는 아이
from itertools import chain
from enum import Enum                   
class Graphtype(Enum):
    line = 1
    donut = 2
    eight = 3

def to_delete(edges: list[list[int, int]]) -> int:
    N = max(list(chain.from_iterable(edges)))
    in_edges = [0] * (N + 1)
    out_edges = [0] * (N + 1)
    for edge in edges:
        a, b = edge[0], edge[1]
        out_edges[a] += 1
        in_edges[b] += 1

    if max(out_edges) > 2:
        to_delete = out_edges.index(max(out_edges))
    else:
        to_delete = [i for i in range(1, N+1) if out_edges[i]==2 and in_edges[i]==0][0]

    return to_delete


def graph_type(edges):
    '''
    그래프가 완전히 분리되었을 때 사용 가능
    '''
    n_vertex = len(list(set(chain.from_iterable(edges))))
    n_edge = len(edges)
    match n_vertex - n_edge:
        case 1:
            return Graphtype.line
        case 0:
            return Graphtype.donut
        case -1:
            return Graphtype.eight
        case _:
            raise Exception("뭔가 문제 있음")

# edge 리스트가 주어졌을 때 연결된 edge끼리 가져올 수 있어야 한다.


# 아 업데이트가 되지 않을 때까지 계속 갱신해야 하는구나.
def separate_edges(edges):
    ret = []
    while len(edges) > 0:
        (a, b) = edges.pop(0)
        temp = [[a, b]]
        vertices = set([a, b])
        x = len(temp)
        while True:
            for edge in edges[:]:
                if edge[0] in vertices:
                    temp.append(edge)
                    vertices.update(edge)
                    edges.remove(edge)
            if len(temp) == x: break
            else: x = len(temp)
        ret.append(temp)

    return ret

def solution(edges):
    to_del = to_delete(edges)
    donut = 0; line = 0; eight = 0
    search = [edge for edge in edges if to_del != edge[0] and to_del != edge[1]]
    graphs = separate_edges(search)
    print(graphs)
    for gr in graphs:
        match graph_type(gr):
            case Graphtype.donut:
                donut += 1
            case Graphtype.eight:
                eight += 1
            case Graphtype.line:
                line += 1

    n_vertex = len(set(chain.from_iterable(edges)))
    line += n_vertex - len(set(chain.from_iterable(chain.from_iterable(graphs)))) - 1
    return [to_del, donut, line, eight]

print(solution(edges))

# 와 씨발 예외 케이스 개많네
# n = 1짜리 도넛은 아예 간선이 안잡혀서 따로 잡아야 함..

    




