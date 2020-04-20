
<template>
	<div >
		<img src="../assets/icons/station_icon.png" style="height: 100px;float: left;" >
		<label>名称：**小站</label>
		<br />
		<a href="test.html">详情</a>
		<a href="test.html">连接</a>
		<br />
		<a href="test.html">移除</a>
		<a href="test.html">编辑</a>
		<br />
	</div>
</template>

<script>
	module.exports = {
        name: 'big-tag',
		props: ['info'],
	}
</script>

<style scoped="">
div {
	float: left;
	margin: 10px 10px 10px 10px; 
	border-radius: 5px; 
	border-style: dashed; 
	width: 120px;
	background-color: antiquewhite; 
	text-align: center; 
	padding-left: 0px; 
	padding-bottom: 5px;
	padding-top: 5px;
}
</style>
