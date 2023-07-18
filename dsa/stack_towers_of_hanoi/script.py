from stack import Stack


print("\nLet's play Towers of Hanoi!!")

# Create the Stacks
stacks = []
left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack = Stack('Right')

stacks += [left_stack, middle_stack, right_stack]

# Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
    num_disks = int(input("\nChoose more dude..\n"))

for num in range(num_disks, 0, -1):
    left_stack.push(num)

num_optimal_moves = 2 ** num_disks - 1
print("\nThe fastest you can solve this game is in {0} moves".format(
    num_optimal_moves))


def get_input():
    choices = [stack.get_name()[0] for stack in stacks]
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print("Enter {0} for {1}".format(letter, name))
        user_input = input("\nEnter: ")
        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]


num_user_moves = 0

while right_stack.get_size() != num_disks:
    print("\n\n\n...Current Stacks...")

    for stack in stacks:
        print(stack.print_items())

    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()

        if from_stack == to_stack:
            print(
                "\nYou have selected the same stack twice. You must select two different stacks.\n")
        elif from_stack.is_empty():
            print("\nYour chosen stack has no disks on it.\n")
        elif to_stack.size > 0 and from_stack.peek() > to_stack.peek():
            print("\nYou cannot move a larger disk onto a smaller disk.\n")
        else:
            disk = from_stack.pop()
            to_stack.push(disk)
            break

print("Congratulations, you have completed the game!")
