set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 21}
diff_set1_set2 = set1 - set2
diff_set2_set1 = set2 - set1
union_sets = set1 | set2
sym_diff_set2_set1 = set2 ^ set1
sym_diff_set1_set2 = set1 ^ set2
intersection_set1_set2 = set1 & set2
intersection_set2_set1 = set2 & set1

print("Set Difference (set1 - set2):", diff_set1_set2)
print("Set Difference (set2 - set1):", diff_set2_set1)
print("\nUnion of Sets (set1 | set2):", union_sets)
print("\nSymmetric Difference (set2 ^ set1):", sym_diff_set2_set1)
print("Symmetric Difference (set1 ^ set2):", sym_diff_set1_set2)
print("\nSet Intersection (set1 & set2):", intersection_set1_set2)
print("Set Intersection (set2 & set1):", intersection_set2_set1)
