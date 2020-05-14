class Baggage:
    def __init__(self, length, width, height, weight):
        self.length = length
        self.width = width
        self.height = height
        self.sum = length + width + height

        self.weight = weight

        self._check()

    def _check(self):
        if self.sum <= 2:
            raise Exception("长宽高的和未超过2, 不是一个行李")
