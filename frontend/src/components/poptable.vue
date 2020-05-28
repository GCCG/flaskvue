<!--
 * @Author: your name
 * @Date: 2020-05-25 16:53:16
 * @LastEditTime: 2020-05-28 11:37:38
 * @LastEditors: Please set LastEditors
 * @Description: 一个弹出列表。通过选定列表中的条目，并点击“确定”按钮，就会出发“OK”事件，并返回列表条目被选中的情况。
                在本项目中，用于在‘权限配置’功能中给群组添加角色，给角色添加权限。
 * @FilePath: /frontend/src/components/poptable.vue
--> 
<template>
    <div class="poptable">
        <div style="text-align: center; margin-bottom:10px;font-weight:bold">{{title}}</div>
        <div class="table-container">
            <table-block :fields='fields' :rows='rows' @selectionChanged='onSelectionChanged(arguments)'></table-block>
        </div>
        <!-- <p>什么情况？</p> -->
        <div style="margin-top:15px">
            <button style="float:left" @click="onOK">确定</button>
            <button style="float:right" @click="onCancel">取消</button>
        </div>
    </div>
</template>

<script>
import tableBlock from "../components/tableblock"

export default {
    props:['fields', 'rows', 'title'],
    components:{
        'table-block': tableBlock,
    },
    data: function(){
        return {
            selectedRows: []
        }
    },
    methods:{
        onOK: function(){
            this.$emit('OK',this.selectedRows)
        },
        onSelectionChanged: function(args){
            this.selectedRows = args[0]
        },
        onCancel: function(){
            this.$emit('Cancel')
        }
    },
    watch:{
        rows:{
            handler: function(rows){
                this.selectedRows = new Array(rows.length).fill(0)
            }
        }
    }
    
}
</script>

<style scoped>
.poptable {
    background-color:aliceblue;
    width: fit-content;
    text-align: left;
    height: fit-content;
    padding: 10px;
    border-style:ridge;
    border-color: aqua;
    border-radius: 8px;
    padding-left: 40px;
    padding-right: 40px;
}

.table-container {
    max-width: 600px;
    max-height: 400px;
    overflow-x: scroll;
	overflow-y: scroll;
}
</style>