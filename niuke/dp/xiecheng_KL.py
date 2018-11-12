import sys
import math

p = [1,1,1,2,3,4,1,2,3,4,1,3,4,1,2,3,3,1,2,3,1,2,3,1,3,1]
q = [2,2,2,2,3,4,4,2,2,1,2,4,3,2,2,1,3,4,4,2,4,3]


def kl_dis(x,y):
    D_pq = 0
    p_count = {}
    q_count = {}
    p_x = {}
    q_x = {}
    len_p = len(x)
    len_q = len(y)
    for i in range(len_p):
        if str(p[i]) not in p_count:
            p_count[str(p[i])] = 1
        else:
            p_count[str(p[i])] += 1
    for i in range(len_q):
        if str(q[i]) not in q_count:
            q_count[str(q[i])] = 1
        else:
            q_count[str(q[i])] += 1
    for i in p_count:
        if i not in p_x:
            p_x[i] = p_count[i]/len_p
        if i not in q_x:
            q_x[i] = q_count[i]/len_q

    for i in p_x:
        D_pq  +=  p_x[i]*(math.log2(p_x[i]/q_x[i]))
    print(p_count)
    print(q_count)
    print(p_x)
    print(q_x)
    return round(D_pq,2)

res = kl_dis(p,q)
print(res)


