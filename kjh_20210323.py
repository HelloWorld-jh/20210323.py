print('Hello world!')
# 숫자열 자료형
a = 123
print(a)

a = -12.34
print(a)


a = 5
b = 3
print(a + b)  # 덧셈
print(a - b)  # 뺄셈
print(a * b)  # 곱셈
print(a / b)  # 나눗셈
print(a // b) # 몫
print(a % b)  # 나머지

# 문자열 자료형
a = 'hello world'
print(a)
b = "Life is short, You need Python"
print(b)

a = """Life is too short, You need Python"""
b = '''Life is too short, You need Python'''
print(a)
print(b)
print("Python's favorite food is perl")
# print("Python's favorite food is perl")

print('"Python is very easy." he says."')
# print(""Python is very easy." he says."")

print('Python\'s favorite food is perl')
print("\"Python is very easy.\" he says.")

a = '''Life is too short
You need Python'''
print(a)
a = """Life is too short
You need Python"""
print(a)

a = 'Life is too short\nyou need Python'
print(a)



'''
메모
1. Python 기초
2. Python 데이터 분석
3. 머신러닝
'''

head = "Python"
tail = " is fun!"
print(head + tail) # 덧셈의 연산: 문자열 합치기

a = 'python'
print(a * 2) # 문자열 곱셈: 문자열 반복

print('\\123python' * 6)

# 문자열 길이 구하기
a = "Life is too short"
print(len(a))
b = "Life is too short, You need Python"
print(len(b))
c =''
print(len(c))

a = "\"Python\" he says."
print(len(a),"\n", a)

# 문자열 인덱싱
a = "Life is too short, You need Python"
print(a[0])  # 첫번째 글자
print(a[1])  # 두번째 글자
print(a[-1]) # 마지막 글자
print(a[-2]) # 끝에서 두번째 글자
print(a[0] + a[1] + a[2 ]+ a[3])  # Life 출력값

# print(a[100]) # IndexError 없는 인덱스 접근 오류

# 문자열 슬라이싱
a = "Life is too short, You need Python"
print(a[0:6])
print(a[0:17])


a = 'abcdefghijkmmlnop'
print(a[0:5])
print(a[5:10])
print(a[0:10:2]) # [시작번호:끝번호:증감값]
print(a[10:0:-1])

print(a[:5])
print(a[5:])
print(a[:])
print(a[10:0:-1])