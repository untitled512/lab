test = "Замена шаблона На замену. maxcount ограничивает. количество замен"
# new_type = test.split(" ")
# print(new_type)
# print(type(new_type))

# new_type2 = [1, 2, 3, 4, 'ghb', "_"]
# print(f'{type(new_type2)=} {new_type2}')

# for i in new_type2:
#     print(f'{i=}', type(i))
#     if isinstance(i, str):

#         if len(i) > 1:
#             print('\tбольше', i)

# print(new_type[0])

# l = []
# for i in test:
#     if i.istitle():
#         print(i)
#         l.append(i)
# print(l)

check_simb = [' ','.']
c = 0
for i in test:
    # print(i)
    if i not in check_simb:
        print(c, i)
        c += 1 
print(c)
exit(0)
print()
for i in test:
    print(f'{i=}', type(i))

