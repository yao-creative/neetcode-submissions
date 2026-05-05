class Node:
    def __init__(self, value = "", count = 0, children = None):
        self.value = value
        self.count = count
        self.children = dict()
    
    def __repr__(self):
        return f"Node(value: {self.value}, count: {self.count}, children: {[c for c in self.children]})"


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        # traverse the word if it's in the tree
        # print(f"adding: {word}")
        node = self.root
        for c in word:
            # print(f"node: {node}")
            children_vals = {child_val : child for child_val, child in node.children.items()}
            # print(f"children_vals: {children_vals}")
            if c not in children_vals:
                # print(f"adding character {c}")
                node.children[c] = Node(c)
            
            node = node.children[c]
        #add counter to last node that there's a word here
        node.count += 1
        # print(f"final node: {node}")

    def search(self, word: str) -> bool:
        node = self.root
        # print(f"searching: {word}")

        possible_end_nodes = []
        #two cases "." leads us to the end, or "." leads to a letter in the middle.
        def dfs(i: int, node) -> None:
            # print(f"Node: {node}")
            if i == len(word):
                # we're at the node
                possible_end_nodes.append(node)
                return #then check check node 
            
            c = word[i]

            potential_children = []
            if c == ".":
                potential_children.extend(node.children.values())
            elif c in node.children:
                potential_children.append(node.children[c])
            else: #not current character mismatch
                return  
            
            for child in potential_children:
                # there's technically no skipping we still have to check all to know
                node = child
                dfs(i+1, node)
                
        dfs(0, node)
        # scan the possible nodes 
        if len(possible_end_nodes) > 0:
            #scan for count >0 
            for possible_node in possible_end_nodes:
                if possible_node.count > 0:
                    return True
        return False # all possible node counts 0 or 




