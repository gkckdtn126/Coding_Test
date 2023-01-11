import sys
n,k = map(int,input().split())
def main(n,k):
    m_list = []
    for x in range(1,n+1):
        if n%x==0:
            m_list.append(x)
    if len(m_list)<k:
        return -1
    else:
        return m_list[k-1]
print(main(n,k))