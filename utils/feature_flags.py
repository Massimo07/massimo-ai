FEATURE_FLAGS = {
    "enable_new_dashboard": False,
    "beta_voice_ai": True,
    "live_radio": True,
}

def is_feature_enabled(feature: str) -> bool:
    return FEATURE_FLAGS.get(feature, False)
