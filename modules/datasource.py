import akshare as ak
import pandas as pd


class DataSource:

    @staticmethod
    def get_stock_pool():

        print("开始获取A股股票池...")

        df = ak.stock_zh_a_spot_em()

        print(f"原始股票数量: {len(df)}")

        # 保留需要字段
        df = df[
            [
                "代码",
                "名称",
                "最新价",
                "涨跌幅",
                "成交量",
                "成交额",
                "市盈率-动态"
            ]
        ]

        # 去掉ST
        df = df[
            ~df["名称"].str.contains(
                "ST",
                na=False
            )
        ]

        # 排除创业板
        df = df[
            ~df["代码"].astype(str).str.startswith("300")
        ]

        # 排除科创板
        df = df[
            ~df["代码"].astype(str).str.startswith("688")
        ]

        # 排除北交所
        df = df[
            ~df["代码"].astype(str).str.startswith("8")
        ]

        # 股价限制
        df = df[
            (df["最新价"] > 0)
            &
            (df["最新价"] <= 100)
        ]

        print(f"过滤后股票数量: {len(df)}")

        return df