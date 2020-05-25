<!--
 * @Author: your name
 * @Date: 2020-05-22 15:36:05
 * @LastEditTime: 2020-05-25 11:39:18
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /frontend/src/components/configableoperationbar.vue
--> 
<template>
    <div class='operationbar' >
		<label >{{label}}</label>
		<!-- <button type="button" @click="onAllSelect">全选</button>
		<button type="button" @click="onDelete">删除</button>
		<button type="button" @click="onEdit">编辑</button>
		<button type="button" @click="onAdd">新增</button> -->
        <button type="button" v-for="button in buttons" :key="button.field" @click="onClick(button)">{{button.field}}</button>
						
	</div>

</template>

<script>

const eventName = 'operation'

export default {
    name: 'configurable-operation-bar',
    props: ['info','buttons'],
    label: '',
    methods:{
        onClick: function(button){
            this.$emit(eventName, button.event_option)
        }
    },
    watch: {
        info: {
            handler: function(){
                this.label = ''
                for(let index in this.info){
                    this.label = this.label +this.info[index].field + '：' + this.info[index].value +'；'
                }
            },
            immediate: true,
        }
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