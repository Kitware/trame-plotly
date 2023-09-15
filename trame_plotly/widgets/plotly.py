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
    """
    Create a Plotly figure element. For more details refer to the component
    `options documentation <https://plotly.com/javascript/configuration-options/>`_

    Properties:

    :param display_mode_bar:
    :param scroll_zoom:
    :param editable:
    :param static_plot:
    :param to_image_options:
    :param mode_bar_buttons_to_remove:
    :param mode_bar_buttons_to_add:
    :param locale:
    :param display_logo:
    :param responsive:
    :param double_click_delay:

    Events:

    :param after_export:
    :param after_plot:
    :param animated:
    :param animating_frame:
    :param animation_interrupted:
    :param auto_size:
    :param before_export:
    :param button_clicked:
    :param click:
    :param click_annotation:
    :param deselect:
    :param double_click:
    :param framework:
    :param hover:
    :param legend_click:
    :param legend_double_click:
    :param relayout:
    :param restyle:
    :param redraw:
    :param selected:
    :param selecting:
    :param slider_change:
    :param slider_end:
    :param slider_start:
    :param transitioning:
    :param transition_interrupted:
    :param unhover:
    """

    _next_id = 0

    def __init__(self, figure=None, state_variable_name=None, **kwargs):
        if state_variable_name is None:
            Figure._next_id += 1
            state_variable_name = f"trame__plotly_{Figure._next_id}"

        self.__figure_key = state_variable_name
        super().__init__(
            "trame-plotly",
            data=(f"{self.__figure_key}.data",),
            layout=(f"{self.__figure_key}.layout",),
            **kwargs,
        )
        if self.server:
            self.server.enable_module(module)

        self.__figure_data = figure
        self.server.state.setdefault(self.__figure_key, {"data": [], "layout": {}})
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
            ("after_export", "AfterExport"),
            ("after_plot", "AfterPlot"),
            ("animated", "Animated"),
            ("animating_frame", "AnimatingFrame"),
            ("animation_interrupted", "AnimationInterrupted"),
            ("auto_size", "AutoSize"),
            ("before_export", "BeforeExport"),
            ("button_clicked", "ButtonClicked"),
            ("click", "Click"),
            ("click_annotation", "ClickAnnotation"),
            ("deselect", "Deselect"),
            ("double_click", "DoubleClick"),
            ("framework", "Framework"),
            ("hover", "Hover"),
            ("legend_click", "LegendClick"),
            ("legend_double_click", "LegendDoubleClick"),
            ("relayout", "Relayout"),
            ("restyle", "Restyle"),
            ("redraw", "Redraw"),
            ("selected", "Selected"),
            ("selecting", "Selecting"),
            ("slider_change", "SliderChange"),
            ("slider_end", "SliderEnd"),
            ("slider_start", "SliderStart"),
            ("transitioning", "Transitioning"),
            ("transition_interrupted", "TransitionInterrupted"),
            ("unhover", "Unhover"),
        ]
        self.update()

    def update(self, plotly_fig=None, **kwargs):
        """
        Update the Plotly Figure with new content

        :param plotly_fig: Python plotly figure object
        """
        if plotly_fig:
            self.__figure_data = plotly_fig

        if self.__figure_data:
            self.server.state[self.__figure_key] = ENCODER(
                self.__figure_data.to_plotly_json()
            )

    @property
    def key(self):
        """Return the name of the state variable used internally"""
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
