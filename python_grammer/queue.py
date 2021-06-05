# a=list() # 오른쪽을 기준으로 추가, 왼쪽을 기준으로 삭제하는 경우
# a.append("a") #배열의 맨 뒤에 데이터 추가
# a.append("b")
# a.append("c")
# a.append("d")
# print(a) #['a', 'b', 'c', 'd']
# a.pop(0) #pop(0) 는 제일 처음에 추가된 데이터 삭제 - queue
# print(a) #['b', 'c', 'd']
# a.pop() #pop() 은 제일 최근에 추가된 데이터 삭제 - stack
# print(a) #['b', 'c']

# a=list() # 오른쪽을 기준으로 삭제, 왼쪽을 기준으로 추가하는 경우
# a.insert(0,"a") #배열의 처음부분에 데이터 추가
# a.insert(0,"b")
# a.insert(0,"c")
# a.insert(0,"d")
# print(a) #['d','c','b','a']
# a.pop() #제일 처음에 추가된 맨 뒤의 데이터 삭제 - queue
# print(a) #['d','c','b']
# #top 이나 peek같은 메소드는 존재하지 않는다.
# from queue import Queue
# a = Queue()
# a.put("a") #추가
# a.put("b")
# a.put("c")
# a.put("d")
# print(a.get()) #제거
# #output : 'a' from collections import deque
# a = deque(['a','b','c','d'])
# a.appendleft('f')
# a.append('f2')
# print(a) #deque(['f', 'a', 'b', 'c', 'd', 'f2'])
# a.pop()
# print(a) #deque(['f', 'a', 'b', 'c', 'd'])
# a.popleft()
# print(a) #deque(['a', 'b', 'c', 'd'])
# print(a[0])