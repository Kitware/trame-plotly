# trame-plotly

This directory capture the vue-plotly component and bundle it as a Vue plugin so it can be use within trame.

## Setup

```bash
npm install
npm run build
```

### Lints and fixes files

```bash
npm run lint
```

### Future version

If the following PR get merged, trame will be able to directly use the published version by running the following command and updating `vue_use = ["vue-plotly"]` depending of the name update.

```
curl https://unpkg.com/vue-plotly/dist/vue-plotly.umd.min.js -Lo ./trame_plotly/module/serve/trame-plotly.js
```