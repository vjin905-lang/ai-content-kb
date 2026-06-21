
def build_prompt(base, style, character, extra=""):
    parts = []

    if base:
        parts.append(base.strip())

    if style:
        parts.append(style.strip())

    if character:
        parts.append(character.strip())

    if extra:
        parts.append(extra.strip())

    return ", ".join(parts)
