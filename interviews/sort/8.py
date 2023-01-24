class Person:
  def __init__(self, k, n):
    self.age = k
    self.name = n


def solution(people):
  ageToCount = dict()

  for p in people:
    if p.age in ageToCount.keys():
      ageToCount[p.age] += 1
    else:
      ageToCount[p.age] = 1
  
  ageToOffset = dict()
  offset = 0

  for k, v in ageToCount.items():
    ageToOffset[k] = offset
    offset += v

  result = [None] * len(people)
  for p in people:
    offset = ageToOffset.get(p.age)
    result[offset] = p
    ageToOffset[p.age] += 1
  
  return result
  


if __name__ == "__main__":
  people = [
    Person(14, 'Greg'),
    Person(12, 'John'),
    Person(11, 'Andy'),
    Person(13, 'Jim'),
    Person(12, 'Phil'),
    Person(13, 'Bob'),
    Person(13, 'Chip'),
    Person(14, 'Tim'),
  ]

  result = solution(people)
  for p in result:
    print(p.age, p.name)