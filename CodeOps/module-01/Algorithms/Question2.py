def reverseCompare(num):
    str_num = str(num)
    rev_num = str_num[1] + str_num[0]
    if num > int(rev_num):
        print('ok')
    else:
        print("not ok")
reverseCompare(23)