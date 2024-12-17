def calculate_structure_sum(data_structure):
    total = 0

    def explore_data(element):
        nonlocal total
        for subelement in element:
            if isinstance(subelement, int):
                total += subelement
            elif isinstance(subelement, str):
                total += len(subelement)
            elif isinstance(subelement, dict):
                total += calculate_structure_sum(subelement.values())
                total += calculate_structure_sum(subelement)
            else:
                total += calculate_structure_sum(subelement)

    explore_data(data_structure)
    return total

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)