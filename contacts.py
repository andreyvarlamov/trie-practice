class Node:
    children = {}
    complete = False
    # added words_count instead of recursive numChildrenUnder - much faster
    words_count = 0
    
    def __init__(self, letter, complete):
        self.letter = letter
        self.complete = complete
        self.children = {}
        self.words_count = 0
        
    """def addChild(self, child):
        self.children[child.letter] = child
        return child"""
    
    def addChild(self, letter, complete):
        child = Node(letter, complete)
        self.children[letter] = child
            
        return self.children[letter]
    
    def hasChild(self, letter):
        if letter in self.children:
            return self.children[letter]
        else:
            return None
        
    def numChildren(self):
        return len(self.children)
    
    ########## not used in the end - instead adding counter to each node when adding a new word
    def numChildrenUnder(self):
        #print('recurse')
        counter = 0
        if self.children:
            for letter in self.children:

                counter += self.children[letter].numChildrenUnder()
                
                if self.children[letter].complete:
                    counter += 1
            
           
        return counter

class Trie:
    heads = {}
    
    # not used - for practice - searches if the whole word exists or not
    def searchWord(self, word):
        length = len(word)
        if word[0] in self.heads:
            pointer = self.heads[word[0]]
            for index in range(1,length):
                pointer = pointer.hasChild(word[index])
                if not pointer:
                    return False
                
                if pointer.complete and index+1==length:
                    return True

            return False   # this returns none for some reason      
        else:
            return False
        
    def searchPartial(self, word):
        length = len(word)
        count = 0
        pp = None
        if word[0] in self.heads:
            pointer = self.heads[word[0]]
            for index in range(1,length):
                count = pointer.words_count
                pointer = pointer.hasChild(word[index])
                if not pointer:
                    return 0
                else:
                    count = pointer.words_count
                
            if length == 1:
                count = pointer.words_count
                
            return count
        else:
            return 0
    
    def addWord(self, word):
        length = len(word)
        if word[0] not in self.heads:
            self.heads[word[0]] = Node(word[0], length==1)
            
        pointer = self.heads[word[0]]    
        for index in range(1,length):
            pointer.words_count += 1
            if not pointer.hasChild(word[index]):
                pointer = pointer.addChild(word[index], index+1==length)
            else:
                pointer = pointer.hasChild(word[index])
                
        pointer.words_count += 1
    

n = int(input().strip())

trie = Trie()

for a0 in range(n):
    op, contact = input().strip().split(' ')
    
    if op == 'find':
        print(trie.searchPartial(contact))
    elif op == 'add':
        trie.addWord(contact)
