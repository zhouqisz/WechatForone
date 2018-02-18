# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: test.py
@time: 2018/2/18 上午9:40
"""
def function(r):
    list = ''
    num =0
    nums = 0
    numt = 0
    for i in r:

        num = num + 1
        if i !=' ':

            nums = nums +1
            if nums == 3:
                list = list + '██'
                nums = 0

        if i ==' ':
            numt = numt + 1
            if numt ==2:

                list = list + '  '
                numt =0


    print list


file = open("1.txt")
while 1:
    line = file.readline()

    if not line:
        break
    function(line)
file.close()










if __name__ == '__main__':
    pass