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
