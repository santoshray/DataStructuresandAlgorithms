## Represents a single node in the Trie
import copy
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children ={}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char]=TrieNode()

    def find_words(self, prefix):
        matches = []
        if self.is_word:
            matches += [prefix]
            print(matches ,prefix)
        for (char, node) in self.children.items():
            print(char , prefix)
            matches += node.find_words(prefix+ char)

        return matches

        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.trie_root = TrieNode()


    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.trie_root

        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]

        current_node.is_word = True


    def match(self, prefix):
        ## Return all matching words in the tree
        node = self.find(prefix)
        if node:
            return node.find_words(prefix)
        else:
            return []


    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.trie_root
        for char in prefix:
            if char not in current_node.children:
                return None 
            current_node = current_node.children[char]

        return current_node



    def get_words(self,trie_node,prefix):
        matches = []
        if trie_node.is_word:
            matches += [prefix]
            print(matches ,prefix)
        for (char, node) in trie_node.children.items():
            print(char , prefix)
            matches += self.get_words(node,prefix+ char)

        return matches





    def suffixes(self,prefix=''):
        
        cn = self.find (prefix)
        print(prefix)
        print(cn.children.items())
#        return cn.find_words('')
        return self.get_words(cn,'')


if __name__ == '__main__':

    MyTrie = Trie()
    wordList = [
        "ant", "anthology", "antagonist", "antonym", 
        "fun", "function", "factory", 
        "trie", "trigger", "trigonometry", "tripod"
    ]

    for word in wordList:
        MyTrie.insert(word)


    print( MyTrie.suffixes("fu"))
