import math as m
import decimal as d

# Paper Tape Class
# Author=rinscr3003

class PaperTape(object):
    x = []
    dx = []
    d2x = []
    T = d.Decimal("0.1")

    def __init__(self, x_list, t, k):  # number in list MUST be DECIMAL compatible
        l = len(x_list)
        for i in x_list:
            self.x.append(d.Decimal(str(i))*d.Decimal(str(k)))
        for i in range(1, l):
            self.dx.append(self.x[i] - self.x[i - 1])
        for i in range(1, len(self.dx)):
            self.d2x.append(self.dx[i] - self.dx[i - 1])
        self.T = d.Decimal(str(t))

    # 求两点间加速度（二段逐差法）
    def get_acc(self, j, k):
        if(j == k):
            return d.Decimal(0)
        sign = d.Decimal(1)
        if (j > k):  # 反向求加速度
            sign = d.Decimal(-1)
            r = k
            k = j
            j = r
        l = len(self.x)
        if (j > l or k > l):  # 数据超范围
            return d.Decimal(0)
        n = k - j  # n段位移
        a = d.Decimal(0)
        if (n % 2 == 0):  # 偶数段位移（j,k均是点号）
            mid = (j + k) / 2
            x1 = sum(self.dx[j:int(mid)])
            x2 = sum(self.dx[int(mid):k])
            a = (x2 - x1) / ((d.Decimal(n) * self.T) ** 2)
        else:  # 奇数段位移
            mid = m.ceil((j + k) / 2)
            x1 = sum(self.dx[j:int(mid)])
            x2 = sum(self.dx[int(mid)-1:k])
            a = (x2 - x1) / ((d.Decimal(n) * self.T) ** 2)
        return a*sign

    # 求总加速度（逐差法）
    def get_accz(self):
        return self.get_acc(0,len(self.dx))

    # 求所有段位移间加速度
    def get_acca(self):
        a = []
        for i in self.d2x:
            a.append(i / (self.T ** 2))
        return a