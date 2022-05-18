from trame_client.widgets.core import AbstractElement
from trame_plotly import module

try:
    from trame_client.encoders.numpy import encode

    has_numpy = True
except ImportError:
    has_numpy = False


def no_encoding(_data):
    return _data


ENCODER = encode if has_numpy else no_encoding


class Figure(AbstractElement):
    _next_id = 0
    """
    Create a Plotly figure element
    """

    def __init__(self, figure=None, **kwargs):
        Figure._next_id += 1
        self.__figure_key = f"trame__plotly_{Figure._next_id}"
        super().__init__(
            "vue-plotly",
            data=(f"{self.__figure_key}.data",),
            layout=(f"{self.__figure_key}.layout",),
            **kwargs,
        )
        if self.server:
            self.server.enable_module(module)

        self.__figure_data = figure
        self.server.state[self.__figure_key] = {"data": [], "layout": {}}
        self._attr_names += [
            "data",
            "layout",
            ("display_mode_bar", "displayModeBar"),
            ("scroll_zoom", "scrollZoom"),
            "editable",
            ("static_plot", "staticPlot"),
            ("to_image_options", "toImageButtonOptions"),
            ("mode_bar_buttons_to_remove", "modeBarButtonsToRemove"),
            ("mode_bar_buttons_to_add", "modeBarButtonsToAdd"),
            "locale",
            ("display_logo", "displaylogo"),
            "responsive",
            ("double_click_delay", "doubleClickDelay"),
        ]
        self._event_names += [
            ("after_export", "afterexport"),
            ("after_plot", "afterplot"),
            ("animated", "animated"),
            ("animating_frame", "animatingframe"),
            ("animation_interrupted", "animationinterrupted"),
            ("auto_size", "autosize"),
            ("before_export", "beforeexport"),
            ("button_clicked", "buttonclicked"),
            ("click", "click"),
            ("click_annotation", "clickannotation"),
            ("deselect", "deselect"),
            ("double_click", "doubleclick"),
            ("framework", "framework"),
            ("hover", "hover"),
            ("legend_click", "legendclick"),
            ("legend_double_click", "legenddoubleclick"),
            ("relayout", "relayout"),
            ("restyle", "restyle"),
            ("redraw", "redraw"),
            ("selected", "selected"),
            ("selecting", "selecting"),
            ("slider_change", "sliderchange"),
            ("slider_end", "sliderend"),
            ("slider_start", "sliderstart"),
            ("transitioning", "transitioning"),
            ("transition_interrupted", "transitioninterrupted"),
            ("unhover", "unhover"),
        ]
        self.update()

    def update(self, plotly_fig=None, **kwargs):
        if plotly_fig:
            self.__figure_data = plotly_fig

        if self.__figure_data:
            self.server.state[self.__figure_key] = ENCODER(
                self.__figure_data.to_plotly_json()
            )

    @property
    def key(self):
        return self.__figure_key

    @staticmethod
    def to_data(chart, **kwargs):
        """
        Serialize plotly figure
        """
        return ENCODER(chart.to_plotly_json())


__all__ = [
    "Figure",
]
