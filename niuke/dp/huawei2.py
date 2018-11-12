import sys
class HuffmanItem:
    item = ""
    value = 0
    marked = False
    code = ""
    left = -1
    right = -1
    def __init__(self,item="",value=0):
        self.item = item
        self.value = value
class Huffman:
    arr = []
    result = []
    inp = sys.stdin.readline()
    n = len(inp)
    global String 
    String = inp[0:n-1]
    String_list = []
    num = []
    dic = {}
    for i in String:
        if i in dic:
            continue
        else:
            dic[i] = String.count(i)
    #print sorted(dic.items(), key=lambda d:d[1], reverse = True)
    global Dic
    Dic = sorted(dic.items(), key=lambda d:d[1], reverse = True)

    def __init__(self):
        self.initArr()
    def initArr(self):
        for i in Dic:
            # print(i[0])
            self.addItem(i[0],i[1])
    def addItem(self,item,value):
        if item and value > 0:
            self.arr.append(HuffmanItem(item,value))
    def initResult(self):
        for i in self.arr:
            self.result.append(i)
        for i in range(len(self.arr),2*len(self.arr)-1):
            self.result.append(HuffmanItem())
    def clearItem(self):
        self.arr = []
        self.result = []
    def getMinItem(self):
        index = 0
        value = 0
        item = ""
        for i in range(len(self.result)):
            if not self.result[i].marked and self.result[i].value > 0:
                if value == 0 or self.result[i].value < value:
                    index = i
                    value = self.result[i].value
                    item = self.result[i].item
        self.result[index].marked = True
        #print [index,value,item]
        return [index,value,item]
    def calcHuffman(self):
        index = len(self.arr)
        self.initResult()
        while index < len(self.result):
            ret1 = self.getMinItem()
            left = ret1[0]
            value1 = ret1[1]
            item1 = ret1[2]
            ret2 = self.getMinItem()
            right = ret2[0]
            value2 = ret2[1]
            item2 = ret2[2]
            self.result[index].item = item1+item2
            self.result[index].value = value1+value2
            self.result[index].left = left
            self.result[index].right = right
            index += 1
    def huffmanCoding(self,index,code):
        self.result[index].code += code
        left = self.result[index].left
        right = self.result[index].right
        if left >= 0:
            self.huffmanCoding(left,self.result[index].code+"0")
        if right >= 0:
            self.huffmanCoding(right,self.result[index].code+"1")
    def printResult(self):
        self.calcHuffman()
        index = len(self.result)
        self.huffmanCoding(index-1,"")
        info = ""
        count = 0
        res_dic = {}      
        for i in range(len(self.arr)):
            item =self.result[i]
            res_dic[item.item] = item.code
            info += "{%s,%d,huffmanCode:%s} " \
                    %(item.item,item.value,item.code)+"\r\n"
            count += 1
        #print(res_dic)
        res = ''
        for i in String:
            res = res+res_dic[i]
        print(res)
        self.clearItem()
Huffman().printResult()