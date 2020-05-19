/*
 * @Author: your name
 * @Date: 2020-04-17 09:18:17
 * @LastEditTime: 2020-05-18 10:45:36
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /frontend/src/main.js
 */ 
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import searchblock from './components/searchblock.vue'




Vue.config.productionTip = false

new Vue({

  router,
  render: h => h(App),
  components: {
    'search-block':searchblock,
  },
}).$mount('#app')
