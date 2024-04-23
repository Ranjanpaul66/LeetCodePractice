from integer_container import IntegerContainer


class IntegerContainerImpl(IntegerContainer):

    def __init__(self):
        # TODO: implement
        self.container = []
        pass

    def add(self, value: int) -> int:
        """
        Add the specified integer `value` to the container
        and return the number of integers in the container after the
        addition.
        """
        self.container.append(value)
        return len(self.container)

    # TODO: implement interface methods here

    def delete(self, value: int) -> bool:
        """
        Attempt to remove the specified integer `value` from
        the container.
        If the `value` is present in the container, remove it and
        return `True`, otherwise, return `False`.
        """
        if value in self.container:
            self.container.remove(value)
            return True
        else:
            return False

    def get_median(self) -> int | None:

        if not self.container:  # if container is empty
            return None

        sorted_container = sorted(self.container)
        length = len(sorted_container)
        if length % 2 == 0:  # if length is even
            return sorted_container[length // 2 - 1]
        else:
            return sorted_container[length // 2]