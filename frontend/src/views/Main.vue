<template>
	<div class="op-space">
		<!--这里来个搜索框-->
		<search-block v-bind:fields="fields"></search-block>
		<!--这里来个操作栏-->
		<!--这里来个信息框-->
		<!--这里来个状态栏-->
	</div>
</template>

<script>
import searchblock from "../components/searchblock"

export default {
	components: {
		'search-block': searchblock,
	},
	props: ['fields'],
	data: function(){
		return {

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
	background-color: antiquewhite;
}
</style>