import {
  ref,
  computed,
  watch,
  onMounted,
  onBeforeUnmount,
  nextTick,
} from "vue";
import Plotly from "plotly.js-dist-min";

// ----------------------------------------------------------------------------
// Utils
// ----------------------------------------------------------------------------

function cached(fn) {
  const cache = Object.create(null);
  return function cachedFn(str) {
    const hit = cache[str];
    return hit || (cache[str] = fn(str));
  };
}

const regex = /-(\w)/g;
const camelize = cached((str) =>
  str.replace(regex, (_, c) => (c ? c.toUpperCase() : ""))
);

// ----------------------------------------------------------------------------
// Events
// ----------------------------------------------------------------------------
const eventsName = [
  "AfterExport",
  "AfterPlot",
  "Animated",
  "AnimatingFrame",
  "AnimationInterrupted",
  "AutoSize",
  "BeforeExport",
  "ButtonClicked",
  "Click",
  "ClickAnnotation",
  "Deselect",
  "DoubleClick",
  "Framework",
  "Hover",
  "LegendClick",
  "LegendDoubleClick",
  "Relayout",
  "Restyle",
  "Redraw",
  "Selected",
  "Selecting",
  "SliderChange",
  "SliderEnd",
  "SliderStart",
  "Transitioning",
  "TransitionInterrupted",
  "Unhover",
];
// ----------------------------------------------------------------------------
// Methods
// ----------------------------------------------------------------------------
const plotlyFunctions = [
  "restyle",
  "relayout",
  "update",
  "addTraces",
  "deleteTraces",
  "moveTraces",
  "extendTraces",
  "prependTraces",
  "purge",
];

// ----------------------------------------------------------------------------

export default {
  props: {
    data: {
      type: Array,
    },
    layout: {
      type: Object,
    },
  },
  emits: eventsName,
  setup(props, { emit, expose, attrs }) {
    const elem = ref(null);
    const scheduled = ref(null);
    const innerLayout = ref({ ...props.layout });
    const options = computed(() => {
      const optionsFromAttrs = Object.keys(attrs).reduce((acc, key) => {
        acc[camelize(key)] = attrs[key];
        return acc;
      }, {});
      return {
        responsive: false,
        ...optionsFromAttrs,
      };
    });

    // Methods

    function onResize() {
      Plotly.Plots.resize(elem.value);
    }
    const sizeObserver = new ResizeObserver(onResize);

    function react() {
      Plotly.react(elem.value, props.data, innerLayout.value, options.value);
    }

    async function schedule(replot) {
      if (scheduled.value) {
        scheduled.value = { replot: scheduled.value.replot || replot };
        return;
      }
      scheduled.value = { replot };
      await nextTick();
      const shouldReact = scheduled.value?.replot;
      scheduled.value = null;
      if (shouldReact) {
        react();
        return;
      }
      methods.relayout(innerLayout.value);
    }

    function toImage(options) {
      const allOptions = Object.assign(getPrintOptions(), options.value);
      return Plotly.toImage(elem.value, allOptions);
    }

    function downloadImage(options) {
      const filename = `plot-${new Date().toISOString()}`;
      const allOptions = Object.assign(
        getPrintOptions(),
        { filename },
        options.value
      );
      return Plotly.downloadImage(elem.value, allOptions);
    }

    function getPrintOptions() {
      return {
        format: "png",
        width: elem.value.clientWidth,
        height: elem.value.clientHeight,
      };
    }

    const methods = {
      onResize,
      react,
      schedule,
      toImage,
      downloadImage,
      getPrintOptions,
    };
    for (let i = 0; i < plotlyFunctions.length; i++) {
      const method = plotlyFunctions[i];
      methods[method] = (...args) => {
        return Plotly(elem.value, ...args);
      };
    }

    // Watch
    watch(
      () => props.data,
      async () => {
        await schedule(true);
      }
    );

    watch(options, async (newValue, oldValue) => {
      if (JSON.stringify(newValue) === JSON.stringify(oldValue)) {
        return;
      }
      await schedule(true);
    });
    watch(
      () => props.layout,
      async (layout) => {
        innerLayout.value = { ...layout };
        await schedule(false);
      }
    );

    // --------------

    onMounted(() => {
      if (!elem.value) {
        return;
      }
      Plotly.newPlot(elem.value, props.data, innerLayout.value, options.value);
      eventsName.forEach((name) => {
        const completeName = `plotly_${name.toLowerCase()}`;
        const handler = (...args) => emit(name, ...args);
        elem.value.on(completeName, handler);
      });
      sizeObserver.observe(elem.value);
    });

    onBeforeUnmount(() => {
      sizeObserver.unobserve(elem.value);
      eventsName.forEach((name) => {
        const completeName = `plotly_${name.toLowerCase()}`;
        elem.value.removeAllListeners(completeName);
      });
      Plotly.purge(elem.value);
    });

    expose(methods);

    return { elem, ...methods };
  },
  template: `<div style="position: relative; width: 100%; height: 100%;" v-bind="$attrs">
              <div ref="elem" style="position: absolute; width: 100%; height: 100%;"></div>
            </div>`,
};
