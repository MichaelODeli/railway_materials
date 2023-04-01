# импорт библиотек
import osmnx as ox
# определение параметров
ox.settings.log_console=True
ox.settings.max_query_area_size=50000000000

# Загрузка геометрии дл упрощенного графа
ox.settings.useful_tags_way += ["railway"]
G = ox.graph_from_place(
    "Свердловская область, Россия",
    retain_all=False,
    truncate_by_edge=True,
    simplify=True,
    custom_filter='["railway"]',
)
# сохранение графа в файл
ox.save_graphml(G, "simple_svzd_graph.graphml")

# Загрузка геометрии для полного графа
ox.settings.useful_tags_way += ["railway"]
G_full = ox.graph_from_place(
    "Свердловская область, Россия",
    retain_all=False,
    truncate_by_edge=True,
    simplify=False,
    custom_filter='["railway"]',
)
# сохранение графа в файл
ox.save_graphml(G_full, "full_svzd_graph.graphml")