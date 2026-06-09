from modules.scoring import Scoring
from modules.financial_filter import FinancialFilter


class Ranker:

    @staticmethod
    def calc_total_score(symbol, price):

        price_score = Scoring.score_price(price)

        financial_score = \
            FinancialFilter.get_financial_score(
                symbol
            )

        total_score = (
            price_score
            + financial_score
        )

        return {
            "symbol": symbol,
            "price_score": price_score,
            "financial_score": financial_score,
            "total_score": total_score
        }