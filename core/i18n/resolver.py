def resolve_language(request) -> str:
    raw = request.headers.get("Accept-Language", "en")

    langs = [l.split(";")[0].strip() for l in raw.split(",")]

    return langs[0] if langs else "en"