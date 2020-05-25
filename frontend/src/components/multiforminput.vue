<!--
 * @Author: your name
 * @Date: 2020-05-20 08:57:00
 * @LastEditTime: 2020-05-20 16:55:16
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /frontend/src/components/multiform_input.vue
--> 
<template>
    <div>
        <div style="margin-bottom:5px;margin-top:5px">
            <label >{{field_name}}:</label>
        </div>
        
        <!-- <p>In multiform-input</p> -->
        <div>
            <input v-model="content" v-if="config['type']=='input'" v-on:change='onChange' />
            <!-- <p>{{config['type']}}</p> -->

            <select v-model="content" v-if="config['type']=='select'" v-on:change='onChange'>
                <option v-for="option in config['options']" :key="option" :value='option'>{{option}}</option>
            </select>
            <textarea v-model="content" v-if="config['type']=='textarea'" v-on:change="onChange">
            </textarea>
        </div>
       
    </div>
</template>

<script>
export default {
    name: 'multiform-input',
    props:['field_name','config', 'value'],
    data: function(){
        return {
            content: null,
        }
    },
    methods:{
        onChange: function(){
            console.log('In multiform-input, onChange, content is:'+this.content)
            this.$emit('inputChanged', {field_name: this.field_name, content: this.content})
        }
    },
    created: function(){
        console.log('multform-input created, config is: '+JSON.stringify(this.config))
        this.content = this.value
    }
    
}
</script>

<style scoped>
select {
    min-width: 100px;
    background-color:antiquewhite;
}
input {
    /* min-width: 100px; */
    background-color:aqua;
    height: auto;
}
textarea {
    min-height: 100px;
    background-color:aqua;
    /* min-width: 100px; */
}
</style>