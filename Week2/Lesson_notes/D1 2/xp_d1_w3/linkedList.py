class DoublyLinkedList:

    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None

    def set_next(self, next) -> None:
        self.next = next
        self.next.prev = self

    def set_prev(self, prev) -> None:
        self.prev = prev
        self.prev.next = self


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index == 0 and self.head:
            return self.head
        elif index > self.length - 1:
            return -1
        else:
            node = self.locate_node_at_index(index)
            return node.val

    def addAtHead(self, val: int) -> None:
        new_head = DoublyLinkedList(val)
        if self.head is None:
            self.head = new_head
            self.tail = new_head
        else:
            self.head.set_prev(new_head)
            self.head = new_head
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_tail = DoublyLinkedList(val)
        if self.tail is None:
            self.head = new_tail
            self.tail = new_tail
        else:
            self.tail.set_next(new_tail)
            self.tail = new_tail
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length - 1:
            return
        elif index == 0 and self.head:
            self.addAtHead(val)
        elif index == self.length - 1:
            self.addAtTail(val)
        else:
            new_node = DoublyLinkedList(val)

            node = self.locate_node_at_index(index)
            prev_node = node.prev

            prev_node.set_next(new_node)
            node.set_prev(new_node)

            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index > self.length - 1:
            return
        else:
            node = self.locate_node_at_index(index)
            prev_node = node.prev
            next_node = node.next

            prev_node.set_next(next_node)

            self.length -= 1

    def locate_node_at_index(self, index: int) -> DoublyLinkedList:
        current_index = 0
        current_node = self.head

        while current_index != index:
            current_node = current_node.next
            current_index += 1

        return current_node


def main():
    myLinkedList = MyLinkedList()
    myLinkedList.addAtHead(1)
    myLinkedList.addAtTail(3)
    myLinkedList.addAtIndex(1, 2)
    # linked list becomes 1->2->3
    myLinkedList.get(1)  # return 2
    myLinkedList.deleteAtIndex(1)  # now the linked list is 1->3
    myLinkedList.get(1)  # return 3


if __name__ == "__main__":
    main()
