from slugify import slugify


def get_slug_from_title(title: str) -> str:
    return slugify(text=title)
