from config_loader import settings_loader

settings = settings_loader()

print("Sistema:", settings["system_name"])
print("Logo:", settings["logo"])
print("Banco de dados:", settings["db_path"])
print("Tema carregado:")
print("Cor primária:", settings["theme"].get("primary_color"))
print("Cor secundária:", settings["theme"].get("secondary_color"))
print("Cor do texto:", settings["theme"].get("text_color"))
print("Fonte:", settings["theme"].get("font"))