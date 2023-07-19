export default {
  base: "./",
  build: {
    sourcemap: true,
    lib: {
      entry: "./src/main.js",
      name: "trame_plotly",
      formats: ["umd"],
      fileName: "trame-plotly",
    },
    rollupOptions: {
      external: ["vue"],
      output: {
        globals: {
          vue: "Vue",
        },
      },
    },
    outDir: "../trame_plotly/module/serve",
    assetsDir: ".",
  },
};
