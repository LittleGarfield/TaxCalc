class TaxCalculator:
    @staticmethod
    def calc_bonus_tax(bonus: float):
        """ 奖金计税（单位：元）
        Args:
            bonus: 纳入奖金计税的金额
        Returns:
            奖金税金额
        """
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
    def calc_taxable_income_tax(taxable_income: float):
        """ 个税计税（单位：元）
        Args:
            taxable_income: 奖金实际发放年度的应纳税所得额，如2024年发的奖金，则为2024年的全年应纳税所得额
        Returns:
            个税金额
        """
        if taxable_income <= 36000:
            tax = taxable_income * 0.03
        elif 36000 < taxable_income <= 144000:
            tax = taxable_income * 0.1 - 2520
        elif 144000 < taxable_income <= 300000:
            tax = taxable_income * 0.2 - 16920
        elif 300000 < taxable_income <= 420000:
            tax = taxable_income * 0.25 - 31920
        elif 420000 < taxable_income <= 660000:
            tax = taxable_income * 0.3 - 52920
        elif 660000 < taxable_income <= 960000:
            tax = taxable_income * 0.35 - 85920
        else:
            tax = taxable_income * 0.45 - 181920
        return tax

    @staticmethod
    def calc_tax(taxable_income: float, bonus: float, cash):
        """ 计算总税额（单位：元）
        Args:
            taxable_income: 奖金实际发放年度的应纳税所得额，如2024年发的奖金，则为2024年的全年应纳税所得额
            bonus: 奖金金额
            cash: 奖金部分以现金形式发放的数额，此部分单独计税，其它部分与个税合并计税
        Returns:
            (总税额, 个税, 奖金税)
        """
        income_tax = TaxCalculator.calc_taxable_income_tax(float(taxable_income) + bonus - float(cash))  # 个税
        bonus_tax = TaxCalculator.calc_bonus_tax(float(cash))  # 奖金税
        total_tax = income_tax + bonus_tax  # 总税额
        return total_tax, income_tax, bonus_tax


def test(taxable_income: float, bonus: float):
    """ 打印所有组合，并且提示最优组合
    Args:
        taxable_income: 奖金实际发放年度的应纳税所得额，如2024年发的奖金，则为2024年的全年应纳税所得额
        bonus: 奖金金额
    Returns:
        无
    """
    min_tax = taxable_income + bonus
    min_tax_item = None
    items = []
    cashes = [c for c in range(0, round(bonus), 100)]
    cashes.append(bonus)
    for cash in cashes:
        tax, income_tax, bonus_tax = TaxCalculator.calc_tax(taxable_income, bonus, cash)
        item = f'\t现金:{cash}, 期权:{bonus - cash}, {tax:.1f}(总税额) = {income_tax:.1f}(个税) + {bonus_tax:.1f}(奖金税)'
        items.append(item)
        print(item)
        if tax < min_tax:
            min_tax = tax
            min_tax_item = item
    print(f'累积应纳税所得额：{taxable_income}\t奖金总额：{bonus}')
    print(f'最小税额组合：{min_tax_item.strip()}')


if __name__ == '__main__':
    _income = float(input("您的累积应纳税所得额（单位：元）: "))
    _bonus = float(input("您的奖金总额（单位：元）: "))
    test(_income, _bonus)
