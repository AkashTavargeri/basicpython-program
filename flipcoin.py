import random

num_of_flip = 4 #int("Enter the number of flips : ")
head_count = 0
tail_count = 0
for i in range(num_of_flip):
    face = random.randint(0,1,)
    if(face == 0):
        # print("Head")
        head_count = head_count + 1
    else:
        # print("Tail")
        tail_count = tail_count + 1

# print("Head count is : ",head_count)
# print("Tail count is : ",tail_count)
head_percentage = (head_count/num_of_flip) * 100
tail_percentage = 100 - head_percentage

print("Percentage of head is : ",head_percentage,"%")
print("Percentage of Tail is : ",tail_percentage,"%")