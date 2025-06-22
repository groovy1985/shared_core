# shared_core/file_writer.py

import os
import json
from datetime import datetime

def save_raw_post(bot_name, text):
    """
    構文死体（未評価ポスト）を Syntaxtemple/raw_post/{bot}/ に保存
    """
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    dir_path = f"Syntaxtemple/raw_post/{bot_name}"
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, f"{now}.txt")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text.strip())

    print(f"✅ raw_post 保存完了: {file_path}")
    return file_path


def save_evaluated(bot_name, text, eval_result, classification, file_id=None):
    """
    評価済構文とメタ情報を Syntaxtemple/evaluated/{bot}/ に保存
    """
    now = datetime.now().strftime("%Y%m%d_%H%M%S") if file_id is None else file_id
    base_dir = f"Syntaxtemple/evaluated/{bot_name}"
    os.makedirs(base_dir, exist_ok=True)

    # 本文保存
    text_path = os.path.join(base_dir, f"{now}.txt")
    meta_path = os.path.join(base_dir, f"{now}_meta.json")

    # ヘッダ付き本文保存
    header = [
        "---",
        f"KZ: {eval_result.get('KZ')}",
        f"HX: {eval_result.get('HX')}",
        f"Fランク: {classification.get('rank')}",
        f"MOD: {eval_result['KZ_scores'].get('MOD')} / "
        f"DCC: {eval_result['KZ_scores'].get('DCC')} / "
        f"STR: {eval_result['KZ_scores'].get('STR')} / "
        f"PHN: {eval_result['KZ_scores'].get('PHN')} / "
        f"DYN: {eval_result['KZ_scores'].get('DYN')}",
        f"SIL: {eval_result['HX_scores'].get('SIL')} / "
        f"ETH: {eval_result['HX_scores'].get('ETH')} / "
        f"RTN: {eval_result['HX_scores'].get('RTN')} / "
        f"PRX: {eval_result['HX_scores'].get('PRX')}",
        "---", ""
    ]

    with open(text_path, "w", encoding="utf-8") as f:
        f.write("\n".join(header))
        f.write(text.strip())

    # メタ情報保存
    meta = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "rank": classification["rank"],
        "KZ": eval_result.get("KZ"),
        "HX": eval_result.get("HX"),
        "KZ_scores": eval_result.get("KZ_scores"),
        "HX_scores": eval_result.get("HX_scores"),
        "PRX": classification.get("PRX"),
        "SC_candidate": classification.get("SC_candidate")
    }

    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)

    print(f"✅ evaluated 保存完了: {text_path}")
    return text_path
