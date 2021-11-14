class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength

    def next(self) -> str:
        n = len(self.characters)
        vals_lst = []
        for i in range(n):
            for j in range(i+1, n):
                value = self.characters[i]+self.characters[j]
                if len(value) == self.combinationLength:
                    vals_lst.append(value)
        return vals_lst

    def hasNext(self) -> bool:

        # Your CombinationIterator object will be instantiated and called as such:
        # obj = CombinationIterator(characters, combinationLength)
        # param_1 = obj.next()
        # param_2 = obj.hasNext()
