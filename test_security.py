import unittest

def calculate_risk_score(suspicious, failed_logins):
    """Функция расчёта риск-скора (скопирована из generate_data.py)"""
    risk_score = suspicious * 2 + failed_logins * 3
    if risk_score > 25:
        level = "высокий"
    elif risk_score > 12:
        level = "средний"
    else:
        level = "низкий"
    return risk_score, level

class TestRiskCalculation(unittest.TestCase):

    def test_zero_risk(self):
        score, level = calculate_risk_score(0, 0)
        self.assertEqual(score, 0)
        self.assertEqual(level, "низкий")

    def test_low_risk(self):
        score, level = calculate_risk_score(5, 0)
        self.assertEqual(score, 10)
        self.assertEqual(level, "низкий")

    def test_medium_risk_suspicious(self):
        score, level = calculate_risk_score(7, 0)  # 14
        self.assertEqual(score, 14)
        self.assertEqual(level, "средний")

    def test_medium_risk_failed(self):
        score, level = calculate_risk_score(0, 5)  # 15
        self.assertEqual(score, 15)
        self.assertEqual(level, "средний")

    def test_high_risk(self):
        score, level = calculate_risk_score(10, 2)  # 20+6=26
        self.assertEqual(score, 26)
        self.assertEqual(level, "высокий")

    def test_boundary_25(self):
        score, level = calculate_risk_score(8, 3)  # 16+9=25
        self.assertEqual(score, 25)
        self.assertEqual(level, "средний")

        score2, level2 = calculate_risk_score(9, 3)  # 18+9=27
        self.assertEqual(level2, "высокий")

if __name__ == '__main__':
    unittest.main()