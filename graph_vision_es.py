import graphviz as gv

graph_vision_es = gv.Digraph()

graph_vision_es.edge('Inicio', 'Cargar Modelo')
graph_vision_es.edge('Cargar Modelo', 'Preparar Imágenes', label='test.py')
graph_vision_es.edge('Preparar Imágenes', 'Detección en Imágenes')
graph_vision_es.edge('Detección en Imágenes', 'Guardar Resultados')
graph_vision_es.edge('Cargar Modelo', 'Detección en Tiempo Real', label='real_time.py')
graph_vision_es.edge('Detección en Tiempo Real', 'Análisis de Video en Vivo')
graph_vision_es.edge('Análisis de Video en Vivo', 'Alertas y Reportes')
graph_vision_es.edge('Guardar Resultados', 'Fin')
graph_vision_es.edge('Alertas y Reportes', 'Fin')
