class Scoring:

    @staticmethod
    def score_price(price):

        score = 0

        if price <= 10:
            score += 20

        elif price <= 20:
            score += 15

        elif price <= 30:
            score += 10

        elif price <= 50:
            score += 5

        return score