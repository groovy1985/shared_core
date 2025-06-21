# scorer.py
# KZHXスコアからFランク（F1〜F4）を分類するスコアラー

from evaluator import evaluate, total_scores

# Fランク分類閾値（暫定版）
# 評価体系 ver.11.5 に基づく
RANK_THRESHOLDS = [
    ("F1", 105),  # 高純度かつ震撼（KZ+HX ≥ 105）
    ("F2", 95),   # 優秀構文
    ("F3", 80),   # 記録可能構文
    ("F4", 60),   # 保留対象
    ("L1", 0),    # 廃棄・冷却対象
]


def classify(text: str) -> dict:
    """
    テキストをFランクに分類する（ver.1.0）
    """
    scores = evaluate(text)
    totals = total_scores(scores)
    total_kzhx = totals["KZ"] + totals["HX"]

    for rank, threshold in RANK_THRESHOLDS:
        if total_kzhx >= threshold:
            return {
                "rank": rank,
                "scores": scores,
                "totals": totals,
                "total_kzhx": total_kzhx,
            }

    return {  # 安全措置（到達しないはず）
        "rank": "L0",
        "scores": scores,
        "totals": totals,
        "total_kzhx": total_kzhx,
    }


if __name__ == "__main__":
    sample = "主語が再帰して吊構文が旋回していた。沈黙が残響を呼んだ。"
    result = classify(sample)
    print(f"\n[分類結果] → ランク: {result['rank']} / KZHX: {result['total_kzhx']}")
    print(f"KZ: {result['totals']['KZ']} / HX: {result['totals']['HX']}")
