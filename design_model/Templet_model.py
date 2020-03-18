# -*- coding:utf-8 -*-
"""
 模板模式
"""


class StockQueryDevice():
    stock_code = '0'
    stock_price = 0.0

    def login(self, usr, pwd):
        pass

    def setCode(self, code):
        self.stock_code = code

    def queryPrice(self):
        pass

    def shwoPrice(self):
        pass

    def operateQuery(self, usr, pwd, code):
        if not self.login(usr, pwd):
            return False
        self.setCode(code)
        self.queryPrice()
        self.shwoPrice()
        return True


class WebAstockQueryDevice(StockQueryDevice):
    def login(self, usr, pwd):
        if usr == 'myStockA' and pwd == 'myPwdA':
            print ('Web A:login ok... user:%s pwd:%s' % (usr, pwd))
            return True
        else:
            print ('Web A:login ERROR... user:%s pwd:%s' % (usr, pwd))
            return False

    def queryPrice(self):
        print ('Web A Querying... code:%s' % self.stock_code)
        self.stock_code = 20.00

    def showPrice(self):
        print ('Web A Stock Price ... code:%s price:%s' % (self.stock_code, self.stock_price))


class WebBStockQueryDevice(StockQueryDevice):
    def login(self, usr, pwd):
        if usr == 'myStockB' and pwd == 'myPwdB':
            print ('Web B:login ok ... usr:%s pwd:%s' % (usr, pwd))
            return True
        else:
            print ('Web B:login ERROR... usr:%s pwd:%s' % (usr, pwd))
            return False

    def queryPrice(self):
        print ('Web B Querying ... code:%s' % self.stock_code)
        self.stock_price = 30.00

    def shwoPrice(self):
        print ('Web B Stock Price ... code:%s price:%s' % (self.stock_code, self.stock_price))


if __name__ == '__main__':
    web_a_query_dev = WebAstockQueryDevice()
    web_a_query_dev.operateQuery('myStockA', 'myPwdA', '12345')
