class BlockChain:

    def __init__(self, genesis_block):
        self.root = genesis_block
        self.blocks = dict()

        root_hash = self.root.hash()
        self.blocks[root_hash] = self.root
        self.blocks[None] = None


    def append(self, new_block):
        if new_block == self.root:
            return None
        curr_block = new_block
        while curr_block != self.root:
            if curr_block is None:
                return None
            if curr_block not in self.blocks.keys():
                return None
            curr_block = self.blocks[curr_block.previous_hash]
        self.blocks[new_block.hash()] = new_block
        return new_block
