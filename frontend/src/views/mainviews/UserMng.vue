<!--
 * @Author: your name
 * @Date: 2020-04-20 10:14:45
 * @LastEditTime: 2020-05-19 15:34:33
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /frontend/src/views/mainviews/UserMng.vue
 -->
<template>
	<div class="op-space">
		<!--这里来个搜索框-->
		<div class="block">
			<search-block style="margin: 0 auto;" v-bind:fields="tablefields" v-on:submitquery='onSearch'></search-block>
		</div>
		
		<!--这里来个操作栏-->
		<div class="block">
			<operation-bar v-bind:field_num='field_num' v-bind:row_num='row_num' v-bind:selected_num='selected_num' v-on:tableoperation='onOperation'></operation-bar>
		</div>

		<!--这里来个信息框-->
		<div class="table-block">
			<table-block ref='tableblock' v-bind:fields="tablefields" v-bind:rows="rows" v-on:selectionChanged='onSelectionChanged(arguments)'></table-block>
		</div>
		<!--这里来个状态栏-->
	</div>
</template>

<script>
import searchblock from "../../components/searchblock"
import operationbar from "../../components/operationbar"
import tableblock from "../../components/tableblock"
import BACKEND_API_PREFIX from "../../backend_api/restful_api"
import axios from 'axios'


export default {
	name: 'UserMng',
	components: {
		'search-block': searchblock,
		'operation-bar': operationbar,
		'table-block': tableblock,
	},
	props: ['fields'],
	data: function(){
		return {
			tablefields: ['姓名','性别','号码','邮箱'],
			// tablefields: [],
			rows: [[1,2,3,4],[3,4,5,6],[5,6,7,8]],
			// rows: [],
			api: BACKEND_API_PREFIX + '/user',
			field_num: 0,
			row_num: 0,
			selected_num: 0,
			selected_rows: [],
			params: {},
		}
	},
	methods: {
		func1: function(response) {
			console.log(response.data.resource.user_list)
			this.tablefields = []
			// var i = 0
			var user_list = response.data.resource.user_list
			for (let key in user_list[0]){
				this.tablefields.push(key)
				this.params[key] = null
				// i = i +1 
			}
			this.rows = user_list
					
			this.field_num = this.tablefields.length
			this.row_num = this.rows.length
			this.selected_num = 0
			console.log(this.tablefields)
			console.log('params is '+JSON.stringify(this.params))
			// console.log(this.field_num)
		},
		onSelectionChanged: function(args){
			this.selected_rows = args[0]
			this.selected_num = args[1]
			console.log('Selection is: '+args[0]+' selected_num is '+args[1])
		},
		onSearch: function(queryinfo){
			this.params = {}
			for (let index in queryinfo){
				if(queryinfo[index]['field'] != ''){
					console.log('info is: '+JSON.stringify(queryinfo[index]))
					this.params[queryinfo[index]['field']] = queryinfo[index]['value']
				}
			}
			console.log('parameters are: '+JSON.stringify(this.params))

			axios.get(this.api, {params: this.params}).then(this.queryUsers)
		},
		queryUsers: function(response){
			
			console.log(response.data.resource.user_list)
			this.rows = response.data.resource.user_list
			this.field_num = this.tablefields.length
			this.row_num = this.rows.length
			this.selected_num = 0
		},
		onOperation: function(operation){
			console.log('In onOperation, operation is: '+operation)
			if(operation == 'SELECTALL'){
				this.$refs.tableblock.selectAll()
			}
			
		}
	},
	created: function() {
		axios.get(this.api).then(this.func1)
	}

}
</script>
<style scoped>
.op-space {
	position: absolute;
	top: 60px;
	left: 210px;
	bottom: 0px;
	right: 0px;
	background-color: azure;

}
.block {
	margin-top: 10px;
	/*background-color: wheat; */
	background-color: #CCFFFF;
	margin-left:10px; 
	margin-right:10px;
}

.table-block {
	margin-top: 10px;
	/*background-color: wheat; */
	background-color: #CCFFFF;
	margin-left:10px; 
	margin-right:10px;
	overflow-x: scroll;
	overflow-y: scroll;
	position: absolute;
	top: 160px;
	bottom: 0px;
	left: 0px;
	right: 0px;
}
</style>