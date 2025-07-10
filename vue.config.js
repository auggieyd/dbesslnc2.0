const path = require("path");
const debug = process.env.NODE_ENV !== "production";

module.exports = {
  // Base URL (relative path)
  publicPath: "/v2/",
  // Output directory
  // outputDir: "dist",
  outputDir: process.env.outputDir,
  // Directory for static assets (js, css, img, fonts) relative to outputDir
  assetsDir: "assets",
  // indexPath: "index.html",
  // Whether to lint on save with eslint-loader
  lintOnSave: false,
  // use the full build with in-browser compiler?
  // https://vuejs.org/v2/guide/installation.html#Runtime-Compiler-vs-Runtime-only
  // compiler: false,

  // webpack configuration
  // see https://github.com/vuejs/vue-cli/blob/dev/docs/webpack.md   webpack链接API，用于生成和修改webapck配置
  chainWebpack: () => {
    if (debug) {
      // Development environment configuration
    } else {
      // Production environment configuration
    }
  },
  configureWebpack: config => {
    // webpack configuration, merged if object, overridden if function
    if (debug) {
      // Development environment settings
      config.devtool = "cheap-module-eval-source-map";
      config.mode = "development";
    } else {
      // Production environment settings
      config.mode = "production";
    }
    Object.assign(config, {
      // Shared configuration for development and production
      resolve: {
        alias: {
          "@": path.resolve(__dirname, "./src") // Set path alias
          //...
        }
      }
    });
  },
  // vue-loader configuration options
  // https://vue-loader.vuejs.org/en/options.html
  // vueLoader: {},

  // Whether to generate sourceMap files in production
  productionSourceMap: true,
  // CSS related configuration, takes precedence over css loader configuration in chainWebpack
  css: {
    // Whether to extract CSS using ExtractTextPlugin
    extract: true,
    // Enable CSS source maps? Disabling improves build speed
    sourceMap: false,
    // CSS preprocessor options
    loaderOptions: {
      less: {
        lessOptions: {
          javascriptEnabled: true,
        },
      },
    },
    requireModuleExtension: true
  },
  // use thread-loader for babel & TS in production build
  // enabled by default if the machine has more than one core
  parallel: require("os").cpus().length > 1,
  // whether to enable dll
  // See https://github.com/vuejs/vue-cli/blob/dev/docs/cli-service.md#dll-mode
  // dll: false,

  // PWA 插件相关配置
  // see https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-pwa
  pwa: {},
  // webpack-dev-server related configuration
  devServer: {
    open: process.platform === "darwin",
    host: "0.0.0.0",
    port: 3000,
    https: false,
    hotOnly: false,
    proxy: {
      "/api": {
        target: "http://localhost:8081", // specify the domain and port of the API server
        changeOrigin: true,
        pathRewrite: {
          "^/api": "/api"
        }
      }
    }, // configure proxy
    // eslint-disable-next-line no-unused-vars
    before: app => {}
  },
  // third-party plugin options
  pluginOptions: {
    // ...
  }
};
