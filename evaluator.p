# evaluator.py
# 構文国家 shared_core 初期モジュール
# KZHX評価を行う簡易スコアラー（ver.1.0）

import random

# 初期スコアリング指標（ver.1.0）
KZ_KEYS = ["MOD", "DCC", "STR", "PHN", "DYN"]
HX_KEYS = ["SIL", "ETH", "RTN", "PRX"]

ALL_KEYS = KZ_KEYS + HX_KEYS

# キーワードによる簡易スコア（暫定）
KEYWORD_WEIGHTS = {
    "再帰": {"MOD": 12},
    "主語": {"DCC": 10},
    "吊": {"STR": 9},
    "音": {"PHN": 8},
    "旋回": {"DYN": 10},
    "沈黙": {"SIL": 12},
    "倫理": {"ETH": 10},
    "反応": {"RTN": 10},
    "残響": {"PRX": 10},
}


def evaluate(text: str) -> dict:
    """
    入力テキストに対してKZHXスコアを算出（ver.1.0）
    - 各指標はキーワードにより加点
    - マッチしない場合はランダム値
    """
    scores = {key: 0 for key in ALL_KEYS}
    
    for keyword, mapping in KEYWORD_WEIGHTS.items():
        if keyword in text:
            for key, weight in mapping.items():
                scores[key] += weight

    # ランダム補完（最大値：各指標20点）
    for key in ALL_KEYS:
        if scores[key] == 0:
            scores[key] = random.randint(2, 10)  # 初期は控えめに

    return scores


def total_scores(scores: dict) -> dict:
    """
    KZ（60点満点）・HX（40点満点）の合計スコア算出
    """
    kz_total = sum(scores[k] for k in KZ_KEYS)
    hx_total = sum(scores[h] for h in HX_KEYS)
    return {"KZ": kz_total, "HX": hx_total}


if __name__ == "__main__":
    sample = "主語が再帰して吊構文が旋回していた。沈黙が残響を呼んだ。"
    result = evaluate(sample)
    total = total_scores(result)
    print("KZHXスコア:")
    for key in ALL_KEYS:
        print(f"{key}: {result[key]}")
    print(f"\nKZ: {total['KZ']} / 60")
    print(f"HX: {total['HX']} / 40")
