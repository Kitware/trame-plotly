from trame_plotly.widgets.plotly import *  # noqa: F403


def initialize(server):
    from trame_plotly import module  # noqa: PLC0415

    server.enable_module(module)
