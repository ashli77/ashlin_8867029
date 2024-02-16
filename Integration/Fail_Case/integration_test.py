from main import InterestCalculator
import unittest

class TestFinancialAppIntegration(unittest.TestCase):

    def test_savings_account_interest(self):
        account_balance = 5000
        annual_interest_rate = 2.5
        years = [1, 3, 5]

        simple_interests = [InterestCalculator.simple_interest(account_balance, annual_interest_rate, year) for year in years]
        expected_interests = [126.0, 375.0, 625.0]

        self.assertEqual(simple_interests, expected_interests)

    def test_investment_account_interest(self):
        initial_investment = 10000
        annual_interest_rate = 4
        time_in_years = 5
        compounding_frequency = 4
        compound_interest = InterestCalculator.compound_interest(initial_investment, annual_interest_rate, time_in_years, compounding_frequency)
        expected_interest = initial_investment * (1 + annual_interest_rate / (100 * compounding_frequency)) ** (compounding_frequency * time_in_years) - initial_investment

        self.assertAlmostEqual(compound_interest, expected_interest, places=2)