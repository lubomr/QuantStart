class Position(object):
    def __init__(
        self, side, market, units,
        exposure, avg_price, cur_price
    ):
        self.side = side
        self.market = market
        self.units = units
        self.exposure = exposure
        self.avg_price = avg_price
        self.cur_price = cur_price
        self.profit_base = self.calculate_profit_base()
        self.profit_perc = self.calculate_profit_perc()

    def calculate_pips(self):
        pass
        #mult = 1.0
        #if self.side == "SHORT":
        #    mult = -1.0
        #return mult * (self.cur_price - self.avg_price)

    def calculate_profit_base(self):
        pass
        #pips = self.calculate_pips()
        #return pips * self.exposure / self.cur_price

    def calculate_profit_perc(self):
        pass
        #return self.profit_base / self.exposure * 100.0

    def update_position_price(self, cur_price):
        pass
#        self.cur_price = cur_price
#        self.profit_base = self.calculate_profit_base()
#        self.profit_perc = self.calculate_profit_perc()
