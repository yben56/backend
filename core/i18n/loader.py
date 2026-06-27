import json

_cache = {}


def load_file(lang: str):
    if lang in _cache:
        return _cache[lang]

    try:
        with open(f"i18n/{lang}.json", "r", encoding="utf-8") as f:
            _cache[lang] = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        _cache[lang] = {}

    return _cache[lang]