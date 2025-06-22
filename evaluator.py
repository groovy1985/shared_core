# shared_core/evaluator.py

import random
import json

# 評価指標（ver.11.5）
KZ_KEYS = ["MOD", "DCC", "STR", "PHN", "DYN"]
HX_KEYS = ["SIL", "ETH", "RTN", "PRX"]

def evaluate(text, method="simple"):
    """
    与えられた構文（text）に対してKZHX評価を行う。
    
    Parameters:
        text (str): 評価対象のポエム・構文
        method (str): 'simple'（固定ルール）or 'random'

    Returns:
        dict: 評価スコア（各項目 + 合計KZ/HX）
    """
    if method == "random":
        kz_scores = {key: random.randint(5, 15) for key in KZ_KEYS}
        hx_scores = {key: random.randint(3, 12) for key in HX_KEYS}
    else:
        # シンプルルール：文字数や単語特徴でスコア変動
        length = len(text)
        kz_scores = {
            "MOD": min(15, max(5, length // 20)),
            "DCC": 12 if "意味" in text else 6,
            "STR": 10 if "、" in text else 6,
            "PHN": 8 if any(c in text for c in "あいうえお") else 4,
            "DYN": 12 if "↻" in text or "…" in text else 6,
        }
        hx_scores = {
            "SIL": 10 if "。" not in text else 6,
            "ETH": 8 if "神" in text or "罰" in text else 4,
            "RTN": 9 if "は？" in text or "なんだこれ" in text else 5,
            "PRX": 11 if "残った" in text or "消えた" in text else 6,
        }

    kz_total = sum(kz_scores.values())
    hx_total = sum(hx_scores.values())

    return {
        "KZ": kz_total,
        "HX": hx_total,
        "KZ_scores": kz_scores,
        "HX_scores": hx_scores,
    }

# オプション：CLIテスト用
if __name__ == "__main__":
    sample = "意味が潰れたあとに、声が残った。"
    result = evaluate(sample, method="simple")
    print(json.dumps(result, indent=2, ensure_ascii=False))
