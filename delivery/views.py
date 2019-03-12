from django.shortcuts import render
from django.http import JsonResponse
from . import delivery_cost
from . import calculate_distance
def index(request):
	sol = delivery_cost.Solution()
	graph = calculate_distance.create_distance_graph()
	length  = len(graph)
	for i in range(0,length):
		sol.addEdge(graph[i][0],graph[i][1],graph[i][2])	
	answer = sol.solve(length-1,graph)
	return JsonResponse({"Solution Approach":"Used minimum spanning tree algo to solve the given problem","Shortest Distance covered by    		       delivery boy":answer},safe=False)
