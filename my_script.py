sameh = ["Sameh\n", "Yeah\n", "Toast\n"]
# open a file
sameh_file = open('sameh.txt', 'w')
sameh_file.writelines(sameh)
sameh_file.close()

sameh_file = open('sameh.txt', 'r')
Reading = sameh_file.readlines()

count = 0
for line in Reading:
    count+=1
    print("Reading line {}: {}".format(count, line.strip()))

# new_file = open('new_file.txt')
# file_items = new_file.readlines()

# for i in range(len(file_items)):
#     each_item = file_items[i]
#     print('Before: {}'.format(each_item))
#     print(each_item[0:-1])
#     file_items[i] = each_item[0:-1]
#     print(file_items)

# new_file.close()
# numbers = [1,2,3]
# for i in range(len(numbers)):
#     num = numbers[i]
#     sameh_file.write("{}\n".format(num))

# write to a file
# sameh_file.write("\nHello\n")
# sameh_file.close()

# # read a file
# print(sameh_file.read())

# # close a file
# sameh_file.close()

adam_file = open('adam.txt', 'w')

adam_file.write("\nAdam\n")
adam_file.close()