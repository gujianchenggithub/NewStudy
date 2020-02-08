# import csv
# stu1=['marry',28,'changsha']
# stu2=['lili',22,'hanghzou']
# out=open('stu.csv','a',newline='')
# csv_write=csv.writer(out,dialect='excel')
# csv_write.writerow(stu1)
# csv_write.writerow(stu2)
# print("write is over!!!")

# print(""" I ;"''"NIH AO"123"  """)
#
# # print(''' I ;"''"NIH AO"123" ''')
# import math
#
# # str='lemon'
# # print(str.replace('lemon','apple'))
# # print('i am %d years old' %(16))
# # print('hello {}'.format('word'))
# # # print('hello {1} {0}'.format('word','python'))
# # print('i am %(name)s,i am %(age)s years old' %{'name':'lemon','age':'16'})
#
# list=['qwe',12]
# print(list)
# print(list[0])

# age=18
# name='ASDFASFgjc'
# score=99.99
# # print("%s，今年%d岁,数学考了%.2f分"%(name,age,score))
# # print("{1},今年考了{1}分".format(name,score))
# res=name.strip('gjc')
#
# print("我是{}".format(res))



# list_A=[12,'qwe',(1,3,7),[12,'er']]
# print(list_A[-1][0])

# a={'name':'gjc','age':18,'home':'jilin'}
# c={'name':'njx','age':14,'home':'chifeng'}

# a['score']=[12,13]
# a['name']='njx'
# a.pop('age')
# del a['home']
# print(a.keys())
# print(a.values())
# print(a.items())
# a.update(c)

# a='gjc'
# print(a*5)


# color='dd'
# if color=='red':
#     print('红灯停....')
# elif color=='green':
#     print('绿灯行...')
# else:
#     print("黄灯等一等！！！")



# a=1
# sum = 0
# while a < 1011:
#     sum = sum + a
#     a = a+1
# print("1-100的和相加是：{0}".format(sum))


# a=10
# while True:
#     a-=1
#     if a>0:
#         print("a value is {0}".format(a))
#         continue
#     else:
#         break

# print(list(range(1,9,3)))

# s='python'
# for i in range(0,len(s)):
#     print(s[i])

# ji_sum=0
# ou_sum=0
# for i in range(101):
#     if i%2==0:
#         ou_sum+=i
#     else:
#         ji_sum+=i
#
# print("1-100奇数相加和为:{0}\n1-100偶数相加和为:{1}".format(ji_sum,ou_sum))


# def add(m,n,k):
#     count=0
#     for i in range(m,n,k):
#         count+=i
#
#     return count
#
# result=add(0,101,2)
# print(result)

# def gjc_info(**kwargs):
#     print("kwargs:",kwargs)
#     for item in kwargs.values():
#         print(item)
#
#
#
# gjc_info(t_name="gjc nihao",t_class="柠檬班",t_course="python全栈自动化")



class BoyFriend:
    height=175
    money=20000
    name='周杰伦'
    age=28

    def cooking(self):
        print('会做饭')

    def hiking(self):
        print('like hiking')

    def swiming(self):
        print('like swiming')


bf=BoyFriend()
print(bf.height)

bf.swiming()



































































