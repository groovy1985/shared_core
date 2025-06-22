# shared_core/file_writer.py

import os
import json
from datetime import datetime

def write_outputs(text, eval_result, classification, output_dir, file_id):
    """
    評価済構文とmeta情報を指定フォルダに保存する。

    Parameters:
        text (str): 評価対象の構文本文
        eval_result (dict): evaluatorの出力（KZHXスコア）
        classification (dict): scorerの出力（ランク、PRX、SC判定）
        output_dir (str): 保存先のBot別出力ディレクトリ（例："poemkun/output"）
        file_id (str): 保存ファイル名の接頭辞（例："01"）

    Returns:
        str: 保存先ファイルパス
    """
    rank = classification["rank"]
    date_str = datetime.now().strftime("%Y-%m-%d")

    # 本文保存パス
    text_dir = os.path.join(output_dir, rank)
    os.makedirs(text_dir, exist_ok=True)
    text_path = os.path.join(text_dir, f"{file_id}.txt")

    # meta保存パス
    meta_dir = os.path.join(output_dir, "meta")
    os.makedirs(meta_dir, exist_ok=True)
    meta_path = os.path.join(meta_dir, f"{file_id}_meta.json")

    # 保存処理
    with open(text_path, "w", encoding="utf-8") as f:
        f.write(text.strip())

    meta = {
        "date": date_str,
        "rank": rank,
        "KZ": eval_result.get("KZ"),
        "HX": eval_result.get("HX"),
        "KZ_scores": eval_result.get("KZ_scores"),
        "HX_scores": eval_result.get("HX_scores"),
        "PRX": classification.get("PRX"),
        "SC_candidate": classification.get("SC_candidate")
    }

    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)

    return text_path

# テスト実行例
if __name__ == "__main__":
    dummy_text = "構文の死体を運ぶ音がまだ濡れている。"
    dummy_eval = {
        "KZ": 48, "HX": 29,
        "KZ_scores": {"MOD": 12, "DCC": 8, "STR": 10, "PHN": 8, "DYN": 10},
        "HX_scores": {"SIL": 7, "ETH": 5, "RTN": 8, "PRX": 9}
    }
    dummy_class = {
        "rank": "F2", "KZ": 48, "HX": 29, "PRX": 9, "SC_candidate": True
    }

    write_outputs(dummy_text, dummy_eval, dummy_class, "poemkun/output", "01")
