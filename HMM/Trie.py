import pickle
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end = -1

    def str_format(self, word):
        return word.lower()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        word=self.str_format(word)
        curNode = self.root
        for c in word:
            if not c in curNode:
                curNode[c] = {}
            curNode = curNode[c]
        curNode[self.end] = 0

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        word=self.str_format(word)
        curNode = self.root
        for c in word:
            if not c in curNode:
                return False
            curNode = curNode[c]

        # Doesn't end here
        if not self.end in curNode:
            return False

        return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        prefix=self.str_format(prefix)
        curNode = self.root
        for c in prefix:
            if not c in curNode:
                return False
            curNode = curNode[c]

        return True
    def search_part(self,string):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        word=""
        string=self.str_format(string)
        curNode = self.root
        while len(string) > 0:
            c=string[0]
            if not c in curNode:
                if len(word)==0:
                    word=c
                    string=string[1:]
                return [word,string]
            curNode = curNode[c]
            # if len(string)>1:
            string=string[1:]
            # else:
            #     string=''
            word+=c
        # Doesn't end here
        return [word,string]
    def save(self):
        with open("trie.pkl", 'wb') as file:
            pickle.dump(self,file)
# Your Trie object will be instantiated and called as such:
if __name__ == '__main__':# Initialize Trie
    # obj = Trie()
    # with open("p_count", 'rb') as file:
    #     p_count = pickle.load(file)
    # with open("potential_w", 'rb') as file:
    #     potential_w = pickle.load(file)
    # tries=list(p_count.keys())
    # tries+=list(potential_w.keys())
    # for key in tries:
    #     obj.insert(key)
    # obj.save()
    # print(len(tries))
    with open("trie",'rb') as file:
        trie=pickle.load(file)
    pinyin=input("Please enter pinyin:")
    result=[]
    while len(pinyin)>0:
        word,pinyin=trie.search_part(pinyin)
        result.append(word)
    print(result)
