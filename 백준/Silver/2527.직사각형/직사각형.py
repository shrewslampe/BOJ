for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    if p1 < x2 or q1 < y2 or p2 < x1 or q2 < y1:
        print('d')
    elif (p1 == x2 and q1 == y2) or (p2 == x1 and q2 == y1) or (p2 == x1 and y2 == q1) or (p1 == x2 and y1 == q2):
        print('c')
    elif p1 == x2 or q1 == y2 or p2 == x1 or q2 == y1:
        print('b')
    else:
        print('a')
