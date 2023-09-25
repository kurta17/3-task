from collections import Counter

# def count_popular():
#     number = []
#     for i in array_number:
#         x = array_number.count(i)
#         number.append(x)
#     if number == []:
#         return "0"
#     return number
    
# print(max(count_popular()))

from collections import Counter
collection = [2,3,4,4,5,5,5]
def most_frequent_item_count(collection):
    if collection == []:
        return 0
    counter = Counter(collection)
    return counter.most_common(1)[0][1]

print(most_frequent_item_count(collection))
