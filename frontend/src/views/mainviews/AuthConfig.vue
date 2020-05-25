<!--
 * @Author: your name
 * @Date: 2020-05-21 11:30:37
 * @LastEditTime: 2020-05-25 11:48:37
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /frontend/src/views/mainviews/AuthConfig.vue
--> 
<template>
    <div class="op-space">
        <!--页签-->
        <div class="menu">
            <div style="height:40px;margin:0 auto;width:fit-content;">
                <!-- <p>什么情况？</p> -->
                <label :class="{selectedtag:selectedTag == 'tagGroupRole', tag: selectedTag != 'tagGroupRole'}" @click="onTagGroupRole('tagGroupRole')">群组-角色</label>
                <label :class="{selectedtag:selectedTag == 'tagRolePrivilege', tag: selectedTag != 'tagRolePrivilege'}" @click="onTagRolePrivilege('tagRolePrivilege')">角色-权限</label>
            </div>
        </div>

        <!--页面-->
        <div class="page">
            <div v-if="tagGroupRole" >
                <div>
                    <search-block style="margin: 10px auto;" :fields='groupfields' v-on:submitquery='onSearchGroupRoles'></search-block>
                </div>

                <div class='block'>
                    <configurable-operation-bar :info='table_info' :buttons='buttons' @operation='onOperation'></configurable-operation-bar>
                </div>

                <div class="table-block">
                    <table-block style="margin-top: 10px;margin-bottom:20px;" :fields="rolefields" :rows="rolerows"></table-block>
                </div>
            </div>

            <div v-if="tagRolePrivilege">
                <div>
                    <search-block style="margin: 10px auto;" :fields='rolefields' @submitquery='onSearchRolePrivileges'></search-block>
                </div>

                <div class='block'>
                    <configurable-operation-bar :info='table_info' :buttons='buttons' @operation='onOperation'></configurable-operation-bar>
                </div>

                <div class="table-block">
                    <table-block  style="margin-top: 10px;" :fields="privilegefields" :rows="privilegerows"></table-block>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// const SELECTED_TAG_COLOR = "bisque"
import searchBlock from "../../components/searchblock"
import tableBlock from "../../components/tableblock"
import backendApi from "../../restful_api/backend_api"
import configurableOperationBar from "../../components/configurableoperationbar"
import axios from 'axios'
// import qs from 'qs'

export default {
    name: "AuthConfig",
    components: {
        'search-block': searchBlock,
        'table-block':tableBlock,
        'configurable-operation-bar': configurableOperationBar,
    },
    data: function(){
        return {
            tagGroupRole: 1,
            tagRolePrivilege: 0,
            selectedTag: 'tagGroupRole',
            groupfields:[],
            rolefields: [],
            privilegefields: ['Cart', 'Apple', 'Banana', 'Pear', 'Rose'],
            rolerows: [
                ["good","good","good","good","good"],
                ["1","2","3","4","5"],
                ["1","2","3","4","5"],
                ["1","2","3","4","5"],
            ],
            privilegerows: [
                ["good","good","good","good","good"],
                ["1","2","3","4","5"],
                ["1","2","3","4","5"],
                ["1","2","3","4","5"],
            ],
            params: {},
            role_field_num: 0,
            role_row_num: 0,
            role_selected_num: 0,
            privilege_field_num: 0,
            privilege_row_num: 0,
            privilege_selected_num: 0,
            buttons:[
                {
                    field:'全选',
                    event_option:'ALLSELECT',
                },
                {
                    field:'添加',
                    event_option:'ADD',
                },
                {
                    field:'移除',
                    event_option:'REMOVE'
                },
            ],
            table_info:[
                {
                    field:'字段',
                    value:0
                },
                {
                    field:'条目',
                    value:0
                },
                {
                    field:'选中',
                    value:0
                },
            ]
            
        }
    },
    methods: {
        onTagGroupRole: function(tag){
            this.tagGroupRole = 1
            this.tagRolePrivilege = 0
            this.selectedTag = tag
        },
        onTagRolePrivilege: function(tag){
            this.tagRolePrivilege = 1
            this.tagGroupRole = 0
            this.selectedTag = tag
        },
        handleGroupRoles: function(response){
            console.log('In AuthConfig handleGroupRoles, response is: '+JSON.stringify(response))
            // console.log(response.data.resource.role_list)
			this.rolefields = []
			// var i = 0
			if (response.data.resource.message !=''){
				alert(response.data.message)
				return 
			}
			var role_list = response.data.resource.role_list
			for (let key in role_list[0]){
				this.rolefields.push(key)
				this.params[key] = null
				// i = i +1 
			}
			this.rolerows = role_list
					
			this.role_field_num = this.rolefields.length
			this.role_row_num = this.rolerows.length
			this.role_selected_num = 0
			console.log('Role fields are: '+this.rolefields)
			console.log('params is '+JSON.stringify(this.params))
			// console.log(this.field_num)
        },
        handleRolePrivileges: function(response){
            console.log('In AuthConfig handleRolePrivileges, response is: '+JSON.stringify(response))
            // console.log(response.data.resource.role_list)
			this.privilegefields = []
			// var i = 0
			if (response.data.resource.message !=''){
				alert(response.data.message)
				return 
			}
			var privilege_list = response.data.resource.privilege_list
			for (let key in privilege_list[0]){
				this.privilegefields.push(key)
				this.params[key] = null
				// i = i +1 
			}
			this.privilegerows = privilege_list
					
			this.privilege_field_num = this.privilegefields.length
			this.privilege_row_num = this.privilegerows.length
			this.privilege_selected_num = 0
			console.log('Role fields are: '+this.privilegefields)
			console.log('params is '+JSON.stringify(this.params))
			// console.log(this.field_num)
        },
        handleGroupfields: function(response){
            this.groupfields = []
			// var i = 0
			if (response.data.resource.message !=''){
				alert(response.data.message)
				return 
			}
			var group_list = response.data.resource.group_list
			for (let key in group_list[0]){
				this.groupfields.push(key)
			}
			console.log('groupfields is: '+this.groupfields)
        },
        onSearchRolePrivileges: function(queryinfo){
            this.params = {}
            console.log('In onSearchRolePrivileges, queryinfo is: '+queryinfo)
			for (let index in queryinfo){
				if(queryinfo[index]['field'] != ''){
					console.log('info is: '+JSON.stringify(queryinfo[index]))
					this.params[queryinfo[index]['field']] = queryinfo[index]['value']
				}
			}
			console.log('parameters are: '+JSON.stringify(this.params))

			axios.get(backendApi.role_privileges, {params: this.params}).then(this.queryRolePrivileges)
        },
        onSearchGroupRoles: function(queryinfo){
            this.params = {}
            console.log('In onSearchGroupRoles, queryinfo is: '+queryinfo)
			for (let index in queryinfo){
				if(queryinfo[index]['field'] != ''){
					console.log('info is: '+JSON.stringify(queryinfo[index]))
					this.params[queryinfo[index]['field']] = queryinfo[index]['value']
				}
			}
			console.log('parameters are: '+JSON.stringify(this.params))

			axios.get(backendApi.group_roles, {params: this.params}).then(this.queryGroupRoles)
        },
        queryGroupRoles: function(response){
            var role_list = response.data.resource.role_list
            console.log('In queryGroupRoles, role_list is: '+JSON.stringify(role_list))
            if (role_list != null){
                this.rolerows = role_list
            }
            else{
                this.rolerows = []
            }
			
			// this.field_num = this.rolefields.length
			this.row_num = this.rolerows.length
			this.selected_num = 0
        },
        queryRolePrivileges: function(response){
            var privilege_list = response.data.resource.privilege_list
            console.log('In queryRolePrivileges, privilege_list is: '+JSON.stringify(privilege_list))
            if(privilege_list != null){
                this.privilegerows = privilege_list
            }
            else{
                this.privilegerows = []
            }

			// this.field_num = this.privilegefields.length
			this.row_num = this.rolerows.length
			this.selected_num = 0
        },
        onOperation: function(event_option){
            console.log('In onOperation, event option is: '+event_option)
        },
    },
    created: function(){
        axios.get(backendApi.group_roles).then(this.handleGroupRoles)
        axios.get(backendApi.group).then(this.handleGroupfields)
        axios.get(backendApi.role_privileges).then(this.handleRolePrivileges)
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
	background-color: white;;
    /* border-radius: 10px; */
    /* border-style: solid; */
    
}

.menu {
    height:42px;
    background-color: #CCFFCC;
}

/* .page {
    border-style: dotted;
    border-width: 5px;
    border-radius: 10px;
} */

.tag {
    margin-left: 0px;
    margin-right: 1px;
    margin-top: 0px;
    margin-bottom: 0px;
    float: left;
    height: 40px;
    width: 100px;
    border-style: solid;
    border-width: 1px;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    border-bottom-color: #CCFFCC;
    background-color: #CCFFCC;
}

.selectedtag {
    margin-left: 0px;
    margin-right: 1px;
    margin-top: 0px;
    margin-bottom: 0px;
    float: left;
    height: 40px;
    width: 100px;
    border-style: solid;
    border-width: 1px;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    border-bottom-color: white;
    background-color: white;; 
}

.block {
	margin-top: 10px;
	/*background-color: wheat; */
	/* background-color: #CCFFFF; */
	background-color: white;
	margin-left:10px; 
	margin-right:10px;
}

.table-block {
	margin-top: 10px;
	/*background-color: wheat; */
	/* background-color: white; */
	background-color: white;;
	margin-left:10px; 
	margin-right:10px;
	overflow-x: scroll;
	overflow-y: scroll;
	position: absolute;
	top: 180px;
	bottom: 0px;
	left: 0px;
	right: 0px;
}

</style>