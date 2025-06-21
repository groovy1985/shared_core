# file_writer.py
# 構文国家Bot別保存処理＋meta生成（ver.1.0）

import os
import json
from datetime import datetime
from scorer import classify

# 保存ディレクトリルート
BASE_DIR = "output"

# Bot名ごとのフォルダ
BOT_FOLDERS = {
    "death": "DEATH",
    "poemkun": "POEMKUN",
    "babaa": "BABAA",
    "bukkoresyntax": "BUKKORE",
}


def save_text(bot_name: str, text: str):
    """
    評価＋保存処理（textをbot名別に保存＋meta.json出力）
    """
    assert bot_name in BOT_FOLDERS, f"未知のbot名: {bot_name}"
    
    result = classify(text)
    date_str = datetime.now().strftime("%Y-%m-%d")
    timestamp = datetime.now().strftime("%H%M%S")

    folder = os.path.join(BASE_DIR, BOT_FOLDERS[bot_name], date_str)
    os.makedirs(folder, exist_ok=True)

    # 本文保存
    file_id = f"{timestamp}_{result['rank']}"
    text_path = os.path.join(folder, f"{file_id}.txt")
    with open(text_path, "w", encoding="utf-8") as f:
        f.write(text)

    # meta保存
    meta = {
        "rank": result["rank"],
        "kz": result["totals"]["KZ"],
        "hx": result["totals"]["HX"],
        "total_kzhx": result["total_kzhx"],
        "scores": result["scores"],
        "timestamp": timestamp,
        "bot": bot_name,
    }
    meta_path = os.path.join(folder, f"{file_id}_meta.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    print(f"✅ 保存完了: {text_path}")


if __name__ == "__main__":
    sample_text = "吊構文に再帰した紙が旋回して沈黙を破った。倫理と残響がぶつかった。"
    save_text("poemkun", sample_text)
