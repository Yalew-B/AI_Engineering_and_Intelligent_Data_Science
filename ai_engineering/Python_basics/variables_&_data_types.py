"""A beginner-friendly introduction to Python variables and data types."""


def main() -> None:
	# Python variables are names assigned to values; their types are inferred.
	name = "Ada"
	age = 36
	height = 1.65
	is_programmer = True

	print("Variables")
	print(f"Name: {name}; age: {age}; height: {height} m")
	print(f"Programmer: {is_programmer}")
	print(f"The type of age is {type(age).__name__}.")

	# Common built-in types include str, int, float, bool, and NoneType.
	message = "Hello, Python!"
	count = 3
	temperature = 21.5
	is_ready = False
	result = None

	# Collections group multiple values: list, tuple, set, and dict.
	colors = ["blue", "green"]
	coordinates = (10, 20)
	unique_numbers = {1, 2, 2, 3}  # Sets automatically discard duplicates.
	student = {"name": name, "age": age}

	print("\nCommon data types")
	examples = (
		("message", message),
		("count", count),
		("temperature", temperature),
		("is_ready", is_ready),
		("result", result),
		("colors", colors),
		("coordinates", coordinates),
		("unique_numbers", unique_numbers),
		("student", student),
	)
	for label, value in examples:
		print(f"{label}: {value!r} ({type(value).__name__})")

	# Variables can be reassigned, and unpacking assigns tuple values by name.
	count += 1
	x, y = coordinates
	print(f"\nUpdated count: {count}; x={x}, y={y}")

	# Convert values explicitly when needed. Invalid conversions raise errors.
	age_number = int("36")
	price = float("4.50")
	print(f"Converted age: {age_number}; price: {price:.2f}")

	if isinstance(age_number, int):
		print("age_number is an integer")


if __name__ == "__main__":
	main()
