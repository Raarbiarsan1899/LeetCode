class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        output = []
        for i in range(1, n + 1):
            tmp = ''
            if i % 3 == 0:
                tmp += 'Fizz'
            if i % 5 == 0:
                tmp += 'Buzz'
            if len(tmp) != 0:
                output.append(tmp)
            else:
                output.append(str(i))
                
        return output
