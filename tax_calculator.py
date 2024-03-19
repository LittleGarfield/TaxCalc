class TaxCalculator:
    @staticmethod
    def calc_bonus_tax(bonus: float):
        """ 奖金计税（bonus纳入奖金计税的数额） """
        monthly_bonus = bonus / 12
        if monthly_bonus <= 3000:
            tax = bonus * 0.03
        elif 3000 < monthly_bonus <= 12000:
            tax = bonus * 0.1 - 210
        elif 12000 < monthly_bonus <= 25000:
            tax = bonus * 0.2 - 1410
        elif 25000 < monthly_bonus <= 35000:
            tax = bonus * 0.25 - 2660
        elif 35000 < monthly_bonus <= 55000:
            tax = bonus * 0.3 - 4410
        elif 55000 < monthly_bonus <= 80000:
            tax = bonus * 0.35 - 7160
        else:
            tax = bonus * 0.45 - 15160
        return tax

    @staticmethod
    def calc_income_tax(income: float):
        """ 个税计税（income为累积应纳税所得额，可查阅个税APP获得）"""
        if income <= 36000:
            tax = income * 0.03
        elif 36000 < income <= 144000:
            tax = income * 0.1 - 2520
        elif 144000 < income <= 300000:
            tax = income * 0.2 - 16920
        elif 300000 < income <= 420000:
            tax = income * 0.25 - 31920
        elif 420000 < income <= 660000:
            tax = income * 0.3 - 52920
        elif 660000 < income <= 960000:
            tax = income * 0.35 - 85920
        else:
            tax = income * 0.45 - 181920
        return tax

    @staticmethod
    def calc_tax(income: float, bonus: float, cash):
        """ 计算总税额（cash为将奖金部分以现金形式发放的数额，此部分单独计税，其它部分与个税合并计税）"""
        income_tax = TaxCalculator.calc_income_tax(income=float(income) + bonus - float(cash))
        bonus_tax = TaxCalculator.calc_bonus_tax(bonus=float(cash))
        total_tax = income_tax + bonus_tax
        return total_tax, income_tax, bonus_tax


def test(income: float, bonus: float):
    min_tax = income + bonus
    min_tax_item = None
    items = []
    cashes = [c for c in range(0, round(bonus), 1000)]
    cashes.append(bonus)
    for cash in cashes:
        tax, income_tax, bonus_tax = TaxCalculator.calc_tax(income=income, bonus=bonus, cash=cash)
        print('\t现金=%.1f, 总税额=%.1f = %.1f(个税) + %.1f(奖金税)' % (cash, tax, income_tax, bonus_tax))
        item = (cash, tax, income_tax, bonus_tax)
        items.append(item)
        if tax < min_tax:
            min_tax = tax
            min_tax_item = item
    print('最小税额组合：\n\t现金=%.1f, 总税额=%.1f = %.1f(个税) + %.1f(奖金税)' % (min_tax_item[0], min_tax_item[1],
                                                                 min_tax_item[2], min_tax_item[3]))


if __name__ == '__main__':
    _income = float(input("您的累积应纳税所得额（单位：元）: "))
    _bonus = float(input("您的奖金总额（单位：元）: "))
    test(income=_income, bonus=_bonus)
