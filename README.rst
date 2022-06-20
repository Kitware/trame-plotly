Plotly widget for trame
===========================================================================

.. image:: https://github.com/Kitware/trame-plotly/actions/workflows/test_and_release.yml/badge.svg
    :target: https://github.com/Kitware/trame-plotly/actions/workflows/test_and_release.yml
    :alt: Test and Release

trame-plotly extend trame **widgets** with components that can interface with Plotly to display their charts.

Plotly integration in trame allow you to create rich visualization by leveraging their `Python <https://plotly.com/python/>`_ or `JavaScript <https://plotly.com/javascript/>`_ interface.
The JavaScript version is exposed via `Vue.plotly <https://david-desmaisons.github.io/vue-plotly/>`_ within trame.widgets.plotly.Plotly class definition.

This package is not supposed to be used by itself but rather should come as a dependency of **trame**.
For any specificity, please refer to `the trame documentation <https://kitware.github.io/trame/>`_.


Installing
-----------------------------------------------------------

trame-plotly can be installed with `pip <https://pypi.org/project/trame-plotly/>`_:

.. code-block:: bash

    pip install --upgrade trame-plotly

Usage
-----------------------------------------------------------

The `Trame Tutorial <https://kitware.github.io/trame/docs/tutorial.html>`_ is the place to go to learn how to use the library and start building your own application.

The `API Reference <https://trame.readthedocs.io/en/latest/index.html>`_ documentation provides API-level documentation.

The Plotly component relies on the server for generating the chart definition. This can be achieved by hand or by simply using the Python version of Plotly.


How to use it?
```````````````````````````````````````````````````````````

Using the Python library

.. code-block:: python

    import plotly.graph_objects as go
    from trame.widgets import plotly

    fig = go.Figure(
        data=go.Contour(
            z=[
                [10, 10.625, 12.5, 15.625, 20],
                [5.625, 6.25, 8.125, 11.25, 15.625],
                [2.5, 3.125, 5.0, 8.125, 12.5],
                [0.625, 1.25, 3.125, 6.25, 10.625],
                [0, 0.625, 2.5, 5.625, 10],
            ]
        )
    )
    fig2 = go.Figure(
        data=go.Contour(
            z=[
                [5.625, 6.25, 8.125, 11.25, 15.625],
                [2.5, 3.125, 5.0, 8.125, 12.5],
                [10, 10.625, 12.5, 15.625, 20],
                [0.625, 1.25, 3.125, 6.25, 10.625],
                [0, 0.625, 2.5, 5.625, 10],
            ]
        )
    )

    widget = plotly.Figure(fig)
    widget.update(fig2)

But if you are feeling more adventurous you can use the component API directly by building the data yourself as well.

.. code-block:: python

    from trame.widgets import plotly

    # https://plotly.com/javascript/reference/
    plotly_data = [
      {
        "x": [1,2,3,4],
        "y": [10,15,13,17],
        "type": "scatter",
      }
    ]

    # https://plotly.com/javascript/reference/layout/
    plotly_layout = {
      "title": "My graph",
    }

    # https://plotly.com/javascript/configuration-options/
    plotly_options = {
      "scroll_zoom": True,
      "editable": True,
      "static_plot": True,
      "to_image_options": {
        "format": "svg", # one of png, svg, jpeg, webp
        "filename": "custom_image",
        "height": 500,
        "width": 700,
        "scale": 1 # Multiply title/legend/axis/canvas sizes by this factor
      },
      "display_mode_bar": True,
      "mode_bar_buttons_to_remove": [
        "zoom2d", "pan2d", "select2d", "lasso2d", "zoomIn2d", "zoomOut2d", "autoScale2d", "resetScale2d", # 2D
        "zoom3d", "pan3d", "orbitRotation", "tableRotation", "handleDrag3d", "resetCameraDefault3d", "resetCameraLastSave3d", "hoverClosest3d", # 3D
        "hoverClosestCartesian", "hoverCompareCartesian", # Cartesian
        "zoomInGeo", "zoomOutGeo", "resetGeo", "hoverClosestGeo", # Geo
        "hoverClosestGl2d", "hoverClosestPie", "toggleHover", "resetViews", "toImage", "sendDataToCloud", "toggleSpikelines", "resetViewMapbox", # Other
      ],
      "mode_bar_buttons_to_add": [
        {
          "name": 'color toggler',
          "icon": icon1, # https://plotly.com/javascript/configuration-options/#add-buttons-to-modebar
          "click": "...",
        },
      ],
      "locale": "fr",
      "display_logo": False,
      "responsive": True,
      "double_click_delay": 1000,
    }

    # Hand made chart
    chart = plotly.Figure(
      data=("chart_data", plotly_data),
      layout=("chart_layout", plotly_layout),
      **plotly_options,
    )


.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Type
     - Values
   * - properties
     - data, layout, display_mode_bar, scroll_zoom, editable, static_plot, to_image_options, mode_bar_buttons_to_remove, mode_bar_buttons_to_add, locale, display_logo, responsive, double_click_delay
   * - events
     - after_export, after_plot, animated, animating_frame, animation_interrupted, auto_size, before_export, button_clicked, click, click_annotation, deselect, double_click, framework, hover, legend_click, legend_double_click, relayout, restyle, redraw, selected, selecting, slider_change, slider_end, slider_start, transitioning, transition_interrupted, unhover


License
-----------------------------------------------------------

trame-plotly is made available under the MIT License. For more details, see `LICENSE <https://github.com/Kitware/trame-plotly/blob/master/LICENSE>`_
This license has been chosen to match the one use by `Plotly <https://github.com/plotly/plotly.py/blob/master/LICENSE.txt>`_ and `vue-plotly <https://github.com/David-Desmaisons/vue-plotly/blob/master/LICENSE>`_ which are instrumental for making that library possible.


Community
-----------------------------------------------------------

`Trame <https://kitware.github.io/trame/>`_ | `Discussions <https://github.com/Kitware/trame/discussions>`_ | `Issues <https://github.com/Kitware/trame/issues>`_ | `RoadMap <https://github.com/Kitware/trame/projects/1>`_ | `Contact Us <https://www.kitware.com/contact-us/>`_

.. image:: https://zenodo.org/badge/410108340.svg
    :target: https://zenodo.org/badge/latestdoi/410108340


Enjoying trame?
-----------------------------------------------------------

Share your experience `with a testimonial <https://github.com/Kitware/trame/issues/18>`_ or `with a brand approval <https://github.com/Kitware/trame/issues/19>`_.
