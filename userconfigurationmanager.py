test_settings = {
    "Theme": "dark",
    "Notifications": "enabled",
    "Volume": "high"
    }
settings = ("language", "english")
def add_setting(test_settings, settings):
    key = settings[0].lower()
    value = settings[1].lower()
    if key in test_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        test_settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"
    pass

def update_setting(test_settings, settings):
    key = settings[0].lower()
    value = settings[1].lower()
    if key in test_settings:
        test_settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    pass


def delete_setting(test_settings, key):
    key = key.lower()
    if key in test_settings:
        del test_settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"
    pass

def view_settings(test_settings):
    if not test_settings:
        return "No settings available."
    result = "Current User Settings:\n"
    for key,value in test_settings.items():
        result += f"{key.capitalize()}: {value}\n"
    return result
    pass
