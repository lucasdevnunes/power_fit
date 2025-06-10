import json
import os


def settings_loader(path="settings.json"):
    with open(path, "r", encoding="utf-8") as f:
        settings = json.load(f)

    theme_path = settings.get("tema")
    if tema_path and os.path.exists(tema_path):
        with open(theme_path, "r", encoding="utf-8") as tf:
            theme = json.load(tf)
        settings["theme"] = theme
    else:
        settings["theme"] = {}

    return settings