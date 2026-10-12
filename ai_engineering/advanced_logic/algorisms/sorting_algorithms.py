
"""Common comparison-based sorting algorithms."""

from typing import TypeVar

T = TypeVar("T")


def bubble_sort(values: list[T]) -> list[T]:
	"""Return a sorted copy using bubble sort (O(n²))."""
	result = values.copy()
	for end in range(len(result) - 1, 0, -1):
		swapped = False
		for index in range(end):
			if result[index] > result[index + 1]:
				result[index], result[index + 1] = result[index + 1], result[index]
				swapped = True
		if not swapped:
			break
	return result


def selection_sort(values: list[T]) -> list[T]:
	"""Return a sorted copy using selection sort (O(n²))."""
	result = values.copy()
	for start in range(len(result)):
		smallest = min(range(start, len(result)), key=result.__getitem__)
		result[start], result[smallest] = result[smallest], result[start]
	return result


def insertion_sort(values: list[T]) -> list[T]:
	"""Return a sorted copy using stable insertion sort (O(n²))."""
	result = values.copy()
	for index in range(1, len(result)):
		item = result[index]
		position = index
		while position > 0 and result[position - 1] > item:
			result[position] = result[position - 1]
			position -= 1
		result[position] = item
	return result


def merge_sort(values: list[T]) -> list[T]:
	"""Return a sorted copy using stable merge sort (O(n log n))."""
	if len(values) < 2:
		return values.copy()
	middle = len(values) // 2
	left = merge_sort(values[:middle])
	right = merge_sort(values[middle:])
	merged: list[T] = []
	i = j = 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			merged.append(left[i])
			i += 1
		else:
			merged.append(right[j])
			j += 1
	merged.extend(left[i:])
	merged.extend(right[j:])
	return merged


def quick_sort(values: list[T]) -> list[T]:
	"""Return a sorted copy using quicksort (average O(n log n))."""
	if len(values) < 2:
		return values.copy()
	pivot = values[len(values) // 2]
	lower = [item for item in values if item < pivot]
	equal = [item for item in values if item == pivot]
	upper = [item for item in values if item > pivot]
	return quick_sort(lower) + equal + quick_sort(upper)


def heap_sort(values: list[T]) -> list[T]:
	"""Return a sorted copy using heap sort (O(n log n))."""
	result = values.copy()

	def sift_down(root: int, end: int) -> None:
		while 2 * root + 1 < end:
			child = 2 * root + 1
			if child + 1 < end and result[child] < result[child + 1]:
				child += 1
			if result[root] >= result[child]:
				return
			result[root], result[child] = result[child], result[root]
			root = child

	size = len(result)
	for root in range(size // 2 - 1, -1, -1):
		sift_down(root, size)
	for end in range(size - 1, 0, -1):
		result[0], result[end] = result[end], result[0]
		sift_down(0, end)
	return result
