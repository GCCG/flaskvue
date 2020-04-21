<template>
    <li class="menu_layer_2"><img v-bind:src="item.imgRsc" /><router-link class="linker" v-bind:to="item.url">{{item.tag}}</router-link> </li>
</template>

<script>
export default {
    name: 'menuItem',
    props : ['item']
}
</script>

<style scope>
.menu_layer_2 {
	
	font-size: 20px;
	margin-top: 1px;
	margin-left: 40px;
	padding-left: 5px;
	width: 156px;
	/*float: left;*/
	display: flex;
	/*没有下面这一项，li里面的内容就会自动居中，这是vue的默认配置吗，好恶心 */
	text-align: left;
	
	/*边框属性*/
	border-style: ridge;
	border-color: navajowhite;
	border-width: 1px;
}

.menu_layer_2 img {
	align-self: center;
	margin: 0px;
	padding-left: 0px;
	width: 20px;
	/*background-color: blanchedalmond;*/
}

.menu_layer_2 .linker {
	font-family: 仿宋,georgia;
	align-self: center;
	padding-left: 8px;
	text-decoration: none;
	color: black;
}
</style>