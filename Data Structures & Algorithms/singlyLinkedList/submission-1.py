class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        return

    def insertHead(self, value) -> None:
        if self.head is None:  # Empty list
            self.head = Node(value)
            self.tail = self.head
            return
        new_head = Node(value)
        previous_head = self.head
        self.head = new_head
        self.head.next = previous_head

    def insertTail(self, value: int) -> None:
        new_tail = Node(value)
        if self.tail:
            self.tail.next = new_tail
        else:  # empty list
            self.head = new_tail
        self.tail = new_tail

    def _get(self, index: int) -> Node | None:
        if index < 0:
            return None
        curr = self.head
        if curr is None:  # Empty list
            return None
        i = 0
        while curr.next is not None:
            if i == index:
                return curr
            curr = curr.next
            i += 1
        return curr if i == index else None

    def remove(self, index: int) -> bool:
        node = self._get(index)  # Handle empty list
        if node is None:
            return False

        prev_node = self._get(index - 1)
        next_node = self._get(index + 1)

        if prev_node is None and next_node is None:  # Only one node in the list
            self.head = None
            self.tail = None
        elif prev_node is None and next_node:  # First element
            self.head = next_node
        elif prev_node and next_node is None:  # Last element
            prev_node.next = None
            self.tail = prev_node
        else:
            prev_node.next = next_node

        del node
        return True

    def get(self, index: int) -> int:
        node = self._get(index)
        return node.value if node is not None else -1

    def getValues(self) -> list[int]:
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.value)
            curr = curr.next
        return result

    def __repr__(self) -> str:
        if self.head is None:
            print("EMPTY")
            return ""

        if self.head.next is None:
            print("👇 HEAD")
            print(
                f"ADDR = {hex(id(self.head))[-4:]}\tVALUE = {self.head.value}\tNEXT = {self.head.next}"
            )
            print("👆 TAIL")
            return ""

        print("👇 HEAD")
        curr = self.head
        while curr.next is not None:
            print(
                f"ADDR = {hex(id(curr))[-4:]}\tVALUE = {curr.value}\tNEXT = {hex(id(curr.next))[-4:]}"
            )
            curr = curr.next
        print(
            f"ADDR = {hex(id(self.tail))[-4:]}\tVALUE = {self.tail.value}\tNEXT = {self.tail.next}"
        )
        print("👆 TAIL")
        return ""