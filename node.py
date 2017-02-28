class node:
    def __init__(self, root, left, right, word, score):
        self.root = root
        self.left = left
        self.right = right
        self.word = word
        self.score = score
        self.isEnd = True
        if (word == None):
            self.isEnd = False
