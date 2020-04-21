<template>
  <div id="app">
    <!--
    <div id='nav'>
        <router-link to='/'>Home</router-link>|
        <router-link to="/About">About</router-link>
    </div>
    
	<router-view/>
    -->
	<!--
    <div id='nav'>
        <router-link to='/'>MainPage</router-link>|
		<router-link to='/search-block'>SearchBlock</router-link>
    </div>
    <router-view/>
	<p>Information in root Instance is: {{info}}. Do you see it?</p>
	-->
	<div id='myheader' >
				<a id='appname' href="index.html">物联网云管平台</a>
				<label id='userinfo'>User</label>
				<img id='header_user_icon' src="./assets/icons/user_icon.png"/>
			</div>

    <!--这是平台的工作区-->
			<div id='work-space'>
				<!--这是平台的左边菜单-->
				<ol id='main_menu' >
					<li class='menu_layer_1' v-on:click="clickAuthMng"><img src="./assets/icons/auth_manage_icon.png" /><label>权限管理</label> </li>
					<menu-item v-for="item in authMngItems" :key="item.tag" v-bind:item="item" v-bind:style="itemStyles[0]" v-on:click.native="displayedItem=item.tag"></menu-item>
					<li class='menu_layer_1' v-on:click="clickStationMng"><img src="./assets/icons/edge_station_icon.png" /><label>小站管理</label> </li>
					<menu-item v-for="item in stationMngItems" :key="item.tag" v-bind:item="item" v-bind:style="itemStyles[1]" v-on:click.native="displayedItem=item.tag"></menu-item>
					<li class='menu_layer_1' v-on:click="clickNetworkSvc"><img src="./assets/icons/net_service_icon.png" /><label>网络服务</label> </li>
                    <menu-item v-for="item in netServiceItems" :key="item.tag" v-bind:item="item" v-bind:style="itemStyles[2]" v-on:click.native="displayedItem=item.tag"></menu-item>
					<li class='menu_layer_1' v-on:click="clickSecurityDef"><img src="./assets/icons/security_protect_icon.png" /><label>安全防护</label> </li>
                    <menu-item v-for="item in securityDefItems" :key="item.tag" v-bind:item="item" v-bind:style="itemStyles[3]" v-on:click.native="displayedItem=item.tag"></menu-item>
					<li class='menu_layer_1' v-on:click="clickDataProc"><img src="./assets/icons/data_processing_icon.png" /><label>数据处理</label> </li>
                    <menu-item v-for="item in dataProcItems" :key="item.tag" v-bind:item="item" v-bind:style="itemStyles[4]" v-on:click.native="displayedItem=item.tag"></menu-item>
				</ol>
				
				
				<!--这是平台右边操作区-->
				
				<router-view/>
				
				
			</div>
  </div>
</template>

<script>
import menuitem from './components/menuitem.vue'

export default {
	components: {
		'menu-item': menuitem
	},
	
    //component data 
    data: function(){
      return {
				message: 'bad',
				title: 'hello, this is title',
				authMngItems: [
					{tag:'用户管理',imgRsc:require('./assets/icons/manu_layer_2_user.png'), url:'/authmng/usermng'},
					{tag:'角色管理',imgRsc:require('./assets/icons/manu_layer_2_role.png'), url:'/home'},
					{tag:'权限配置',imgRsc:require('./assets/icons/manu_layer_2_auth_config.png'), url:'/about'},
					],
					
				stationMngItems: [
					{tag:'小站管理',imgRsc:require('./assets/icons/manu_layer_2_user.png'), url:'/about'},
					{tag:'设备管理',imgRsc:require('./assets/icons/manu_layer_2_role.png'), url:'/about'},
				],
				
				netServiceItems: [
					{tag:'NetService',imgRsc:require('./assets/icons/manu_layer_2_user.png'), url:'/about'},
					{tag:'VNF',imgRsc:require('./assets/icons/manu_layer_2_role.png'), url:'/about'},
					{tag:'Template',imgRsc:require('./assets/icons/manu_layer_2_auth_config.png'), url:'/about'},
				],
				securityDefItems: [
					{tag:'服务日志',imgRsc:require('./assets/icons/manu_layer_2_user.png'), url:'/about'},
					{tag:'设备监控',imgRsc:require('./assets/icons/manu_layer_2_role.png'), url:'/about'},
				],
				dataProcItems: [
					{tag:'数据集',imgRsc:require('./assets/icons/manu_layer_2_user.png'), url:'/about'},
					{tag:'数据可视化',imgRsc:require('./assets/icons/manu_layer_2_role.png'), url:'/about'},
					{tag:'处理程序',imgRsc:require('./assets/icons/manu_layer_2_auth_config.png'), url:'/about'},
				],
				//二层菜单项列表的样式绑定，主要使用display属性控制二层菜单项
				//的显示与否
				itemStyles:[
					{"background-color": 'aquamarine',
					display: 'none',},
					{"background-color": 'aquamarine',
					display: 'none',},
					{"background-color": 'aquamarine',
					display: 'none',},
					{"background-color": 'aquamarine',
					display: 'none',},
					{"background-color": 'aquamarine',
					display: 'none',},
				],
				
				//记录当前显示的item内容
				displayedMenu: '',
				displayedItem: '',
				fields: ['姓名','性别','号码','邮箱'],
				rows: [[1,2,3,4],[3,4,5,6],[5,6,7,8]]
				}
    },
    //component methods
    methods:{
				//五个主菜单项的单击响应函数
				clickAuthMng: function(){
					this.displayedMenu = '权限管理'
					if(this.itemStyles[0].display=='none'){
						this.itemStyles[0].display='block'
						
					}
					else if(this.itemStyles[0].display=='block'){
						this.itemStyles[0].display='none'
					}
				},
				clickStationMng: function(){
					this.displayedMenu = '小站管理'
					if(this.itemStyles[1].display=='none'){
						this.itemStyles[1].display='block'
						
					}
					else if(this.itemStyles[1].display=='block'){
						this.itemStyles[1].display='none'
					}
				},
				clickNetworkSvc: function(){
					this.displayedMenu = '网络服务'
					if(this.itemStyles[2].display=='none'){
						this.itemStyles[2].display='block'
						
					}
					else if(this.itemStyles[2].display=='block'){
						this.itemStyles[2].display='none'
					}
				},
				clickSecurityDef: function(){
					this.displayedMenu = '安全防护'
					if(this.itemStyles[3].display=='none'){
						this.itemStyles[3].display='block'
						
					}
					else if(this.itemStyles[3].display=='block'){
						this.itemStyles[3].display='none'
					}
				},
				clickDataProc: function(){
					this.displayedMenu = '数据处理'
					if(this.itemStyles[4].display=='none'){
						this.itemStyles[4].display='block'
						
					}
					else if(this.itemStyles[4].display=='block'){
						this.itemStyles[4].display='none'
					}
				},
				
				//控制菜单二级item对应页面组件的显示与否
				onclick: function(){
					this.displayedItem = 'hello'
				},
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

/*界面顶栏属性*/
#myheader {
	background-color: aqua; 
	height: 60px;
}


/*顶栏中app名标签属性*/
#appname {
	color: white;
	font-size: 40px;
	float: left; 
	width: 300px;
	background-color:burlywood; 
	height: 60px;
	text-align:center;
	line-height:60px; 
	font-family: '仿宋','Times New Roman', Times, serif;
	
	text-decoration: none;
}

/*顶栏中用户图标属性*/
#header_user_icon {
	height: 60px;
	float: right;
}


/*顶栏中用户信息标签属性*/
#userinfo {
	float: right; 
	height: 60px;
	text-align: center;
	line-height: 60px;
	padding-right: 20px; 
	padding-left: 10px;
	font-family: georgia,仿宋;
	color: black;
}

#main_menu {
	
	width: 210px;
	position: absolute;
	top: 60px;
	/*bottom： 0px使得该元素底部与父元素底部相距为0，也可以填满剩余高度*/
	bottom: 0px;
	left: 0px;
	
	background-color: aqua;
	padding-left: 0px;
	margin: 0px;
}

/*操作区的样式*/
.op-space {
	position: absolute;
	top: 60px;
	left: 210px;
	bottom: 0px;
	right: 0px;
	background-color: antiquewhite;
}

/*第一层菜单项样式*/
.menu_layer_1 {
	/*float: left;*/
	height: 40px;
	width: 200px;
	font-size: 30px;
	font-family: 仿宋,georgia;
	margin-top: 1px;
	background-color: aqua;
	
	display: flex;
	/*边框的属性*/
	border-style: dashed;
	border-color:aquamarine;
	
}




/*第一层菜单项中图片样式*/
.menu_layer_1 img {
	width: 30px;
	float: left;
	align-self: center;
}

/*第一层菜单项中标签样式*/
.menu_layer_1 label{
	padding: 10px; 
	align-self: center;
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
