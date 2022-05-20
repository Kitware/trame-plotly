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
