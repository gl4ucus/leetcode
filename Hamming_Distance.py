class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = list(bin(x)[2:])
        y_bin = list(bin(y)[2:])

        x_len = len(x_bin)
        y_len = len(y_bin)
        
        if x_len > y_len:
            y_bin = ['0'] * (x_len - y_len) + y_bin
        else:
            x_bin = ['0'] * (y_len - x_len) + x_bin
        
        res = 0
        for i in range(0, len(x_bin)):
            if x_bin[i] != y_bin[i]:
                res += 1
                
        return(res)