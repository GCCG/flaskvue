<template>
	<div class='searchblock'>
		<div>
				<search-field v-bind:fields="fields" v-on:selectchanged='fieldChanged1' v-on:inputchanged='valueChanged1'></search-field>
				<search-field v-bind:fields="fields" v-on:selectchanged='fieldChanged2' v-on:inputchanged='valueChanged2'></search-field>
		</div>
		<div>
				<search-field v-bind:fields="fields" v-on:selectchanged='fieldChanged3' v-on:inputchanged='valueChanged3'></search-field>
				<search-field v-bind:fields="fields" v-on:selectchanged='fieldChanged3' v-on:inputchanged='valueChanged4'></search-field>
		</div>
		<img v-bind:style='imgStyle' v-on:mouseleave='onMouseLeave' v-on:mouseup='onMouseUp' v-on:mousedown='onMouseDown' v-on:click='submitQuery' src="../assets/icons/search_icon.png" />
	</div>
    
</template>

<script>
import searchField from '@/components/searchfield.vue'
// import func from '../../vue-temp/vue-editor-bridge'

export default {
    name:'search-block',
    components:{
        'search-field': searchField
    },
    props: ['fields'],
    data: function(){
		return {
			queryInfo: [
				{field:'',value:null},
				{field:'',value:null},
				{field:'',value:null},
				{field:'',value:null},
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
		fieldChanged4: function(field){
			this.queryInfo[3].field = field
		},
		valueChanged1: function(value){
			if(value !='')
				this.queryInfo[0].value = value
			else
				this.queryInfo[0].value = null
		},
		valueChanged2: function(value){
			if(value !='')
				this.queryInfo[1].value = value
			else
				this.queryInfo[1].value = null
		},
		valueChanged3: function(value){
			if(value !='')
				this.queryInfo[2].value = value
			else
				this.queryInfo[2].value = null
		},
		valueChanged4: function(value){
			if(value !='')
				this.queryInfo[3].value = value
			else
				this.queryInfo[3].value = null
		},
		submitQuery: function(){
            this.$emit('submitquery',this.queryInfo)
            console.log('submitquery')
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
		},

		onSearch: function(){
			this.$emit('searching', this.queryInfo)
		}
	},
}
</script>

<style>
.searchblock {
	/*float: left;*/
	
	border-style: dashed;
	border-color: grey;
	border-radius: 45px;
	border-width: 0px;

	/*block的边界和填充 */
	margin: 10px;
	padding-left: 40px;
	padding-right: 40px;
	display: flex; 

	height: 100px; 
	width: 550px;
	background-color: azure;

	/*使得block的宽度适应里面元素的宽度占用 */
	/* width: fit-content; */
}

.searchblock img {
	background-color: aliceblue;
	margin-left: 10px;
	margin-top: 0px;
	flex-direction: row;
	align-self: center;
	border-radius: 20px;
	width: 50px; 
	border-style: outset; 
	border-color: #CCFFFF;
}
.searchblock div {
	flex-direction: row; 
	align-self: center;
}
</style>