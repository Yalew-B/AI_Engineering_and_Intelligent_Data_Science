"""Common graph traversal, shortest-path, and ordering algorithms.

Unweighted functions expect ``{node: iterable_of_neighbors}``. Weighted
functions expect ``{node: iterable_of_(neighbor, weight)_pairs}``.
"""

from collections import deque
from heapq import heappop, heappush
from itertools import count
from math import inf


class NegativeCycleError(ValueError):
	"""Raised when Bellman-Ford detects a reachable negative-weight cycle."""


class GraphCycleError(ValueError):
	"""Raised when topological sorting is attempted on a cyclic graph."""


def breadth_first_search(graph, start):
	"""Return nodes reachable from ``start`` in breadth-first order."""
	visited = {start}
	queue = deque([start])
	order = []
	while queue:
		node = queue.popleft()
		order.append(node)
		for neighbor in graph.get(node, ()):
			if neighbor not in visited:
				visited.add(neighbor)
				queue.append(neighbor)
	return order


def depth_first_search(graph, start):
	"""Return nodes reachable from ``start`` in depth-first order."""
	visited = set()
	order = []
	stack = [start]
	while stack:
		node = stack.pop()
		if node in visited:
			continue
		visited.add(node)
		order.append(node)
		# Reverse neighbors so traversal follows their given order.
		stack.extend(reversed(tuple(graph.get(node, ()))))
	return order


def dijkstra(graph, start):
	"""Return shortest distances from ``start`` for nonnegative weights.

	Raises ``ValueError`` if a reachable edge has a negative weight. Nodes
	unreachable from ``start`` are omitted.
	"""
	distances = {start: 0}
	sequence = count()
	queue = [(0, next(sequence), start)]
	while queue:
		distance, _, node = heappop(queue)
		if distance != distances[node]:
			continue
		for neighbor, weight in graph.get(node, ()):
			if weight < 0:
				raise ValueError("Dijkstra's algorithm requires nonnegative weights")
			candidate = distance + weight
			if candidate < distances.get(neighbor, inf):
				distances[neighbor] = candidate
				heappush(queue, (candidate, next(sequence), neighbor))
	return distances


def bellman_ford(graph, start):
	"""Return shortest distances from ``start``, allowing negative weights.

	Raises ``NegativeCycleError`` when a negative cycle is reachable from the
	start node. Unreachable nodes are omitted from the result.
	"""
	nodes = set(graph)
	edges = []
	for source, neighbors in graph.items():
		for target, weight in neighbors:
			nodes.add(target)
			edges.append((source, target, weight))

	distances = {node: inf for node in nodes}
	distances[start] = 0
	for _ in range(max(0, len(nodes) - 1)):
		changed = False
		for source, target, weight in edges:
			if distances[source] != inf and distances[source] + weight < distances[target]:
				distances[target] = distances[source] + weight
				changed = True
		if not changed:
			break

	for source, target, weight in edges:
		if distances[source] != inf and distances[source] + weight < distances[target]:
			raise NegativeCycleError("reachable negative-weight cycle")
	return {node: distance for node, distance in distances.items() if distance != inf}


def topological_sort(graph):
	"""Return a topological ordering of a directed acyclic graph."""
	indegree = {node: 0 for node in graph}
	for neighbors in graph.values():
		for neighbor in neighbors:
			indegree.setdefault(neighbor, 0)
			indegree[neighbor] += 1

	queue = deque(node for node, degree in indegree.items() if degree == 0)
	order = []
	while queue:
		node = queue.popleft()
		order.append(node)
		for neighbor in graph.get(node, ()):
			indegree[neighbor] -= 1
			if indegree[neighbor] == 0:
				queue.append(neighbor)

	if len(order) != len(indegree):
		raise GraphCycleError("graph contains a directed cycle")
	return order

