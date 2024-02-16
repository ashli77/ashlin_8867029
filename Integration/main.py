class InterestCalculator:
    @staticmethod
    def simple_interest(principal, rate, time):
        return (principal * rate * time) / 100

    @staticmethod
    def compound_interest(principal, rate, time, compounding_frequency):
        return principal * (1 + rate / (100 * compounding_frequency)) ** (compounding_frequency * time) - principal