def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return result
    except ZeroDivisionError:
       return "Error: Division By Zero"
    except ValueError:
        return "Error : Invalid input"