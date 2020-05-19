<template>
  <div>
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
	<!--这是平台的顶栏-->
	<div id='myheader' >
				<a id='appname' href="index.html">物联网云管平台</a>
				<label id='userinfo'>User</label>
				<img id='header_user_icon' src="../assets/icons/user_icon.png"/>
			</div>

    <!--这是平台的工作区-->
			<div id='work-space'>
				<!--这是平台的左边菜单-->
				<ol id='main_menu' >
					<li class='menu_layer_1' v-bind:style="menuStyles[0]" v-on:click="clickAuthMng"><img src="../assets/icons/auth_manage_icon.png" /><label>权限管理</label> </li>
					<menu-item ref="menuItem" v-for="item in authMngItems" :key="item.tag" v-bind:item="item" v-bind:style="itemStyles[0]" v-on:click.native="onClickMenuItem(item.tag)"></menu-item>
					<li class='menu_layer_1' v-bind:style="menuStyles[1]" v-on:click="clickStationMng"><img src="../assets/icons/edge_station_icon.png" /><label>小站管理</label> </li>
					<menu-item ref="menuItem" v-for="item in stationMngItems" :key="item.tag" v-bind:item="item" v-bind:style="itemStyles[1]" v-on:click.native="onClickMenuItem(item.tag)"></menu-item>
					<li class='menu_layer_1' v-bind:style="menuStyles[2]" v-on:click="clickNetworkSvc"><img src="../assets/icons/net_service_icon.png" /><label>网络服务</label> </li>
                    <menu-item ref="menuItem" v-for="item in netServiceItems" :key="item.tag" v-bind:item="item" v-bind:style="itemStyles[2]" v-on:click.native="onClickMenuItem(item.tag)"></menu-item>
					<li class='menu_layer_1' v-bind:style="menuStyles[3]" v-on:click="clickSecurityDef"><img src="../assets/icons/security_protect_icon.png" /><label>安全防护</label> </li>
                    <menu-item ref="menuItem" v-for="item in securityDefItems" :key="item.tag" v-bind:item="item" v-bind:style="itemStyles[3]" v-on:click.native="onClickMenuItem(item.tag)"></menu-item>
					<li class='menu_layer_1' v-bind:style="menuStyles[4]" v-on:click="clickDataProc"><img src="../assets/icons/data_processing_icon.png" /><label>数据处理</label> </li>
                    <menu-item ref="menuItem" v-for="item in dataProcItems" :key="item.tag" v-bind:item="item" v-bind:style="itemStyles[4]" v-on:click.native="onClickMenuItem(item.tag)"></menu-item>
				</ol>
				
				
				<!--这是平台右边操作区-->
				
				<router-view/>
				
				
			</div>
  </div>
</template>

<script>
import menuitem from '../components/menuitem.vue'
const NORMAL_ITEM_STYLE = {backgroundColor: '#99CCFF'}
const SELECTED_ITEM_STYLE = {backgroundColor: '#FFFFCC'}
const NORMAL_MENU_COLOR = '#CCFFCC'
const SELECTED_MENU_COLOR = '#FFFFCC'

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
					{tag:'用户管理',imgRsc:require('../assets/icons/manu_layer_2_user.png'), url:'/main-page/user-mng', style: NORMAL_ITEM_STYLE},
					{tag:'角色管理',imgRsc:require('../assets/icons/manu_layer_2_role.png'), url:'/main-page/blank', style: NORMAL_ITEM_STYLE},
					{tag:'权限配置',imgRsc:require('../assets/icons/manu_layer_2_auth_config.png'), url:'/main-page/blank', style: NORMAL_ITEM_STYLE},
					],
					
				stationMngItems: [
					{tag:'小站管理',imgRsc:require('../assets/icons/manu_layer_2_user.png'), url:'/main-page/blank', style: NORMAL_ITEM_STYLE},
					{tag:'设备管理',imgRsc:require('../assets/icons/manu_layer_2_role.png'), url:'/main-page/blank', style: NORMAL_ITEM_STYLE},
				],
				
				netServiceItems: [
					{tag:'NetService',imgRsc:require('../assets/icons/manu_layer_2_user.png'), url:'/main-page/blank', style: NORMAL_ITEM_STYLE},
					{tag:'VNF',imgRsc:require('../assets/icons/manu_layer_2_role.png'), url:'/main-page/blank', style: NORMAL_ITEM_STYLE},
					{tag:'Template',imgRsc:require('../assets/icons/manu_layer_2_auth_config.png'), url:'/main-page/blank', style: NORMAL_ITEM_STYLE},
				],
				securityDefItems: [
					{tag:'服务日志',imgRsc:require('../assets/icons/manu_layer_2_user.png'), url:'/main-page/blank', style: NORMAL_ITEM_STYLE},
					{tag:'设备监控',imgRsc:require('../assets/icons/manu_layer_2_role.png'), url:'/main-page/blank', style: NORMAL_ITEM_STYLE},
				],
				dataProcItems: [
					{tag:'数据集',imgRsc:require('../assets/icons/manu_layer_2_user.png'), url:'/main-page/blank', style: NORMAL_ITEM_STYLE},
					{tag:'数据可视化',imgRsc:require('../assets/icons/manu_layer_2_role.png'), url:'/main-page/blank', style: NORMAL_ITEM_STYLE},
					{tag:'处理程序',imgRsc:require('../assets/icons/manu_layer_2_auth_config.png'), url:'/main-page/blank', style: NORMAL_ITEM_STYLE},
				],
				//二层菜单项列表的样式绑定，主要使用display属性控制二层菜单项
				//的显示与否
				itemStyles:[
					{display: 'none',},
					{display: 'none',},
					{display: 'none',},
					{display: 'none',},
					{display: 'none',},
				],

				//一层菜单的样式绑定，主要使用backgroundColor属性控制一层菜单的颜色
				menuStyles:[
					{backgroundColor: NORMAL_MENU_COLOR,},
					{backgroundColor: NORMAL_MENU_COLOR,},
					{backgroundColor: NORMAL_MENU_COLOR,},
					{backgroundColor: NORMAL_MENU_COLOR,},
					{backgroundColor: NORMAL_MENU_COLOR,},
				],
				
				//记录当前显示的item内容
				displayedMenu: '',
				displayedItem: '',
				fields: ['姓名','性别','号码','邮箱'],
				rows: [[1,2,3,4],[3,4,5,6],[5,6,7,8]],
				selectedMenuItem: '',
				selectedMenu: -1,
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
				changeMenuItemStyle: function(oldtag, newtag){
					var index = 0
					//权限管理菜单中检查
					var currentSelectedMenu = -1
					for(index=0; index<this.authMngItems.length; index++){
						//console.log("this.authMngItems[0].style is: ",this.authMngItems[0].style)
						if(this.authMngItems[index].tag == oldtag){
							this.authMngItems[index].style = NORMAL_ITEM_STYLE
							
						}
						if(this.authMngItems[index].tag == newtag){
							this.authMngItems[index].style = SELECTED_ITEM_STYLE
							currentSelectedMenu = 0
						}
					}
					//小站菜单中检查
					for(index=0; index<this.stationMngItems.length; index++){
						//console.log("this.stationMngItems[0].style is: ",this.stationMngItems[0].style)
						if(this.stationMngItems[index].tag == oldtag){
							this.stationMngItems[index].style = NORMAL_ITEM_STYLE
							
						}
						if(this.stationMngItems[index].tag == newtag){
							this.stationMngItems[index].style = SELECTED_ITEM_STYLE
							currentSelectedMenu = 1
						}
					}
					//网络服务菜单中检查
					for(index=0; index<this.netServiceItems.length; index++){
						//console.log("this.netServiceItems[0].style is: ",this.netServiceItems[0].style)
						if(this.netServiceItems[index].tag == oldtag){
							this.netServiceItems[index].style = NORMAL_ITEM_STYLE
							
						}
						if(this.netServiceItems[index].tag == newtag){
							this.netServiceItems[index].style = SELECTED_ITEM_STYLE
							currentSelectedMenu = 2
						}
					}
					//安全服务菜单中检查
					for(index=0; index<this.securityDefItems.length; index++){
						//console.log("this.securityDefItems[0].style is: ",this.securityDefItems[0].style)
						if(this.securityDefItems[index].tag == oldtag){
							this.securityDefItems[index].style = NORMAL_ITEM_STYLE
							
						}
						if(this.securityDefItems[index].tag == newtag){
							this.securityDefItems[index].style = SELECTED_ITEM_STYLE
							currentSelectedMenu = 3
						}
					}
					//数据处理菜单中检查
					for(index=0; index<this.dataProcItems.length; index++){
						//console.log("this.dataProcItems[0].style is: ",this.dataProcItems[0].style)
						if(this.dataProcItems[index].tag == oldtag){
							this.dataProcItems[index].style = NORMAL_ITEM_STYLE
							
						}
						if(this.dataProcItems[index].tag == newtag){
							this.dataProcItems[index].style = SELECTED_ITEM_STYLE
							currentSelectedMenu = 4
						}
					}
					//更新菜单背景颜色
					console.log('current selected menu is: '+currentSelectedMenu)
					for(index=0; index<this.menuStyles.length; index++){
						
						if(currentSelectedMenu == index){
							if(this.selectedMenu == -1){
								this.menuStyles[index].backgroundColor = SELECTED_MENU_COLOR
								this.selectedMenu = currentSelectedMenu
								console.log('selected menu '+index)
								console.log('this.menuStyles[index] is '+this.menuStyles[index])
							}
							else if(this.selectedMenu != currentSelectedMenu){
								this.menuStyles[index].backgroundColor = SELECTED_MENU_COLOR
								this.menuStyles[this.selectedMenu].backgroundColor = NORMAL_MENU_COLOR
								this.selectedMenu = currentSelectedMenu
								console.log('selected menu '+index)
							}
							
						}
					}
				},
				onClickMenuItem: function(tag){
					//console.log("this.selectedMenuItem is: "+this.selectedMenuItem )
					//console.log('selected item is: '+tag)
					this.changeMenuItemStyle(this.selectedMenuItem, tag)
					this.selectedMenuItem = tag
				},
			}
}
</script>


<style>
/* 主页的样式*/
html,body{
	font-family: 仿宋,georgia;
	/*background-color: sandybrown;*/
	background-color: #FFFFCC;
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
	/*background-color: aqua; */
	background-color: #CCFFCC;
	height: 60px;
}


/*顶栏中app名标签属性*/
#appname {
	color: white;
	font-size: 40px;
	float: left; 
	width: 300px;
	/*background-color:burlywood;*/
	background-color: #3399CC; 
	height: 60px;
	text-align:center;
	line-height:60px; 
	font-family: '仿宋','Times New Roman', Times, serif;
	
	text-decoration: none;

	border-top-right-radius: 15px;
	border-bottom-right-radius: 15px;
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
	
	/*background-color: aqua;*/
	background-color: #CCFFCC;
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
	/*background-color: antiquewhite;*/
	background-color: #CCFFFF;
}

/*第一层菜单项样式*/
.menu_layer_1 {
	/*float: left;*/
	height: 40px;
	width: 200px;
	font-size: 30px;
	font-family: 仿宋,georgia;
	margin-top: 1px;
	/*background-color: aqua;*/
	background-color: #CCFFCC;
	
	display: flex;
	/*边框的属性*/
	border-style: outset;
	/*border-color:aquamarine;*/
	border-color: #FFFFFF;
	border-radius: 10px;
	
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
