<template>
    <!-- 搜索框 -->
    <div class="searchAdmin" style="display:flex;flex-direction: row;align-content:center;align-items:center;">
        <!-- <div style="width:290px;height:30px;border:2px solid;border-radius: 18px;display:flex;flex-direction: row;"> -->
        <el-date-picker v-model="searchData.date" type="date" format="YYYY-MM-DD" value-format="YYYY-MM-DD"
            placeholder="请选择要查询的日期" style="width:230px" />
        <button class="searchAdminBtn" @click="searchInf">搜索</button>
    </div>

    <!-- </div> -->
    <div>
        <el-table class="infTable" :data="tableData" style="width: 100%" :row-class-name="tableRowClassName">
            <el-table-column prop="eventID" label="序号" sortable width="100" />
            <el-table-column prop="event_start" label="时间" sortable width="250" />
            <el-table-column prop="event_type" label="事件类型" sortable width="180" />
            <el-table-column prop="event_location" label="发生地点" width="180" />
            <el-table-column prop="elderlyName" label="老人姓名" sortable width="180" />
        </el-table>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            searchData: {
                date: null,
            },
            tableData: [],

        }
    },
    created() {
        //获取实时报表列表请求
        axios.post(`http://127.0.0.1:5000/event/search`, { event_type: null }).then(res => {
            console.log(res)
            this.tableData = res.data.data;
            for (let i = 0; i < res.data.data.length; i++) {
                if (res.data.data[i].event_type == 0) {

                }
            }
        }).catch(err => {
            console.log(err.response)
        })
    },
    methods: {
        tableRowClassName({row, rowIndex}) {

    if (row.event_type === "摔倒") {
      return 'warning-row';
    } else if (row.event_type === "开心") {
      return 'success-row';
    }
    return '';
  },
        searchInf() {

        },
    }
}
</script>
<style>
    .el-table .warning-row {
      background: oldlace;
    }
  
    .el-table .success-row {
      background: #f0f9eb;
    }
  </style>