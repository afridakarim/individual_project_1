class Multipication:

    @staticmethod
    def product(multiplier, multiplicand=None):
        if isinstance(multiplier, list):
            return Multipication.productList(multiplier)
        return multiplier * multiplicand

    @staticmethod
    def productList(valueList):
        result = 0
        for value in valueList:
            result = Multipication.product(result, value)

        return result