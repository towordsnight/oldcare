<template>
    <div>
        <el-table :data="tableData" style="width: 100%" :row-class-name="tableRowClassName">
            <el-table-column prop="date" label="时间" width="180" />
            <el-table-column prop="name" label="Name" width="180" />
            <el-table-column prop="address" label="Address" />
        </el-table>
    </div>
</template>

<script>
export default {
    data() {
        return {

        }
    },
    methods: {
    }
}
</script>


