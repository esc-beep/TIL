## math
- round: 반올림
- ceil: 올림
- floor: 내림

역순 - reverse() 혹은 pop()
```
def solution(my_string):
    return ''.join(list(reversed(my_string)))
```

set 자료구조 연습 더 하기

```
if search_string in main_string:
```
이런 식으로 문자열 안에 있는지 없는지 확인 가능

replace로 문자를 대체하거나 for string in my_string으로 문자열 내의 문자를 비교할수도 있음
```
my_string = my_string.replace(vowel, '')

def solution(rsp):
    rsp =rsp.replace('2','s')
    rsp =rsp.replace('5','p')
    rsp =rsp.replace('0','r')
    rsp =rsp.replace('r','5')
    rsp =rsp.replace('s','0')
    rsp =rsp.replace('p','2')
    return rsp
```

sort와 sorted 차이

소수점 자르는 방법
1. int() 변환
2. math.floor
3. format 사용(srt로 변환되는 것 주의하기)

[문자열 안의 숫자 확인](https://sikmulation.tistory.com/83) 알아두면 좋을듯 <br>
[문자열 소문자, 대문자 확인](https://dev-note-97.tistory.com/62)

슬라이스 기능이 참 좋다 <br>
`if i.startswith("aya"): i = i[len("aya"):]` 처럼 자를 수도 있다