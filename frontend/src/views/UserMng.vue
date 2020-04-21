<template>
	<div class="op-space">
		<!--这里来个搜索框-->
		<div class="block">
			<search-block style="margin: 0 auto;" v-bind:fields="tablefields"></search-block>
		</div>
		
		<!--这里来个操作栏-->
		<div class="block">
			<operation-bar></operation-bar>
		</div>

		<!--这里来个信息框-->
		<div class="block" style="overflow-x: scroll;overflow-y: scroll;position: absolute;top: 170px; bottom: 0px;left: 0px;right: 0px;background-color: wheat;">
			<table-block v-bind:fields="tablefields" v-bind:rows="rows" ></table-block>
		</div>
		<!--这里来个状态栏-->
	</div>
</template>

<script>
import searchblock from "../components/searchblock"
import operationbar from "../components/operationbar"
import tableblock from "../components/tableblock"

export default {
	name: 'UserMng',
	components: {
		'search-block': searchblock,
		'operation-bar': operationbar,
		'table-block': tableblock,
	},
	props: ['fields'],
	data: function(){
		return {
			tablefields: ['姓名','性别','号码','邮箱'],
			rows: [[1,2,3,4],[3,4,5,6],[5,6,7,8]]
		}
	}
}
</script>
<style scoped>
.op-space {
	position: absolute;
	top: 60px;
	left: 210px;
	bottom: 0px;
	right: 0px;
	background-color: azure;

}
.block {
	margin-top: 10px;
	background-color: wheat; 
	margin-left:10px; 
	margin-right:10px;
}
</style>