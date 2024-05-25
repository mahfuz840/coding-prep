class SuperStack:

    def __init__(self):
        self.arr = []

    def push(self, num: int):
        self.arr.append(num)

    def pop(self):
        if self.isEmpty():
            raise Exception('Underflow')
        
        val = self.arr.pop()

    def isEmpty(self):
        return len(self.arr) == 0
    
    def getMax(self):
        max = 0

        for num in self.arr:
            if num > max:
                max = num
        
        return max
    

st = SuperStack()
st.push(10)
st.push(1)
st.push(20)
st.pop()
st.push(100)
print(st.getMax())
