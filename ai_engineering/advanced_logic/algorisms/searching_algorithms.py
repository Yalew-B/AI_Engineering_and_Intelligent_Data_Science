"""Basic searching algorithms.

Binary, jump, and interpolation search expect the input to be sorted in
ascending order. Each function returns the index of a match, or -1.
"""

from math import isqrt
from typing import Any, Sequence


def linear_search(items: Sequence[Any], target: Any) -> int:
	"""Search any sequence from left to right in O(n) time."""
	for index, item in enumerate(items):
		if item == target:
			return index
	return -1


def binary_search(items: Sequence[Any], target: Any) -> int:
	"""Search sorted items in O(log n) time."""
	low, high = 0, len(items) - 1
	while low <= high:
		middle = (low + high) // 2
		if items[middle] == target:
			return middle
		if items[middle] < target:
			low = middle + 1
		else:
			high = middle - 1
	return -1


def jump_search(items: Sequence[Any], target: Any) -> int:
	"""Search sorted items in O(sqrt(n)) time."""
	size = len(items)
	if not size:
		return -1

	step = isqrt(size) or 1
	start, end = 0, step
	while start < size and items[min(end, size) - 1] < target:
		start, end = end, end + step

	for index in range(start, min(end, size)):
		if items[index] == target:
			return index
		if items[index] > target:
			break
	return -1


def interpolation_search(
	items: Sequence[int | float], target: int | float
) -> int:
	"""Search sorted numeric items; efficient on uniformly distributed data."""
	low, high = 0, len(items) - 1
	while low <= high and items[low] <= target <= items[high]:
		if items[low] == items[high]:
			return low if items[low] == target else -1

		position = low + int(
			(target - items[low]) * (high - low) / (items[high] - items[low])
		)
		if items[position] == target:
			return position
		if items[position] < target:
			low = position + 1
		else:
			high = position - 1
	return -1
