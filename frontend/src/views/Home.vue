<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <bigtag></bigtag>
    <menu-item v-bind:item="item"></menu-item>
    
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import bigtag from '@/components/bigtag.vue'
import menuItem from '@/components/menuitem.vue'
//import url from '../assets/icons/manu_layer_2_user.png'

export default {
  data: function(){
    return {item:{imgRsc:require('../assets/icons/manu_layer_2_user.png'),tag:'用户管理'}}
  },
  name: 'Home',
  components: {
    HelloWorld,
    bigtag,
    'menu-item': menuItem
  }
}
</script>
