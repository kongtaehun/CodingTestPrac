# 첫째줄에 노드의 개수, 간선 개수
# 둘째줄 부터 연결된 간선 정보입력\
n, m = map(int, input().split())
parant = [0 for i in range(n+1)]

# 자기자신을 부모로 설정하기
for i in range(len(parant)):
    parant[i] = i

# x의 부모를 찾는다.


#경로 압축을 이용하여 부모노드가 바로 루트노드가 되게끔
def find_parant(parant, x):
    if parant[x] != x:
        # x의 부모가 자기자신이 아니면 한번더 재귀적으로 호
        # x의 부모가 자기자신이면 더이상 안찾음
        # x의 루트를 반환하는 메소드
        parant[x] = find_parant(parant, parant[x])
    return parant[x]

# 두 원소가 연결되었을 때 두 원소의 부모(루트가) 작은 쪽의 부모를 부모로 설정


def set_parant(parant, a, b):
    a = find_parant(parant, a)
    b = find_parant(parant, b)
    if a < b:
        parant[b] = a
    else:
        parant[a] = b


for i in range(m):
    a, b = map(int, input().split())
    set_parant(parant, a, b)

# 속한 집합의 루트노드 확인
for i in range(1, n+1):
    print(find_parant(parant, i), end=' ')

# 부모노드 확인하기
for i in range(1, n+1):
    print(parant[i], end=' ')
