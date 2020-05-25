<!--
 * @Author: your name
 * @Date: 2020-04-20 11:11:17
 * @LastEditTime: 2020-05-22 15:11:51
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /frontend/src/components/searchfield.vue
--> 
<template>
    <div style="display: flex; ">
		<select class='fieldselect' v-model='selectedField' v-on:change='selectChanged' >
			<option v-for="field in fields" :key="field" v-bind:value="field">{{field}}</option>
		</select>
		<input class='fieldvalue' v-model='inputValue' v-on:change='inputChanged' type="text"/>
	</div>
</template>

<script>
export default {
	name: 'search-field',
    props: ['fields'],  //一个对外调用接口，用于输入select元素的option
    data: function(){
        return {selectedField: '',inputValue: ''}
    },
    methods:{
		selectChanged: function(){
			this.$emit('selectchanged',this.selectedField)
		},
		inputChanged: function(){
			this.$emit('inputchanged', this.inputValue)
		}
	}, 
}
</script>

<style>
/*搜索条目中的select框*/
.fieldselect {
	border-width: 2px;
	border-radius: 5px;
	border-color: gray;
	border-style: solid;
	line-height: 25px;
	flex-direction: row; 
	margin: 0px; 
	background-color: #CCFFFF;
	width: 70px;
}
/*搜索条目中的input框*/
.fieldvalue {
	border-width: 2px;
	border-radius: 5px;
	border-color: gray;
	border-style: solid;
	line-height: 25px;
	margin: 0px; 
	margin-left: 1px;
	flex-direction: row;
	background-color: aliceblue;
}
</style>