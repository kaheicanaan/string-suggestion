from string_suggestion import EditDistance


ed = EditDistance(insertion_cost=1, deletion_cost=1)
distance = ed.compare('intention', 'execution')
test_array = ed.edit_distance_table
print(distance)
print(test_array)

# ed = EditDistance(insertion_cost=1, deletion_cost=2)
# ed.compare('abc', 'abbc')
