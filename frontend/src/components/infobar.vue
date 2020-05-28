<!--
 * @Author: your name
 * @Date: 2020-05-27 09:23:01
 * @LastEditTime: 2020-05-27 10:10:42
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /frontend/src/components/infobar.vue
--> 
<template>
    <div class='info-bar' >
		<!-- <label >{{label}}</label> -->
        <div class="label" v-for="(value, key) in info" :key="key">
            <b>{{key}}: </b>{{value}}
        </div>
	</div>

    

</template>

<script>

// const eventName = 'operation'

export default {
    name: 'info-bar',
    props: ['info'],
    data: function(){
        return {
            label: '',
        }
    },
    
    methods:{
        resetLabel: function(info){
            this.label = ''
            for(let key in info){
                this.label = this.label + key + ': ' + info[key] + ' || '
            }
            console.log('In info-bar, resetLable, label is:'+this.label)
        },
    },
    watch: {
        info: {
            handler: function(){
                this.label = ''
                for(let key in this.info){
                    this.label = this.label + key + ': ' + this.info[key] + ' || '
                }
            },
            immediate: true,
        }
    }
}
</script>

<style scoped>
.info-bar {
    height: 30px; 
    /* display: flex; */
    /*background-color: aliceblue;*/
    background-color: inherit; 
    left: 0px; 
    right: 0px; 
    margin-left: 0px;
    /* overflow-y: scroll; */
    overflow-y:scroll;
    /* width: 1000px; */
    max-width: 100%;
    
}
.label {
    font-family: 仿宋,georgia;
    float: left;
    margin-bottom: 0px;
    margin-top: 0px; 
    margin-left: 0px;
    margin-right: 20px;
    padding-left: 20px;
    padding-right: 10px;
    min-width: 100px;
    max-width: 400px;
    /* width: 400px; */
    overflow-x: hidden;
    /*background-color: antiquewhite;*/
    /*background-color: #FFFFCC; */
    background-color: #FFCCCC;
    line-height: 30px;

    text-align:left;

    border-radius: 5px;
}
</style>