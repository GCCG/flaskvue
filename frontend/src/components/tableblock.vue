<!--
 * @Author: your name
 * @Date: 2020-04-20 21:16:04
 * @LastEditTime: 2020-05-22 10:11:24
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /frontend/src/components/tableblock.vue
 -->
<template>
    <table border="1" >
		<tr>
			<th v-for="(field, fieldindex) in fields" :key="field+'-'+fieldindex">{{field}}</th>
		</tr>
		<tr v-for="(row, rowindex ) in rows" :key="rowindex" ref="tableRows"  v-on:click="onClickTr(rowindex)" v-bind:style="rowStyles[rowindex]">
			<td style="background-color: inherit"  v-for="(value,columnindex) in row" :key="rowindex+'-'+columnindex" >{{value}}</td>
		</tr>
    </table>
</template>
<script>


const NORMAL_ROW_COLOR = 'honeydew'
const SELECTED_ROW_COLOR = '#99CCCC'
const SELECTION_EVENT = 'selectionChanged'

export default {
    name:'table-block',
	props:['fields','rows'],
	
	data: function(){
		return {
			selectedRows: [],
			rowStyles: [],
			selectedNum: 0,
			
		}
	},
	watch:{
		rows:{ 
			handler: function(rows){
				console.log("updated data, rows length is: "+rows.length)
				this.selectedRows = new Array(rows.length).fill(0)
				this.selectedNum = 0
				//this.rowStyles = new Array(rows.length).fill({backgroundColor: NORMAL_ROW_COLOR})
				this.rowStyles = []
				for(let i=0; i<this.rows.length; i++){
					this.rowStyles.push({backgroundColor: NORMAL_ROW_COLOR,}) 
				}
				this.$emit(SELECTION_EVENT, this.selectedRows, this.selectedNum)
			},
			immediate: true
		}
	},
	
	methods: {
		onClickTr: function(num){
			console.log('In onClickTr, num is: '+num)
			// console.log('rowStyles is: '+JSON.stringify(this.rowStyles))
			if(this.selectedRows[num]==0){
				this.selectedRows[num] = 1
				this.selectedNum += 1
				// console.log("changed color of row "+num)
				this.rowStyles[num].backgroundColor = SELECTED_ROW_COLOR
			}
			else{
				this.selectedRows[num] = 0
				this. selectedNum -= 1
				console.log("changed color of row "+num)
				this.rowStyles[num].backgroundColor = NORMAL_ROW_COLOR
			}
			// console.log("current selectedRows: "+this.selectedRows)
			// console.log("current rowStyles: "+this.rowStyles[0].backgroundColor+this.rowStyles[1].backgroundColor+this.rowStyles[2].backgroundColor)
			this.$emit(SELECTION_EVENT, this.selectedRows, this.selectedNum)
		},
		selectAll: function(){
			console.log('Here is in table-block, selectAll!')
			for(let i=0; i<this.rowStyles.length;i++){
				this.rowStyles[i].backgroundColor = SELECTED_ROW_COLOR
				this.selectedRows[i] = 1
			}
			this.selectedNum = this.rowStyles.length
			console.log('Length of rowStyles is: '+this.rowStyles.length)
			this.$emit(SELECTION_EVENT, this.selectedRows, this.selectedNum)
		}
	},
	
	// mounted: function(){
	// 	this.selectedRows = new Array(this.rows.length).fill(0)
	// 	//this.rowStyles = new Array(this.rows.length).fill({backgroundColor: NORMAL_ROW_COLOR,})
	// 	//this.rowStyles = [{backgroundColor: NORMAL_ROW_COLOR,},{backgroundColor: NORMAL_ROW_COLOR,},{backgroundColor: NORMAL_ROW_COLOR,}]
	// 	//this.rowStyles = new Array(this.rows.length)
	// 	for(let i=0; i<this.rows.length; i++){
	// 		this.rowStyles.push({backgroundColor: NORMAL_ROW_COLOR,}) 
	// 	}
	// 	console.log("Table block created! rows.length is "+this.rows.length)
	// }
	
	
}
</script>

<style scoped>


table {
	min-width: 100%;
	margin: 0 auto;
	border-radius: 5px;
}

/* 表格的样式*/
td,th {
	font-family: 仿宋,georgia;
	background-color: honeydew;
	height: 100%;
	margin: 0px;
	padding: 0px;
	text-align: center;
}
</style>