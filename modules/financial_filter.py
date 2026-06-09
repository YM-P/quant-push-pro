import akshare as ak


class FinancialFilter:

    @staticmethod
    def get_financial_score(symbol):

        try:

            df = ak.stock_financial_abstract_ths(
                symbol=symbol
            )

            latest = df.iloc[-1]

            score = 0

            net_profit = str(
                latest["净利润"]
            )

            debt_ratio = str(
                latest["资产负债率"]
            )

            if "万" in net_profit \
                    or "亿" in net_profit:

                score += 20

            if "%" in debt_ratio:

                debt = float(
                    debt_ratio.replace("%", "")
                )

                if debt < 60:
                    score += 10

                elif debt < 70:
                    score += 5

            return score

        except Exception as e:

            print(
                f"{symbol}失败:",
                e
            )

            return 0