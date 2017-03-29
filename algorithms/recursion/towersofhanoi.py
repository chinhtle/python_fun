def hanoi(disks, source, helper, target):
    if disks >= 1:
        # Move n-1 disks from source to helper
        hanoi(disks - 1, source, target, helper)

        # Move 1 disk from source to target
        print source, "->", target

        # Move previously moved disks from helper to target
        hanoi(disks - 1, helper, source, target)


num_disks = 3
source, helper, target = 1, 2, 3

hanoi(num_disks, source, helper, target)
