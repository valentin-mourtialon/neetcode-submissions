class Node:
    def __init__(self, value: int, distance: int) -> None:
        self.value = value
        self.distance = distance


class MinStack:
    def __init__(self):
        self.stack: list[Node] = []
        self.length: int = 0

    def push(self, val: int) -> None:
        if self.length == 0:
            self.stack.append(Node(val, 0))
        else:
            previous_node = self.stack[-1]
            distance = max(val - (previous_node.value - previous_node.distance), 0)
            new_node = Node(val, distance)
            self.stack.append(new_node)
        self.length += 1

    def pop(self) -> None:
        _ = self.stack.pop()
        self.length -= 1

    def top(self) -> int:
        return self.stack[-1].value

    def getMin(self) -> int:
        top_node = self.stack[-1]
        return top_node.value - top_node.distance

    def __repr__(self) -> str:
        print("VALUE\tDISTANCE")
        for node in self.stack:
            print(f"{node.value}\t{node.distance}")
        return ""