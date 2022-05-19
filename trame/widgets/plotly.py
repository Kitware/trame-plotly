from trame_plotly.widgets.plotly import *


def initialize(server):
    from trame_plotly import module

    server.enable_module(module)
