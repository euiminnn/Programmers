# 문제풀이 노트
## lv01 체육복
### 제출 코드 풀이
```python
def solution(n, lost, reserve):
    nums = 0
    same = []
    student = n - len(lost)
    for l in lost :
        if l in reserve :
            same.append(l)
    student += len(same)
    lost = list(set(lost) - set(same))
    reserve = list(set(reserve) - set(same))
    lost = sorted(lost)
    for l in lost :
        if l - 1 in reserve:
            reserve.remove(l - 1)
            nums += 1
        elif l + 1 in reserve:
            reserve.remove(l + 1)
            nums += 1
    student = student + nums
    return student
```
## lv03-2 단속카메라
### 제출 코드 풀이
```python
def solution(routes):
    routes.sort(key = lambda x: x[0])    # 진입이 빠른 순서로 정렬
    answer = 1
    cam = routes[0][1]
    for r in routes :
        start = r[0]
        end = r[1]
                                         # 알고리즘 설명: 그룹 정하기 -> 그 중에 가장 빠른 진출 시점을 골라 -> cam 설치 -> 다음 그룹                                         
        if start <= cam or end <= cam :  # 그룹 정하기(진입 기준 정렬되어 있으므로 'start는 cam 보다 앞에 있지만 end는 뒤에 있는 경우 - 즉, 진입은 앞 그룹에 & 진출은 뒷 그룹에 "끼인 경우"도 포함됨, 아래 그림에서 for문 2번 경우)
            cam = min(end, cam)          # 가장 빠른 진출 시점(==최소 end) 찾기

        else :                           # 한 그룹이 끝났고, 다음 그룹으로 넘어감
            answer += 1                  # 한 그룹 끝날 때 카메라 설치
            cam = end                    # cam위치는 다음 그룹 시작할 때의 end위치로 옮겨둠(이렇게 해야 그 그룹의 모든 end에 대해 min값 찾기 가능)
            
    return answer
```
### 진입 기준 sort 후 for문 실행순서 
![참조](https://github.com/euiminnn/image-upload/blob/master/cam.png)