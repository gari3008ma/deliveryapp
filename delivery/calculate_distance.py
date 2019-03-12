from math import sin, cos, sqrt, atan2, radians
from . import location
# approximate radius of earth in km
def create_distance_graph():
	R = 6373.0
	Graph=[]
	graph = location.data
	for start in range(0,50):
		lat1 = graph[start][0]
		lon1 = graph[start][1]
		for end in range(start+1,50):
			lat2 = graph[end][0]
			lon2 = graph[end][1]
			dlon = lon2 - lon1
			dlat = lat2 - lat1
			a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
			c = 2 * atan2(sqrt(a), sqrt(1 - a))
			distance = R * c
			Graph.append([start+1,end+1,distance])
	return Graph
