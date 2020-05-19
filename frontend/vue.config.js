/*
 * @Author: your name
 * @Date: 2020-04-18 21:18:59
 * @LastEditTime: 2020-05-18 11:20:50
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /frontend/vue.config.js
 */ 
module.exports = {
    configureWebpack: {
      devtool: 'eval-source-map',
    },
    //outputDir: '../dist',
    //assetsDir: '../dist/static'
    // devServer: {
    //   open: true, //是否自动弹出浏览器页面
    //   host: "localhost", 
    //   port: '8081', 
    //   https: false,   //是否使用https协议
    //   hotOnly: false, //是否开启热更新
    //   proxy: {
    //     '/api': {
    //         target: 'http://localhost:5000', //API服务器的地址
    //         changeOrigin: true,
    //         pathRewrite: {
    //             '^/api': ''
    //             }
    //         }
    //   },
    // }
}