<!--
 * @Author: your name
 * @Date: 2020-04-20 10:14:45
 * @LastEditTime: 2020-05-22 15:09:23
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

		<!--这里来个弹窗-->
		<pop-window class="popwindow" v-if="edit_pop" @Cancel="onEditCancel" @OK="onEditOK" :title='edit_pop_title' :fields='pop_fields'></pop-window>
		<pop-window class="popwindow" v-if="add_pop" @Cancel="onAddCancel" @OK="onAddOK" :title='add_pop_title' :fields='pop_fields'></pop-window>
		<!-- <p>什么情况？</p> -->
	</div>
</template>

<script>
import searchblock from "../../components/searchblock"
import operationbar from "../../components/operationbar"
import tableblock from "../../components/tableblock"
import popwindow from "../../components/popwindow"
// import BACKEND_API_PREFIX from "../../backend_api/restful_api"
import backendApi from "../../restful_api/backend_api"
import axios from 'axios'
import qs from 'qs'
// import func from '../../../vue-temp/vue-editor-bridge'


export default {
	name: 'RoleMng',
	components: {
		'search-block': searchblock,
		'operation-bar': operationbar,
		'table-block': tableblock,
		'pop-window': popwindow,
	},
	props: ['fields'],
	data: function(){
		return {
			tablefields: ['姓名','性别','号码','邮箱'],
			// tablefields: [],
			rows: [[1,2,3,4],[3,4,5,6],[5,6,7,8]],
			// rows: [],
			// api: BACKEND_API_PREFIX + '/user',
			field_num: 0,
			row_num: 0,
			selected_num: 0,
			selected_rows: [],
			params: {},
			add_pop: 0,
			add_pop_title: '新增角色',
			edit_pop: 0,
			edit_pop_title: '编辑角色',
			edit_index: -1,
			pop_fields:[
				// {
				// 	field_name: 'user_id',
				// 	value: null,
				// 	config: {
				// 		type: 'input',
				// 	}
				// },
				{
					field_name: 'role_name',
					value: null,
					config: {
						type: 'input',
					}
				},
				{
					field_name: 'description',
					value: null,
					config: {
						type: 'textarea',
					}
				},
			]
		}
	},
	methods: {
		func1: function(response) {
			console.log(response.data.resource.role_list)
			this.tablefields = []
			// var i = 0
			if (response.data.resource.message !=''){
				alert(response.data.message)
				return 
			}
			var role_list = response.data.resource.role_list
			for (let key in role_list[0]){
				this.tablefields.push(key)
				this.params[key] = null
				// i = i +1 
			}
			this.rows = role_list
					
			this.field_num = this.tablefields.length
			this.row_num = this.rows.length
			this.selected_num = 0
			console.log(this.tablefields)
			console.log('params is '+JSON.stringify(this.params))
			// console.log(this.field_num)
		},
		func2: function(){
			axios.get(backendApi.role).then(this.func1)
			// console.log('Message after add operation is: '+JSON.stringify(response))
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

			axios.get(backendApi.role, {params: this.params}).then(this.queryUsers)
		},
		onAdd: function(){
			// axios.get(backendApi.role, {method: 'put'})
		},
		queryUsers: function(response){
			
			console.log(response.data.resource.role_list)
			this.rows = response.data.resource.role_list
			this.field_num = this.tablefields.length
			this.row_num = this.rows.length
			this.selected_num = 0
		},
		onOperation: function(operation){
			console.log('In onOperation, operation is: '+operation)
			if(operation == 'SELECTALL'){
				this.$refs.tableblock.selectAll()
			}
			else if(operation == 'ADD'){
				for(let i=0; i<this.pop_fields.length;i++){
					this.pop_fields[i]['value'] = null
				}
				this.add_pop = 1
			}
			else if(operation == 'DELETE'){
				// console.log('this.rows is: ')
				for(let i=0; i<this.rows.length;i++){
					if(this.selected_rows[i]==1){
						console.log('Delete user with id '+this.rows[i]['user_id'])
						axios.delete(
							backendApi.role,
							{
								headers: {
									'Content-Type': 'application/x-www-form-urlencoded',
								},
								data: qs.stringify(this.rows[i])
							}).then(this.func2)
					}
				}
			}
			else if(operation == 'EDIT'){
				for(let i=0;i<this.rows.length;i++){
					if(this.selected_rows[i]==1){
						for(let j=0; j<this.pop_fields.length; j++){
							this.pop_fields[j]['value'] = this.rows[i][this.pop_fields[j]['field_name']]
						}
						this.edit_pop =1
						this.edit_index = i
						break
					}
				}

			}
		},
		onAddCancel: function(){
			this.add_pop = 0
			console.log('add_pop is: '+this.add_pop)
		},
		onAddOK: function(info){
			console.log("Info in popwindow is: "+JSON.stringify(info))
			axios.put(
				backendApi.role,
				qs.stringify(info),
				{
					headers: {
						'Content-Type': 'application/x-www-form-urlencoded', 
					}
				}).then(this.func2)
			this.add_pop = 0
		},
		onEditCancel: function(){
			this.edit_pop = 0
		},
		onEditOK: function(info){
			for(let key in info){
				this.rows[this.edit_index][key] = info[key]
			}
			axios.post(
				backendApi.role,
				qs.stringify(this.rows[this.edit_index]),
				{
					headers:{
						'Content-Type': 'application/x-www-form-urlencoded', 
					}
				}
			).then(this.func2)
			this.edit_pop = 0
		}
	},
	created: function() {
		axios.get(backendApi.role).then(this.func1)
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
	background-color: white;

}
.block {
	margin-top: 10px;
	/*background-color: wheat; */
	background-color: white;
	margin-left:10px; 
	margin-right:10px;
}

.table-block {
	margin-top: 10px;
	/*background-color: wheat; */
	background-color: white;
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

.popwindow {
	/* position: absolute;
	top: 50%;
	left: 50%; */

	position:fixed;
	top:0;
	right:0;
	left:0;
	bottom:0;
	margin:auto; 
}
</style>