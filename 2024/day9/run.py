from typing import Optional

from aoc.base_solution import BaseSolution
from aoc.data_structures import LinkedNode


class Solution(BaseSolution):

    def init(self) -> None:
        raw_disk_map = self.load_raw()
        self.head = LinkedNode(-1)
        right_node = self.head

        for i in range(len(raw_disk_map)):
            if raw_disk_map[i] == "0":
                continue

            id = -1 if i % 2 else i // 2
            node = LinkedNode(id, int(raw_disk_map[i]))
            right_node.insert_right(node)

            if right_node.right:
                right_node = right_node.right

        if self.head.right:
            self.head = self.head.right
            self.head.left = None

    def _print_list_from_left(self, node: Optional[LinkedNode]) -> None:
        values = ""
        while node:
            c = "." if node.id == -1 else str(node.id)
            values += c * node.size
            node = node.right
        print("".join(values))

    def _checksum(self, node: Optional[LinkedNode]) -> int:
        checksum = 0
        i = 0
        while node:
            if node.id != -1:
                for n in range(i, i + node.size):
                    checksum += n * node.id
            i += node.size
            node = node.right

        return checksum

    def stage1(self) -> int:
        left = self.head.copy()
        right = left
        while right.right:
            right = right.right

        while left != right:
            # Move left to a free space
            if left.id != -1 or left.size == 0:
                if not left.right:
                    raise RuntimeError()
                left = left.right

            # Move right to a file with blocks to move
            elif right.id == -1 or right.size == 0:
                if not right.left:
                    raise RuntimeError()
                right = right.left

            # Expand previous block if from the same file
            elif left.left and left.left.id == right.id:
                left.left.size += 1
                left.size -= 1
                right.size -= 1

            # Create new block
            else:
                node = LinkedNode(right.id, 1)
                left.insert_left(node)
                left.size -= 1
                right.size -= 1

        while left.left:
            left = left.left

        return self._checksum(left)

    def stage2(self) -> int:
        head = self.head.copy()

        right = head
        while right.right:
            right = right.right

        while right:
            if right.id != -1:
                left = head
                while left:
                    if left.id == right.id:
                        break

                    if left.id == -1 and left.size >= right.size:
                        node = LinkedNode(right.id, right.size)
                        left.insert_left(node)
                        left.size -= right.size
                        right.id = -1
                        break

                    left = left.right

            right = right.left

        return self._checksum(head)


if __name__ == "__main__":
    Solution.main()
