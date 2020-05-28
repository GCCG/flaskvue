<!--
 * @Author: your name
 * @Date: 2020-05-21 11:30:37
 * @LastEditTime: 2020-05-28 11:56:46
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
                    <info-bar ref='groupInfoBar' :info='group' ></info-bar>
                </div>

                <div class='block'>
                    <configurable-operation-bar ref='groupRoleBar' :info='role_table_info' :buttons='buttons' @operation='onGroupRoleOperation'></configurable-operation-bar>
                </div>

                <div class="table-block">
                    <table-block ref="groupRoleTable" style="margin-top: 10px;margin-bottom:20px;" :fields="rolefields" :rows="rolerows" v-on:selectionChanged='onGroupRoleSelectionChanged(arguments)'></table-block>
                </div>

                <!-- <div class="info-tag">
                    <label v-for="(value, field) in group" :key="value"><b>{{field}}</b>: <br/>{{value}}<br/><br/></label>
                </div> -->

                <pop-table class="pop-table" v-if="pop_role_add" :fields="rolefields" :rows="pop_role_table" :title="pop_role_title" @OK="onRoleAddOK" @Cancel="onRoleAddCancel"></pop-table>

            </div>

            <div v-if="tagRolePrivilege">
                <div>
                    <search-block style="margin: 10px auto;" :fields='rolefields' @submitquery='onSearchRolePrivileges'></search-block>
                </div>

                <div class='block'>
                    <info-bar ref='roleInfoBar' :info='role' ></info-bar>
                </div>

                <div class='block'>
                    <configurable-operation-bar ref='rolePrivilegeBar' :info='privilege_table_info' :buttons='buttons' @operation='onRolePrivilegeOperation'></configurable-operation-bar>
                </div>

                <div class="table-block">
                    <table-block ref='rolePrivilegeTable' style="margin-top: 10px;" :fields="privilegefields" :rows="privilegerows" v-on:selectionChanged='onRolePrivilegeSelectionChanged(arguments)'></table-block>
                </div>

                <pop-table class="pop-table" v-if="pop_privilege_add" :fields="privilegefields" :rows="pop_privilege_table" :title="pop_privilege_title" @OK="onPrivilegeAddOK" @Cancel="onPrivilegeAddCancel"></pop-table>
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
import infoBar from "../../components/infobar"
import popTable from "../../components/poptable"
import axios from 'axios'
import qs from 'qs'
// import func from '../../../vue-temp/vue-editor-bridge'
// import qs from 'qs'

export default {
    name: "AuthConfig",
    components: {
        'search-block': searchBlock,
        'table-block':tableBlock,
        'configurable-operation-bar': configurableOperationBar,
        'pop-table': popTable,
        'info-bar': infoBar,
    },
    data: function(){
        return {
            // 控制两个页签及其对应页面的切换
            tagGroupRole: 1,
            tagRolePrivilege: 0,
            selectedTag: 'tagGroupRole',

            // 存储两个页面中表格的信息
            groupfields:[],
            rolefields: [],
            privilegefields: ['Cart', 'Apple', 'Banana', 'Pear', 'Rose'],
            rolerows: [],
            privilegerows: [],

            // 存储搜索框传递来的搜索信息
            params: {},

            // ‘群组-角色’页面的群组信息
            group:{
                group_id:'',
                group_name:'',
                description:'',
            },
            // ‘群组-角色’页面，表格中角色的选中信息，
            role_selected_rows: [],
            

            role:{
                role_id:'',
                role_name:'',
                description:'',
            },
            privilege_selected_rows: [],
            
            // 可配置操作栏的按钮配置
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
           
           // 可配置操作栏中信息标签的信息
            role_table_info:{
                '字段':0,
                '条目':0,
                '选中':0,
            },
            privilege_table_info:{
                '字段':0,
                '条目':0,
                '选中':0,
            },

            // 用于控制’群组-角色‘页面的弹出表格
            pop_role_table: [],
            pop_role_add: 0,
            pop_role_title: '请选择需要添加的角色',

            // 用于控制’角色-权限‘页面的弹出表格
            pop_privilege_table: [],
            pop_privilege_add: 0,
            pop_privilege_title:'请选择需要添加的权限'
            
        }
    },
    methods: {
        onTagGroupRole: function(tag){
            this.tagGroupRole = 1
            this.tagRolePrivilege = 0
            this.selectedTag = tag
            this.pop_role_add = 0
        },
        onTagRolePrivilege: function(tag){
            this.tagRolePrivilege = 1
            this.tagGroupRole = 0
            this.selectedTag = tag
        },
        handleGroupRoles: function(response){
            // console.log('In AuthConfig handleGroupRoles, response is: '+JSON.stringify(response))
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
            this.group.group_id = response.data.resource.group_id
            this.group.group_name = response.data.resource.group_name
            this.group.description = response.data.resource.description
					
			// this.role_field_num = this.rolefields.length
			// this.role_row_num = this.rolerows.length
            // this.role_selected_num = 0
            this.initRoleTableInfo()
			console.log('Role fields are: '+this.rolefields)
			console.log('params is '+JSON.stringify(this.params))
			// console.log(this.field_num)
        },
        handleRolePrivileges: function(response){
            // console.log('In AuthConfig handleRolePrivileges, response is: '+JSON.stringify(response))
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
            this.role.role_id = response.data.resource.role_id
            this.role.role_name = response.data.resource.role_name
            this.role.description = response.data.resource.description
					
			// this.privilege_field_num = this.privilegefields.length
			// this.privilege_row_num = this.privilegerows.length
            // this.privilege_selected_num = 0
            this.initPrivilegeTableInfo()
			console.log('Privilege fields are: '+this.privilegefields)
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
            this.group['group_id'] = response.data.resource.group_id
            this.group['group_name'] = response.data.resource.group_name
            this.group.description = response.data.resource.description
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
            this.initRoleTableInfo()
        },
        queryRolePrivileges: function(response){
            this.role.role_id = response.data.resource.role_id
            this.role.role_name = response.data.resource.role_name
            this.role.description = response.data.resource.description
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
            this.initPrivilegeTableInfo()
        },
        onGroupRoleOperation: function(event_option){
            console.log('In onOperation, event option is: '+event_option)
            if(event_option == 'ALLSELECT'){
                this.$refs.groupRoleTable.selectAll()
                // this.initRoleTableInfo()
            }
            else if(event_option == 'ADD'){
                this.popAddRoles()
            }
            else if(event_option == 'REMOVE'){
                this.popDeleteRoles()
            }

        },
        onRolePrivilegeOperation: function(event_option){
            console.log('In onRolePrivilegeOperation, event option is: '+event_option)
            if(event_option == 'ALLSELECT'){
                this.$refs.rolePrivilegeTable.selectAll()
            }
            else if(event_option == 'ADD'){
                this.popAddPrivileges()
            }
            else if(event_option == 'REMOVE'){
                this.popDeletePrivileges()
            }
        },
        onGroupRoleSelectionChanged: function(args){
            this.role_selected_rows = args[0]
            // this.role_selected_num = args[1]
            this.role_table_info['选中'] = args[1]
            console.log('In AuthConfig, onGroupRoleSelectionChanged, args is: '+JSON.stringify(args))
            this.$refs.groupRoleBar.resetLabel(this.role_table_info)
            this.$refs.groupInfoBar.resetLabel(this.group)
            // this.$refs.groupRoleBar.resetLabel(Object.assign({},this.role_table_info, this.group))
        },
        onRolePrivilegeSelectionChanged: function(args){
            this.privilege_selected_rows = args[0]
            // this.role_selected_num = args[1]
            this.privilege_table_info['选中'] = args[1]
            console.log('In AuthConfig, onRolePrivilegeSelectionChanged, args is: '+JSON.stringify(args))
            this.$refs.rolePrivilegeBar.resetLabel(this.privilege_table_info)
            this.$refs.roleInfoBar.resetLabel(this.role)
        },
        initRoleTableInfo: function(){
            this.role_table_info['字段'] = this.rolefields.length
            this.role_table_info['条目'] = this.rolerows.length
            this.role_table_info['选中'] = 0
            // this.$set(this.role_table_info, 0, {field: '字段', value: this.rolefields.length})
            console.log('In initRoleTableInfo, role_table_info is: '+JSON.stringify(this.role_table_info))
            this.$refs.groupRoleBar.resetLabel(this.role_table_info)
            this.$refs.groupInfoBar.resetLabel(this.group)
            // this.$refs.groupRoleBar.resetLabel(Object.assign({},this.role_table_info, this.group))
        },
        initPrivilegeTableInfo: function(){
            this.privilege_table_info['字段'] = this.privilegefields.length
            this.privilege_table_info['条目'] = this.privilegerows.length
            this.privilege_table_info['选中'] = 0
            if(this.$refs.rolePrivilegeBar != null){
                this.$refs.rolePrivilegeBar.resetLabel(this.privilege_table_info)
                this.$refs.roleInfoBar.resetLabel(this.role)
            }
            else{
                console.log('In AuthConfig, initPRivilegeTAbleInfo, no element with reference rolePrivilegeBar')
            }
            // this.$set(this.privilege_table_info, 0, {field: '字段', value: this.rolefields.length})
            console.log('In initPrivilegeTableInfo, privilege_table_info is: '+JSON.stringify(this.privilege_table_info))
        },
        popAddRoles: function(){
            axios.get(backendApi.role).then(this.setPopRoleTable)
        },
        popAddPrivileges: function(){
            axios.get(backendApi.privilege).then(this.setPopPrivilegeTable)
        },
        popDeleteRoles: function(){
            // var tmp =null
            for(let i=0; i<this.role_selected_rows.length; i++){
                if(this.role_selected_rows[i] == 1){
                    console.log('In AuthConfig, popDeleteRoles, selected row is: '+i+' role is: '+JSON.stringify(this.rolerows[i]))
                    axios.delete(
                        backendApi.group_roles,
                        
                        {
                            headers:{
                                'Content-Type': 'application/x-www-form-urlencoded',
                            },
                            data: qs.stringify({group_id:this.group.group_id, role_id:this.rolerows[i].role_id}),
                        }
                    ).then(this.updateRoleTable) // .then(this.updateRoleTable)
                }
            }
            // if(tmp != null)
            //     tmp
            // console.log('In AuthConfig, popDeleteRoles, params is: '+JSON.stringify(this.params))
        },
        popDeletePrivileges: function(){
            // var tmp =null
            for(let i=0; i<this.privilege_selected_rows.length; i++){
                if(this.privilege_selected_rows[i] == 1){
                    console.log('In AuthConfig, popDeletePrivileges, selected row is: '+i+' privilege is: '+JSON.stringify(this.privilegerows[i]))
                    axios.delete(
                        backendApi.role_privileges,
                        
                        {
                            headers:{
                                'Content-Type': 'application/x-www-form-urlencoded',
                            },
                            data: qs.stringify({role_id:this.role.role_id, privilege_id:this.privilegerows[i].privilege_id}),
                        }
                    ).then(this.updatePrivilegeTable) // .then(this.updateprivilegeTable)
                }
            }
            // if(tmp != null)
            //     tmp.
            // console.log('In AuthConfig, popDeleteRoles, params is: '+JSON.stringify(this.params))
        },
        updateRoleTable: function(){
            axios.get(backendApi.group_roles, {params: this.params}).then(this.queryGroupRoles)
        },
        updatePrivilegeTable: function(){
            axios.get(backendApi.role_privileges,{params: this.params}).then(this.queryRolePrivileges)
        },
        setPopRoleTable: function(response){
            this.pop_role_table = response.data.resource.role_list
            console.log('In AuthConfig, setPopRoleTable, role_list is: '+JSON.stringify(response.data.resource.role_list))
            for(let i=0; i<this.pop_role_table.length; i++){
                for(let j=0; j<this.rolerows.length; j++){
                    if(this.rolerows[j]['role_id'] == this.pop_role_table[i]['role_id']){
                        this.pop_role_table.splice(i,1)
                        // break
                    }
                }
            }
            console.log('In AuthConfig, setPopRoleTable, pop_role_table is: '+JSON.stringify(this.pop_role_table))
            this.pop_role_add = 1
        },
        setPopPrivilegeTable: function(response){
            this.pop_privilege_table = response.data.resource.privilege_list
            console.log('In AuthConfig, setPopPrivilegeTable, privilege_list is: '+JSON.stringify(response.data.resource.privilege_list))
            for(let i=0; i<this.pop_privilege_table.length; i++){
                for(let j=0; j<this.privilegerows.length; j++){
                    if(this.privilegerows[j]['privilege_id'] == this.pop_privilege_table[i]['privilege_id']){
                        this.pop_privilege_table.splice(i,1)
                        // break
                    }
                }
            }
            console.log('In AuthConfig, setPopPrivilegeTable, pop_privilege_table is: '+JSON.stringify(this.pop_privilege_table))
            this.pop_privilege_add = 1
        },
        onRoleAddOK: function(selected_rows){
            var tmp = null
            for(let i=0; i<selected_rows.length; i++){
                // 对每一个被选定的行，将其对应的角色添加到群组中
                if(selected_rows[i] == 1){
                    console.log('In AuthConfig, onRoleAddOK, selected row is: '+i)
                    tmp = axios.post(
                        backendApi.group_roles,
                        qs.stringify({group_id:this.group.group_id,role_id:this.pop_role_table[i].role_id,}),
                        {
                            headers:{
                                'Content-Type': 'application/x-www-form-urlencoded',
                            },
                            // data: qs.stringify(
                            //     {
                            //         group_id: this.group.group_id,
                            //         role_id: this.pop_role_table[i].role_id,
                            //     }
                        // ),
                        }
                    )
                }
                
            }
            // 隐藏弹出窗口
            this.pop_role_add = 0
            // 更新显示的信息
            // axios.get(backendApi.group_roles, {params: this.params}).then(this.queryGroupRoles)
            if(tmp != null)
                tmp.then(this.updateRoleTable)
        },
        onPrivilegeAddOK: function(selected_rows){
            var tmp = null
            for(let i=0; i<selected_rows.length; i++){
                // 对每一个被选定的行，将其对应的角色添加到群组中
                if(selected_rows[i] == 1){
                    console.log('In AuthConfig, onPrivilegeAddOK, selected row is: '+i)
                    tmp = axios.post(
                        backendApi.role_privileges,
                        qs.stringify({role_id:this.role.role_id,privilege_id:this.pop_privilege_table[i].privilege_id,}),
                        {
                            headers:{
                                'Content-Type': 'application/x-www-form-urlencoded',
                            },
                            // data: qs.stringify(
                            //     {
                            //         role_id: this.role.role_id,
                            //         privilege_id: this.pop_privilege_table[i].privilege_id,
                            //     }
                        // ),
                        }
                    )
                }
                
            }
            // 隐藏弹出窗口
            this.pop_privilege_add = 0
            // 更新显示的信息
            // axios.get(backendApi.role_privileges, {params: this.params}).then(this.queryRoleprivileges)
            if(tmp != null)
                tmp.then(this.updatePrivilegeTable)
        },
        onRoleAddCancel: function(){
            this.pop_role_add = 0
        },
        onPrivilegeAddCancel: function(){
            this.pop_privilege_add = 0
        }
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
	top: 230px;
	bottom: 0px;
	left: 0px;
	right: 0px;
}

.info-tag {
    margin-top: 20px;
    text-align: left;
	/*background-color: wheat; */
	/* background-color: white; */
	background-color: white;;
	margin-left:10px; 
	margin-right:10px;
	position: absolute;
	top: 190px;
	/* bottom: 0px; */
    height: fit-content;
	left: 0px;
	width: 200px;
    padding: 10px;
    border-style: double;
    border-width: 2px;
    border-radius: 5px;
    border-color: #CCFFCC;
}

.pop-table {
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