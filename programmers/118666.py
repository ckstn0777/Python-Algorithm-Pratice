# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/118666
# 단순한 구현 문제인듯하다 (레벨 1)

##################
# 내 소스코드 - 배열말고 문자열로 할걸..ㅋㅋ
def my_solution(survey, choices):
    answer = ''

    order = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    scores = [0, 0, 0, 0, 0, 0, 0, 0]

    for idx, survey_d in enumerate(survey):
      l, r = order.index(survey_d[0]), order.index(survey_d[1])

      # print(l, r, choices[idx])
      if choices[idx] < 4:
        scores[l] += 4 - choices[idx]
      elif choices[idx] > 4:
        scores[r] += choices[idx] - 4

    for idx in range(0, 8, 2):
      if scores[idx] >= scores[idx + 1]:
        answer += order[idx]
      else:
        answer += order[idx + 1] 

    return answer


##################
# 다른 사람 소스코드 : zip을 쓰면 좋네. 그 외에는 글쎄?
def solution(survey, choices):
  my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
  for A, B in zip(survey, choices):
    if A not in my_dict.keys():
      A = A[::-1]
      my_dict[A] -= B-4
    else:
      my_dict[A] += B-4 

  # print(my_dict)
  result = ""
  for name in my_dict.keys():
    if my_dict[name] > 0:
      result += name[1]
    elif my_dict[name] < 0:
      result += name[0]
    else:
      result += sorted(name)[0]

  return result



print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))