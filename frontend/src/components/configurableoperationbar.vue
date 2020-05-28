<!--
 * @Author: your name
 * @Date: 2020-05-22 15:36:05
 * @LastEditTime: 2020-05-28 11:16:32
 * @LastEditors: Please set LastEditors
 * @Description: 可配置的操作栏。拥有一个信息label和一组操作按钮。
                信息label接受对象info作为初始显示信息，并通过方法resetLabel来重置信息。
                操作按钮根据对象数组buttons来创建多个button
 * @FilePath: /frontend/src/components/configableoperationbar.vue
--> 
<template>
    <div class='operationbar' >
		<label >{{label}}</label>
        <button type="button" v-for="button in buttons" :key="button.field" @click="onClick(button)">{{button.field}}</button>
						
	</div>

</template>

<script>

const eventName = 'operation'

export default {
    name: 'configurable-operation-bar',
    props: ['info','buttons'],
    data: function(){
        return {
            label: '',
        }
    },
    
    methods:{
        onClick: function(button){
            this.$emit(eventName, button.event_option)
            // this.resetLabel([])
        },
        resetLabel: function(info){
            this.label = ''
            for(let key in info){
                this.label = this.label + key + '：' + info[key] + '；'
            }
            console.log('In configurableoperationbar, resetLable, label is:'+this.label)
        },
    },
    watch: {
        info: {
            handler: function(){
                this.label = ''
                for(let key in this.info){
                    this.label = this.label + key + '：' + this.info[key] + '；'
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