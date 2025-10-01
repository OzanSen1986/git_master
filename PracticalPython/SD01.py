from time import perf_counter

start = perf_counter()

list_of_words = ['Hello', 'yes', 'goodbye', 'last', 'hello']

# time_duration : 0.000021 VS 
#                 0.000024
# print(list_of_words[0] + ',' + list_of_words[1] + ',' + list_of_words[2] + ',' + list_of_words[3])

# to_print = ""

# for i in range(len(list_of_words)):
#     to_print += list_of_words[i]
#     if i != len(list_of_words)-1:
#         to_print += ","
# print(to_print)

DELIMITER = ','
print(DELIMITER.join(list_of_words))

finish = perf_counter()

print(f'total time spent: {finish - start:.6f} second(s)')


