class node:
    def __init__(self, freq = 0, left = None, right = None):
        self.left = left
        self.right = right
        self.frequency = freq
        self.char = ''
class Priority_queue:
    def __init__(self, n, list):
        self.heap = list
        self.len = n
        self.build_heap()
    def build_heap(self):
        i = (self.len // 2) - 1
        while i >= 0:
            self.heapify(i)
            i -= 1
    def heapify(self, ind): 
        mn = ind
        l = ind * 2 + 1
        r = ind * 2 + 2
        if l < self.len and self.heap[mn].frequency > self.heap[l].frequency:
            mn = l
        if r < self.len and self.heap[mn].frequency > self.heap[r].frequency:
            mn = r
        if mn != ind:
            self.heap[ind], self.heap[mn] = self.heap[mn], self.heap[ind]
            self.heapify(mn)
    def insert(self, val):
        self.heap.append(val)
        self.len += 1
        self.build_heap()
    def delete(self):
        r = self.heap[0]
        if self.len > 1:
            self.heap[0] = self.heap.pop()
            self.len -= 1
            self.build_heap()
        else:
            self.heap = []
            self.len = 0
        return r
def encode(val, code, dic):
    if val.left == None and val.right == None:
        dic[val.char] = code
        return
    encode(val.left, (code + '0'), dic)
    encode(val.right, (code + '1'), dic)
if __name__ == '__main__':
    s = input()
    dic, list, ind = {}, [], 0
    for i in s:
        if i in dic:
            list[dic[i]].frequency += 1
        else:
            list.append(node(1))
            list[ind].char = i
            dic[i] = ind
            ind += 1               
    list = Priority_queue(ind, list)
    while list.len > 1:
        a = list.delete()
        b = list.delete()
        list.insert(node((a.frequency + b.frequency), a, b))
    tree_root = list.heap[0]        
    #encode part
    encode(tree_root, '' ,dic)
    encoded_string = ""
    for i in dic:
        print(i, dic[i])
    print()
    for i in s:
        encoded_string += dic[i]
    print(encoded_string)
    print()
    #decode part NOTE: we have to send the tree with the encoded string as well
    curr = tree_root
    decoded_string = ""
    for i in encoded_string:
        if i == '0':
            curr = curr.left
        else:
            curr = curr.right
        if curr.char != '':
            decoded_string += curr.char
            curr = tree_root
    print(decoded_string)