<template>
    <li class="menu_layer_2"><img v-bind:src="item.imgRsc" /><label>{{item.tag}}</label> </li>
</template>

<script>
export default {
    name: 'menuItem',
    props : ['item']
}
</script>

<style scoped>
.menu_layer_2 {
	font-size: 20px;
	margin-top: 1px;
	margin-left: 40px;
	padding-left: 5px;
	width: 156px;
	/*float: left;*/
	display: flex;
	
	/*边框属性*/
	border-style: ridge;
	border-color: navajowhite;
}

.menu_layer_2 img {
	align-self: center;

	width: 20px;
}

.menu_layer_2 label {
	align-self: center;
	padding-left: 8px;
}
</style>