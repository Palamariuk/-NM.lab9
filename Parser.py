class Parser:
    def __init__(self, arg):
        self.coefs = arg

    def get_tabulation_points(self, step = 0.001):
        assert step > 0
        x = []
        y = []
        i = -100
        while i <= 100:
            x.append(i)
            y.append(sum([self.coefs[k] * (i ** k) for k in range(len(self.coefs))]))
            i += step
        return (x, y)
    
    def get_string(self, variable = 'x'):
        res_string = ""
        for i in range(len(self.coefs)):
            res_string += '({:+.3f}) * {} + '.format(
                self.coefs[i],
                f"{variable}^{i}" if i > 0 else ""
            )
        return res_string[:-2]