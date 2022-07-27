def smaller(students, rank = 2):
    names = [x for [x,y] in students]
    scores = [y for [x,y] in students]
    scores2 = set(scores)
    scores3 = sorted(list(scores2))
    min_ranked_score = scores3[rank-1]
    names2 = [x  for [x,y] in students if y== min_ranked_score] 
    return sorted(names2)


if __name__ == "__main__":
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    print(smaller(students,2))
