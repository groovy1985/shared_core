# templates/__init__.py
# 各Botのテンプレートを集約し、共通インターフェースを提供

from .poemkun import render_poemkun
from .death import render_death
from .babaa import render_babaa
from .bukkoresyntax import render_bukkore

TEMPLATES = {
    "poemkun": render_poemkun,
    "death": render_death,
    "babaa": render_babaa,
    "bukkoresyntax": render_bukkore,
}


def render_template(bot_name: str, text: str) -> str:
    if bot_name not in TEMPLATES:
        raise ValueError(f"未登録のBot名: {bot_name}")
    return TEMPLATES[bot_name](text)
