import akshare as ak
import pandas as pd


class StockPool:

    @staticmethod
    def get_main_board():

        print("获取A股代码池...")

        df = ak.stock_info_a_code_name()

        print("原始数量:", len(df))

        # 排除创业板
        df = df[
            ~df["code"].astype(str).str.startswith("300")
        ]

        # 排除科创板
        df = df[
            ~df["code"].astype(str).str.startswith("688")
        ]

        # 排除北交所
        df = df[
            ~df["code"].astype(str).str.startswith(("4", "8"))
        ]

        # 排除ST
        df = df[
            ~df["name"].str.contains("ST", na=False)
        ]

        print("过滤后数量:", len(df))

        return df