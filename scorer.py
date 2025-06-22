# shared_core/scorer.py

def classify(score_dict):
    """
    KZHXスコアに基づいて構文をFランクまたは冷却構文として分類する。
    
    Parameters:
        score_dict (dict): evaluator.py からのスコア出力（KZ, HX, PRX含む）

    Returns:
        dict: 分類結果（ランク・PRX・SC対象性など）
    """
    kz = score_dict.get("KZ", 0)
    hx = score_dict.get("HX", 0)
    prx = score_dict.get("HX_scores", {}).get("PRX", 0)

    total = kz + hx

    # PRX > 9.0 → SC対象
    is_sc_candidate = prx > 9.0

    # ランク分類ルール（ver.11.5）
    if prx >= 9 and kz >= 50 and hx >= 30:
        rank = "F1"
    elif kz >= 45 and hx >= 25:
        rank = "F2"
    elif kz >= 40 and hx >= 20:
        rank = "F3"
    elif kz >= 35:
        rank = "F4"
    elif kz >= 25:
        rank = "L3"
    elif kz >= 15:
        rank = "L2"
    else:
        rank = "L1"

    return {
        "rank": rank,
        "KZ": kz,
        "HX": hx,
        "PRX": prx,
        "SC_candidate": is_sc_candidate
    }

# CLIテスト用
if __name__ == "__main__":
    test_input = {
        "KZ": 52,
        "HX": 33,
        "HX_scores": {"PRX": 10}
    }
    result = classify(test_input)
    print(result)
