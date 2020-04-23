def merge_the_tools(string, k):
    # your code goes here
    t = [string[i*k:(1+i)*(k)] for i in range(int(len(string)/k))]
    u = [list(set(list(i))) for i in t]
    for i in range(len(t)): 
        tmp = ""
        for j in t[i]:
            if j in u[i] and j not in tmp:
                tmp += j
        print(tmp)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)