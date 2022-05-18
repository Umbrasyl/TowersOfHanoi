class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None


class Stack:
    def __init__(self, name):
        self.name = name
        self.head = None
        self.limit = 1000
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def has_space(self):
        return self.limit > self.size

    def push(self, value):
        if self.has_space():
            new_node = Node(value)
            new_node.next_node = self.head
            self.head = new_node
            self.size += 1
        else:
            print("No more room!")

    def peek(self):
        if not self.is_empty():
            return self.head.value
        print("Nothing to see here!")

    def pop(self):
        if not self.is_empty():
            node_to_remove = self.head
            self.head = node_to_remove.next_node
            self.size -= 1
            return node_to_remove.value
        print("The stack is empty!")

    def print_items(self):
        pointer = self.head
        item_list = []
        while pointer:
            item_list.append(pointer.value)
            pointer = pointer.next_node
        item_list.reverse()
        print(f"{self.name} Stack: {item_list}")


def get_input():
    choices = [stack.name[0] for stack in stacks]
    while True:
        for k in range(0, len(stacks)):
            print(f"Enter {choices[k]} for {stacks[k].name}")
        user_input = input("").upper()
        if user_input in choices:
            for m in range(0, len(stacks)):
                if choices[m] == user_input:
                    return stacks[m]


stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

print("\nLet's play Towers of Hanoi!!")
num_disks = int(input("\nHow manu stacks do you want to play with?\n"))
while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3.\n"))

for i in range(num_disks, 0, -1):
    stacks[0].push(i)

num_optimal_moves = 2 ** num_disks - 1
print(f"The fastest you can solve this game is in {num_optimal_moves} moves.")

num_user_moves = 0
while stacks[-1].size < num_disks:
    print("\n\n\n...Current Stacks...")
    for current_stack in stacks:
        current_stack.print_items()
    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()
        if from_stack.is_empty():
            print("\n\nInvalid move. Please try again.")
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        print("\n\nInvalid move. Please try again.")

print(f"You completed the game in {num_user_moves}, and the optimal number of moves is {num_optimal_moves}.")
