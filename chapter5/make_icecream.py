# 실전 5-1. 음료수 얼려 먹기: N x M 얼음 판을 입력 받아 음료수를 넣어 얼린다면 얼마나 많은 아이스크림을 얻을 수 있을까
def dfs(ice,i,j,N,M):
    ice[i][j] = 1   # ice[i][j] == 0 이라면 dfs 함수를 실행하도록 하였으므로 한번 확인한 곳은 1로 값을 변경
    print(i,j)      # 현재 재귀 함수 내에서 확인하고 있는 위치 표시
    if i < N-1 and ice[i+1][j] == 0:    # 만약 아래쪽에 인접한 요소가 값이 0 이라면 위치를 바꾸어 실행. i가 N보다 커질 순 없으므로 조건 추가
        dfs(ice,i+1,j,N,M)
    if j < M-1 and ice[i][j+1] == 0:    # 만약 오른쪽에 위치한 요소가 값이 0 이라면 위치를 바꾸어 실행. j가 M보다 커질 순 없으므로 조건 추가
        dfs(ice,i,j+1,N,M)






# N,M 값 입력받고, 얼음판 모양도 입력받음. (0이 뚫려있는 부분, 1이 막혀있는 부분)
N,M = map(int,input("N, M: ").split())
ice = []
count = 0
for i in range(N):
    ice.append(list(map(int,input(">> ").split())))

for i in range(N):
    for j in range(M):
        if not ice[i][j]:
            dfs(ice,i,j,N,M)
            count += 1          # 인접한 모든 구역을 체크하고 나서 dfs를 빠져나오면 아이스크림 개수를 세어줌
            print("counting!")  # 음료수를 얼린 구역 하나를 모두 찾음!
print(count)

# idea: 첫 행의 첫 요소부터 차례대로 한 행 내의 모든 요소들을 읽은 뒤, 다음 행으로 넘어가는 형식으로 읽는다.
#       이때 0을 읽는다면 깊이 탐색 방법을 이용하여 연결된 부분들을 모두 1로 바꾼다. 읽는 순서를 고려하여 오른쪽, 아래쪽에 붙어있는 요소들만 읽어서 1로 바꾼다.
#       마지막 행의 마지막 요소까지 읽으면 N x M 얼음 판에는 아이스크림의 크기와 관계없이 1개당 0이 1개씩 위치를 할 것이다.
#       그렇다면 해야할 것은? dfs 혹은 bfs를 이용하기 위해 어떻게 할 것인가.