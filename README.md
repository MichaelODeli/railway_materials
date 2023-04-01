# railway_materials
Several useful materials for railway projects

## `stations_parcer.ipynb`
### Информация о проекте
Выборка необходимой информации на основании данных из таблиц ЕСР   
Источник данных: http://osm.sbin.ru/esr/   
© Идея источника данных принадлежит [Sergey Gladilin](https://www.openstreetmap.org/user/Sergey%20Gladilin). Разработка и реализация - [Sergey Gladilin](https://www.openstreetmap.org/user/Sergey%20Gladilin) и [Alexandr Zeinalov](http://www.openstreetmap.org/user/Alexandr%20Zeinalov).   
Использовано по лицензии GNU GPLv3   
### Методы обработки
- [Pandas](https://github.com/MichaelODeli/railway_materials/blob/main/stations_parcer/stations_parcer.ipynb)
### Исходные файлы
- http://osm.sbin.ru/esr/esr.csv
- http://osm.sbin.ru/esr/osm2esr.csv
### Результирующий файл
- [CSV](https://github.com/MichaelODeli/railway_materials/blob/main/stations_parcer/RU_stations_new.csv)
### Предпросмотр файлов
- [Jupyter + Plotly](https://github.com/MichaelODeli/railway_materials/blob/main/stations_parcer/stations_parcer_mapview.ipynb)

## `stations_neighbourhood`
### Информация по проекту
- Соседство станций на основании документа "Тарифное руководство №4"
### Методы обработки
- Вручную, с помощью Microsoft Excel 365
### Исходные файлы
- [Тарифное руководство №4](https://sovetgt.org/tr4/2023/03/20/) (использована книга №1 для формирования соседства станций)
### Результирующий файл
- [CSV для СвЖД](https://github.com/MichaelODeli/railway_materials/blob/main/stations_neighbourhood/svzd_sosedi.csv)
- [CSV для всей ж/д РФ](https://github.com/MichaelODeli/railway_materials/blob/main/stations_neighbourhood/rzd_sosedi.csv)

## `svzd_graph`
### Информация по проекту
- Граф железных дорог СвЖД на основании OSMnx
### Методы обработки
- [Экспорт графа с OSMnx](https://github.com/MichaelODeli/railway_materials/blob/main/svzd_graph/make_svzd_graphs.py)
### Результирующий файл (*.graphml)
- [Полный граф для СвЖД (нужно распаковать)](https://github.com/MichaelODeli/railway_materials/blob/main/svzd_graph/full_svzd_graph.graphml.zip)
- [Упрощенный граф для СвЖД](https://github.com/MichaelODeli/railway_materials/blob/main/svzd_graph/simple_svzd_graph.graphml)
