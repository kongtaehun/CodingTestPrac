def solution(phone_book):
    #sort를 이용하면 for문을 한번만 사용해도댐
    phone_book.sort()
    for i in range(len(phone_book)):
        if phone_book[i].startswith(phone_book[i-1]):
            return False

    return True