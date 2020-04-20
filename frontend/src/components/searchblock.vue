<template>
    <div class='searchblock'>
		<div>
			<search-field v-bind:fields="fields" v-on:selectchanged='fieldChanged1' v-on:inputchanged='valueChanged1'></search-field>
			<search-field v-bind:fields="fields" v-on:selectchanged='fieldChanged2' v-on:inputchanged='valueChanged2'></search-field>
			<search-field v-bind:fields="fields" v-on:selectchanged='fieldChanged3' v-on:inputchanged='valueChanged3'></search-field>
		</div>
		<img v-bind:style='imgStyle' v-on:mouseleave='onMouseLeave' v-on:mouseup='onMouseUp' v-on:mousedown='onMouseDown' v-on:click='submitQuery' src="../assets/icons/search_icon.png" />
	</div>
</template>

<script>
import searchField from '@/components/searchfield.vue'

export default {
    name:'search-block',
    components:{
        'search-field': searchField
    },
    props: ['fields'],
    data: function(){
		return {
			queryInfo: [
				{field:'',value:''},
				{field:'',value:''},
				{field:'',value:''},
			],
			imgBorderStyle: 'outset'
						
						
		}
	},
	computed: {
		imgStyle: function() {
			return {"border-style":this.imgBorderStyle}
		}
    },
	methods: {
		fieldChanged1: function(field){
			this.queryInfo[0].field = field
		},
		fieldChanged2: function(field){
            this.queryInfo[1].field = field
		},
		fieldChanged3: function(field){
			this.queryInfo[2].field = field
		},
		valueChanged1: function(value){
			this.queryInfo[0].value = value
		},
		valueChanged2: function(value){
			this.queryInfo[1].value = value
		},
		valueChanged3: function(value){
			this.queryInfo[2].value = value
		},
		submitQuery: function(){
            this.$emit('submitquery',this.queryInfo)
            console.log('submitQuery')
		},
					
		//把img元素包装成button效果
		onMouseDown: function(){
			this.imgBorderStyle = 'inset'
		},
		onMouseUp: function(){
			this.imgBorderStyle = 'outset'
		},
		onMouseLeave: function(){
			this.imgBorderStyle = 'outset'
		}
	},
}
</script>

<style>
.searchblock {
	/*float: left;*/
	
	border-style: dashed;
	border-color: grey;
	/*border-radius: 5px;*/
	margin: 10px;
	
	padding-left: 3px;
	padding-right: 3px;
	display: flex; 
	height: 100px; 
	width: 320px;
	background-color: azure;
}

.searchblock img {
	background-color: aliceblue;
	margin-left: 10px;
	margin-top: 0px;
	flex-direction: row;
	align-self: center;
	border-radius: 15px;
	width: 50px; 
	border-style: outset; 
	border-color: aquamarine;
}
.searchblock div {
	flex-direction: row; 
	align-self: center;
}
</style>