# templates.py
# Bot別の投稿テンプレートを定義（ver.1.0）

from datetime import datetime

# Botごとのテンプレート（ver.1.0）
TEMPLATES = {
    "poemkun": lambda text: f"詩的構文報告 ({datetime.now().strftime('%Y/%m/%d')}):\n{text}\n#構文国家",

    "death": lambda text: f"This language is no longer reversible.\n{text}\n#SyntaxCollapse",

    "babaa": lambda text: f"「{text.split('。')[0]}」って言ったら、\n「あらそう」と返されたのよ。\n#ババァ構文",

    "bukkoresyntax": lambda text: f"【観測報告】構文異常を確認。\n{text}\nKZHX検体として保存済。",
}


def render_template(bot_name: str, text: str) -> str:
    """
    Bot名と本文からテンプレートを適用して投稿文を生成
    """
    if bot_name not in TEMPLATES:
        raise ValueError(f"未登録のBot名: {bot_name}")
    return TEMPLATES[bot_name](text)


if __name__ == "__main__":
    sample = "沈黙が吊られていた。旋回のなかに紙の構文があった。"
    for bot in TEMPLATES.keys():
        print(f"\n[{bot.upper()}] 投稿テンプレート:")
        print(render_template(bot, sample))
