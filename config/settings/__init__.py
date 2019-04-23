import os

import environ

from split_settings.tools import include, optional

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
base = environ.Path(__file__) - 3
BASE_DIR = base()

env = environ.Env()
if os.path.exists(base(".env")):
    environ.Env.read_env(base(".env"))

if os.getenv("DJANGO_SETTINGS_MODULE") == "config.settings":
    platform = env.str("PLATFORM", default="local")

    include(
        "base.py", optional(os.path.join("platform", f"{platform}.py")), scope=globals()
    )
