from core.i18n.loader import load_file
from pathlib import Path

I18N_DIR = Path(__file__).resolve().parent.parent.parent / "i18n"


def get_available_languages():
    return {f.stem for f in I18N_DIR.glob("*.json")}


def normalize_lang(lang: str, available: set) -> str:
    lang = lang.replace("-", "_")
    return lang if lang in available else "en"


def t(code: str, lang: str) -> str:
    available = get_available_languages()

    lang = normalize_lang(lang, available)

    translations = load_file(lang)
    fallback = load_file("en")

    return translations.get(code) or fallback.get(code) or code