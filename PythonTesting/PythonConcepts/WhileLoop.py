#  while loops are used to check a condition, it will continue until the condition is false

it = 4

while it > 1:  # it will print infinite because condition never become false and it keep on print 4 until you stop the program. To break this infinite loop use it=it-1
    print(it)
    it = it - 1
print("while loop execution is done")

print("********* SKIP *******")
# to skip printing 3 in between 4 & 2, then use if condition
ab = 4
while ab > 1:
    if ab != 3:
        print(ab)
    ab = ab - 1
print("while loop execution is done")

print("********* break statement *******")
# break - it is used to halt the loop abruptly
ac = 5
while ac > 1:
    if ac == 3:
        break
    print(ac)
    ac = ac - 1
print("while loop execution is done")

print("********* continue statement *******")
# continue - it is used when you want to skip the current iteration and proceed to next iteration
ad = 10
while ad > 1:
    if ad == 9:
        ad = ad - 1
        continue
    if ad == 3:
        break
    print(ad)  # 6, 5, 4
    ad = ad - 1
print("while loop execution is done")

