<!--
 * @Author: your name
 * @Date: 2020-04-20 21:01:18
 * @LastEditTime: 2020-05-19 14:56:17
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /frontend/src/components/operationbar.vue
 -->
<template>
    <div class='operationbar' >
		<label >字段：{{field_num}}；条目：{{row_num}}；选中：{{selected_num}}</label>
		<button type="button" @click="onAllSelect">全选</button>
		<button type="button" @click="onDelete">删除</button>
		<button type="button" @click="onEdit">编辑</button>
		<button type="button" @click="onAdd">新增</button>
						
	</div>

</template>

<script>

const eventName = 'tableoperation'

export default {
    name: 'operation-bar',
    props: ['field_num','row_num', 'selected_num'],
    methods:{
        onAllSelect: function(){
            console.log('In onAllSelect')
            this.$emit(eventName,'SELECTALL')
        },
        onDelete: function(){
            this.$emit(eventName, 'DELETE')
        },
        onEdit: function(){
            this.$emit(eventName, 'EDIT')
        },
        onAdd: function(){
            this.$emit(eventName, 'ADD')
        },
    }
}
</script>

<style scoped>
.operationbar {
    height: 30px; 
    display: flex;
    /*background-color: aliceblue;*/
    background-color: inherit; 
    left: 0px; 
    right: 0px; 
    margin-left: 0px;
    
}
div label {
    font-family: 仿宋,georgia;
    margin-bottom: 0px;
    margin-top: 0px; 
    margin-left: 0px;
    width: 400px;
    /*background-color: antiquewhite;*/
    /*background-color: #FFFFCC; */
    background-color: #FFCCCC;
    line-height: 30px;

    border-radius: 5px;
}

div button {
    font-family: 仿宋,georgia;
    margin-bottom: 2px;
    margin-top: 2px;
    flex-direction: row;
    margin-left: 10px; 
    width: 60px;
}
</style>