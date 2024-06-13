n, k = map(int,input().split())
machine = list(map(int,input().split()))

st = set()
victim = 0

for m in range(k):

    cur_data = machine[m]

    if len(st) < n:
        st.add(cur_data)
    else:
        if cur_data not in st:
            dic = {}
            idx = 1

            for data in st:
                dic[data] = 0
            
            for next in range(m+1, k):
                if machine[next] in dic and dic[machine[next]] == 0:
                    dic[machine[next]] = idx 
                    idx += 1
            
            sorted_dic = sorted(dic.items(), key=lambda x : x[1])

            #print("sorted_dic : {}".format(sorted_dic))

            if sorted_dic[0][1] == 0:
                st.remove(sorted_dic[0][0])
            else:
                #print("sorted_dic[-1][0] : {}".format(sorted_dic[-1][0]))
                st.remove(sorted_dic[-1][0])

            st.add(cur_data)
            victim += 1
            #print("st : {}".format(st))

print(victim)