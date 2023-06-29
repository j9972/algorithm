def solution(phone):
    phone.sort()
    
    for i in range(len(phone)-1):
        if phone[i] == phone[i+1][:len(phone[i])]:
            return False

    return True