import graphviz as gv

graph_en = gv.Digraph()

graph_en.edge('Start', 'Load Model')
graph_en.edge('Load Model', 'Prepare Images', label='test.py')
graph_en.edge('Prepare Images', 'Detection on Images')
graph_en.edge('Detection on Images', 'Save Results')
graph_en.edge('Load Model', 'Real-Time Detection', label='real_time.py')
graph_en.edge('Real-Time Detection', 'Live Video Analysis')
graph_en.edge('Live Video Analysis', 'Alerts and Reporting')
graph_en.edge('Save Results', 'End')
graph_en.edge('Alerts and Reporting', 'End')

