<!--
 * @Author: your name
 * @Date: 2020-04-17 09:18:17
 * @LastEditTime: 2020-04-22 11:00:33
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /frontend/src/App.vue
 -->
<template>
  <div id="app">
	<router-view/>
	
  </div>
</template>

<script>

const AUTH_URL = "/auth"


export default {
	
	created: function(){
		this.$router.push(AUTH_URL)
	}
	
}
</script>


<style>
/* 主页的样式*/
html,body{
	font-family: 仿宋,georgia;
	background-color: sandybrown;
	height: 100%;
	margin: 0px;
	padding: 0px;
}
/* 表格的样式*/
td,th {
	font-family: 仿宋,georgia;
	background-color: honeydew;
	height: 100%;
	margin: 0px;
	padding: 0px;
}


#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}


</style>
