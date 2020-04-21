<template>
    <table border="1" >
		<tr>
			<th v-for="(field, fieldindex) in fields" :key="field+'-'+fieldindex">{{field}}</th>
		</tr>
		<tr v-for="(row, rowindex ) in rows" :key="rowindex">
			<td v-for="(value,columnindex) in row" :key="rowindex+'-'+columnindex" style="text-align: center;">{{value}}</td>
		</tr>
    </table>
</template>
<script>
export default {
    name:'table-block',
    props:['fields','rows'],
}
</script>

<style scoped>


table {
	min-width: 970px;
	margin: 0 auto;
}

/* 表格的样式*/
td,th {
	font-family: 仿宋,georgia;
	background-color: honeydew;
	height: 100%;
	margin: 0px;
	padding: 0px;
}
</style>