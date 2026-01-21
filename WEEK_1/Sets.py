# Create two sets of tech skills
skills1 = {"Python", "SQL", "Excel", "Power BI", "Python"}  # duplicate removed automatically
skills2 = {"Python", "Tableau", "Machine Learning", "AWS"}

# Union (all skills)
all_skills = skills1.union(skills2)
print("All skills:", all_skills)

# Intersection (common)
common = skills1.intersection(skills2)
print("Common skills:", common)


# Difference (skills in skills1 but not in skills2)
diff = skills1.difference(skills2)
print("Skills in skills1 but not in skills2:", diff)

