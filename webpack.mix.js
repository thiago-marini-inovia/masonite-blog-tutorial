/* Mix provides a clean, fluent API for defining some Webpack build steps for your Masonite
applications. By default, we are compiling the CSS file for the application as well as
bundling up all the JS files. */
const mix = require('laravel-mix')
const path = require('path')


mix.js('resources/js/app.js', 'js')
  .vue({ version: 3 })
  .postCss('resources/css/app.css', 'css', [
    //
  ])

// ensure root directory of mix is project root
mix.setPublicPath("storage/compiled")

// Enable HMR for development
mix.webpackConfig({
  devServer: {
    host: '0.0.0.0',
    port: 8080,
    allowedHosts: 'all',
    hot: true,
    compress: true,
    headers: {
      'Access-Control-Allow-Origin': '*'
    },
    client: {
      webSocketURL: {
        hostname: 'localhost',
        pathname: '/ws',
        port: 8080,
        protocol: 'ws'
      }
    }
  }
}).options({
  hmrOptions: {
    host: '0.0.0.0',
    port: 8080
  }
})

// add an alias to js code
mix.alias({
  "@": path.resolve("resources/js/"),
})

// add version hash in production
if (mix.inProduction()) {
  mix.version()
}
// Disable compilation success notification
mix.disableSuccessNotifications()
