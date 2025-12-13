from typing import Optional


class LinkedNode:
    def __init__(
        self,
        id: int,
        size: int = 0,
        left: Optional["LinkedNode"] = None,
        right: Optional["LinkedNode"] = None,
    ) -> None:
        self.id = id
        self.size = size
        self.left = left
        self.right = right

    def insert_right(self, node: "LinkedNode") -> None:
        node.left = self
        node.right = self.right
        if node.right:
            node.right.left = node
        self.right = node

    def insert_left(self, node: "LinkedNode") -> None:
        node.left = self.left
        if node.left:
            node.left.right = node
        node.right = self
        self.left = node

    def pop(self) -> None:
        if self.left:
            self.left.right = self.right
        if self.right:
            self.right.left = self.left

    def copy(self) -> "LinkedNode":
        head = LinkedNode(self.id, self.size)
        cur_ptr = self.right
        new_ptr = head
        seen = set([self.id])
        while cur_ptr:
            if cur_ptr in seen:
                break

            new_ptr.insert_right(LinkedNode(cur_ptr.id, cur_ptr.size))
            cur_ptr = cur_ptr.right
            if new_ptr.right:
                new_ptr = new_ptr.right
        return head
