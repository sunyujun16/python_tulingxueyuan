import queue


q = queue.Queue()

q.put({'one': 1})
q.put({'two': 2})
q.put({'three': 3})

# 下面的写法, 内存占用急剧增加
# while True:
#     try:
#         q_list = q.get(block=False)
#     except queue.Empty:
#         continue

q_list = q.get(block=False)

if q_list.get('one'):
    print('yes')

q_list = q.get(block=False)
print(q_list)








