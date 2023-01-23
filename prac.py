from collections import namedtuple
Box = namedtuple('Box', ['width','height'])
b = Box(20,40)
w,h = b
print(w, h)


print(b.width, b.height) # 변수를 이렇게 접근할 수도 있다.
# >>> 20 40

print(b)
# >>> Box(width=20, height=40)

#(class와 비슷)