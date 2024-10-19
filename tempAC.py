import base64
Q=int(input())
for i in range(Q):
  text=input()
  print(base64.b64encode(text.encode()).decode())