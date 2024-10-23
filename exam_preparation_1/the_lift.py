people_waiting = int(input())
lift = list(map(int, input().split()))


for i in range(len(lift)):
    available_space = 4 - lift[i]

    if people_waiting >= available_space:
        lift[i] += available_space
        people_waiting -= available_space
    else:
        lift[i] += people_waiting
        people_waiting = 0

    if people_waiting == 0:
        break


if people_waiting == 0 and any(spots < 4 for spots in lift):
    print(f"The lift has empty spots!\n{' '.join(map(str, lift))}")
elif people_waiting > 0 and all(spots == 4 for spots in lift):
    print(f"There isn't enough space! {people_waiting} people in a queue!\n{' '.join(map(str, lift))}")
else:
    print(' '.join(map(str, lift)))