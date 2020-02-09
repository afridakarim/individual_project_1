class Subtraction:

    @staticmethod
    def difference(minuend, subtrahend=None):
        if isinstance(minuend, list):
            return Subtraction.differenceList(minuend)
        return minuend - subtrahend

    @staticmethod
    def differenceList(valueList):
        result = 0
        for value in valueList:
            result = Subtraction.difference(result, value)

        return result