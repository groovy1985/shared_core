# control_center/dispatch.py

import os
import json
from shared_core.evaluator import evaluate
from shared_core.scorer import classify
from shared_core.file_writer import write_outputs

def process_post(text, output_dir, file_id, mode="simple"):
    """
    単一の構文ポストを評価・分類・保存する処理。

    Parameters:
        text (str): 評価対象の構文
        output_dir (str): Botごとの出力ディレクトリ（例："poemkun/output"）
        file_id (str): ファイル名接頭辞（例："01"）
        mode (str): 評価モード（"simple" or "random"）

    Returns:
        dict: 評価＋分類結果
    """
    eval_result = evaluate(text, method=mode)
    classification = classify(eval_result)
    saved_path = write_outputs(text, eval_result, classification, output_dir, file_id)

    return {
        "text_path": saved_path,
        "rank": classification["rank"],
        "PRX": classification["PRX"],
        "SC_candidate": classification["SC_candidate"]
    }

# CLIテスト用
if __name__ == "__main__":
    sample_text = "意味が潰れた後にだけ、声が残る。"
    result = process_post(sample_text, "poemkun/output", "01", mode="simple")
    print(json.dumps(result, indent=2, ensure_ascii=False))
