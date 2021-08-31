from diagrams import Diagram, Cluster
from nodes import (
    ATK_2P,
    ATK_5P,
    ATK_2K,
    ATK_5K,
    ATK_2D,
    ATK_5D,
    ATK_2H,
    ATK_5H,
    ATK_2S,
    ATK_cS,
    ATK_fS,
    ATK_R6
)


graph_attrs = {
    'padding': '0',
    'layout': 'dot',
    'concentrate': 'true',
    'ranksep': '1',
    'nodesep': '1',
}

with Diagram(show=False, filename="combo_chart", graph_attr=graph_attrs):

    with Cluster("P") as cluster_atk_P:
        atk_2P = ATK_2P()
        atk_5P = ATK_5P()

        group_atk_P = [
            atk_2P,
            atk_5P
        ]

    with Cluster("K") as cluster_atk_K:
        atk_2K = ATK_2K()
        atk_5K = ATK_5K()

        group_atk_K = [
            atk_2K,
            atk_5K
        ]

    with Cluster("D") as cluster_atk_D:
        atk_2D = ATK_2D()
        atk_5D = ATK_5D()

        group_atk_D = [
            atk_2D,
            atk_5D
        ]

    with Cluster("H") as cluster_atk_H:
        atk_2H = ATK_2H()
        atk_5H = ATK_5H()

        group_atk_H = [
            atk_2H,
            atk_5H
        ]

    with Cluster("S") as cluster_atk_S:
        atk_2S = ATK_2S()
        atk_fS = ATK_fS()

        group_atk_S = [
            atk_2S,
            atk_fS
        ]

    atk_cS = ATK_cS()

    atk_R6 = ATK_R6()

    atk_2P >> atk_5P >> atk_2P

    group_atk_P >> atk_R6
    group_atk_K >> atk_R6 << group_atk_H
    group_atk_D >> atk_R6 << group_atk_S

    atk_cS >> atk_R6
    group_atk_S >> atk_cS << group_atk_D
    group_atk_H >> atk_cS

    group_atk_K >> atk_5D
    group_atk_K >> atk_2D
