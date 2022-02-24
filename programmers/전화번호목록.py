# 효율성 실패
# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     for i in range(len(phone_book)-1):
#         nl = len(phone_book[i])
#         for j in range(i+1, len(phone_book)):
#             if phone_book[j][:nl] == phone_book[i]:
#                 answer = False
#                 break

#     return answer

def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False

    return answer
