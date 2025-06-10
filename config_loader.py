import json
import os


def settings_loader(path="settings.json"):
    with open(path, "r", encoding="utf-8") as f:
        settings = json.load(f)

    theme_path = settings.get("theme")
    if theme_path and os.path.exists(theme_path):
        with open(theme_path, "r", encoding="utf-8") as tf:
            theme = json.load(tf)
        settings["theme"] = theme
    else:
        settings["theme"] = {}

    return settings