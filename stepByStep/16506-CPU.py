n = int(input())

asemble = []
for _ in range(n):
    op, rD, rA, smth = map(str, input().split())
    asemble.append([op, int(rD), int(rA), int(smth)])

dic = {
    "ADD" : '00000',
    "ADDC" : '00001',
    "SUB" : "00010",
    "SUBC" : "00011",
    "MOV" : "00100",
    "MOVC" : "00101",
    "AND" : "00110",
    "ANDC" : "00111",
    "OR" : "01000",
    "ORC" : "01001",
    "NOT" : "01010",
    "MULT" : "01100",
    "MULTC" : "01101",
    "LSTFL" : "01110",
    "LSTFLC" : "01111",
    "LSTFR" : "10000",
    "LSTFRC" : "10001",
    "ASFTR" : "10010",
    "ASFTRC" : "10011",
    "RL" : "10100",
    "RLC" : "10101",
    "RR" : "10110",
    "RRC" : "10111"
}

ans = []

def make_binary(a, bits):
    a = bin(a)[2:]
    return a.zfill(bits)

for i in asemble:
    temp = dic[i[0]] + '0'

    temp += make_binary(i[1],3)
    temp += make_binary(i[2],3)
    
    if temp[4] == '0': # rB
        temp += make_binary(i[3],3) + '0'
    elif temp[4] == '1':
        temp +=  make_binary(i[3],4) 
    
    print(temp)
        