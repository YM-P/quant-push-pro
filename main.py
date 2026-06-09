from modules.ranker import Ranker

stocks = [
    ("000001", 12.5),
    ("600869", 5.8),
    ("600050", 7.2)
]

for code, price in stocks:

    result = Ranker.calc_total_score(
        code,
        price
    )

    print(result)