<!--
 * @Author: your name
 * @Date: 2020-05-19 16:59:17
 * @LastEditTime: 2020-05-20 16:54:03
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /frontend/src/views/popviews/add_user.vue
--> 
<template>
    <div class='popwindow'>
        <div style="text-align: center; margin-bottom:10px;">
            {{title}}
        </div>
        <div v-for="field in fields" :key="field['field_name']">
            
            <multiform-input :value="field['value']" :field_name="field['field_name']" :config="field['config']" @inputChanged="onInputChanged"></multiform-input>
            <!-- <p>{{JSON.stringify(field['config'])}}</p> -->
        </div>
        <div style="margin-top:15px;">
            <button style="float;left;margin-left:20px;margin-right:20px;" @click="onOK">确定</button>
            <button style="float:right;margin-left:20px;margin-right:20px;" @click="onCancel">取消</button>
        </div>
            
    </div>
</template>

<script>
import multiformInput from './multiforminput';

export default {
    props:['fields', 'url', 'title'],
    components:{
        'multiform-input': multiformInput,
    },
    data: function(){
        return {
            info: {}
        }
    },
    methods:{
        onInputChanged: function(info){
            console.log('In onInputChanged, content is:'+info['content']+' field_name is '+info['field_name'])
            this.info[info['field_name']] = info['content']
        },
        onOK: function(){
            this.$emit('OK', this.info)
        },
        onCancel: function(){
            this.$emit('Cancel')
        }
    }

    
}
</script>

<style scoped>
.popwindow {
    background-color:aliceblue;
    width: 200px;
    text-align: left;
    height: fit-content;
    padding: 10px;
    border-style:ridge;
    border-color: aqua;
    border-radius: 8px;
    padding-left: 40px;
    padding-right: 40px;
}
form {
    align-content: left;
}
</style>