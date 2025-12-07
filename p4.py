def merge_and_sort_sections(dict_a, dict_b):
    merged_dict = {**dict_a, **dict_b}
    sorted_dict = dict(sorted(merged_dict.items(), key=lambda item: item[1]))
    return sorted_dict

section_a = {'Alice': 101, 'Bob': 102, 'Charlie': 103}
section_b = {'David': 201, 'Eve': 202, 'Frank': 203}
merged_and_sorted = merge_and_sort_sections(section_a, section_b)
print("Merged and sorted dictionary:")
for student, roll_no in merged_and_sorted.items():
    print(f"{student}: {roll_no}")
