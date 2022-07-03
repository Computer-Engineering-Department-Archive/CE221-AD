class DLLNode:
    def __init__(self, pre=None, data=None, link=None):
        self.data = data
        self.link = link
        self.pre = pre


class DLL:

    def __init__(self):
        self.head = None
        self.last = None
        self.len = 0

    def __getitem__(self, index):
        h = self.head
        for i in range(index):
            h = h.link
        return h.data

    def __delitem__(self, index):
        if index == 0:
            self.delete_first()
        elif index == self.len:
            self.delete_last()
        else:
            h = self.head
            for i in range(1, index):
                h = h.link
            h.link = h.link.link
            h.link.pre = h
            self.len -= 1

    def __setitem__(self, index, value):
        del self[index]
        self.insert_index(index, value)


    def __len__(self):
        return self.len

    def add_first(self, value):
        newnode = DLLNode(data=value)
        if self.head is None:
            self.head = newnode
            self.last = newnode
        else:
            newnode.link = self.head
            self.head.pre = newnode
            self.head = newnode
        self.len += 1

    def add_last(self, value):
        newnode = DLLNode(data=value)
        if self.head is None:
            self.add_first(value)
        else:
            self.last.link = newnode
            newnode.pre = self.last
            self.last = newnode
            self.len += 1

    def traverse(self):
        a = self.head
        while a:
            print(a.data)
            a = a.link

    def search(self, integer):
        a = self.head
        while a:
            if a.data == integer:
                return a
            a = a.link


    def delete_first(self):
        if self.head is None:
            return
        else:
            self.head = self.head.link
            self.head.pre = None
            self.len -= 1

    def delete_last(self):
        if self.head is None:
            return
        else:
            self.last = self.last.pre
            self.last.link = None
            self.len -= 1

    def delete_node(self, value):
        h = self.head
        while h:
            while True:
                if self.head.data == value:
                    self.delete_first()
                    h = self.head
                else:
                    break
            if self.last.data == value:
                self.delete_last()
            if h.data == value:
                h.pre.link = h.link
                h.link.pre = h.pre
                self.len -= 1
            h = h.link

    def insert_index(self, index, value):  # its wrong
        newnode = DLLNode(data=value)
        if index == 0:
            self.add_first(value)
        elif index == self.len:
            self.add_last(value)
        else:
            h = self.head
            a = 1
            while a < index:
                h = h.link
                a += 1
            newnode.pre = h
            newnode.link = h.link
            h.link = newnode
            newnode.link.pre = newnode
            self.len += 1


def count_bam_bish(dll: DLL):
    counter = 0  # counter for bam bishs
    h = dll.head.link  # از دومین آیتم شروع کردم، چون اولین آیتم، آیتم کناری نداره و نمیتونم مقایسه کنم
    while h.link:  # تا یکی مونده به آخرین داده پیش میرم. چون بعد از آخرین داده هم None هست
        if h.data > h.pre.data and h.data > h.link.data:
            counter += 1
        h = h.link
    print(counter)


dll = DLL()
dll.add_first(3)
dll.add_last(2)
dll.add_last(8)
dll.add_last(2)
dll.add_last(20)
dll.add_last(1)


count_bam_bish(dll)



