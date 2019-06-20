# -*- coding: utf-8 -*-
"""Create an application instance, and this is the main entry for whole application."""

from flask.helpers import get_debug_flag

from jianshu.app import create_app
from jianshu.settings import DevConfig, ProdConfig

ENV_CONF = DevConfig if get_debug_flag() else ProdConfig

app = create_app(ENV_CONF)
