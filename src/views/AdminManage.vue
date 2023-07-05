<template>
    <div
        style="display: flex;flex-direction: row;justify-content: space-between;align-items:center;width:1200px;margin-bottom: 30px;">
        <!-- 搜索框 -->
        <!-- <div style="display: inline-block;width: 800px;"> -->
        <div class="searchAdmin" style="display:flex;flex-direction: row;align-content:center;align-items:center;">
            <div style="width:290px;height:30px;border:2px solid;border-radius: 18px;display:flex;flex-direction: row;">
                <svg t="1688457189199" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                    p-id="21858" width="25" height="25">
                    <path d="M474.453333 884.053333c-225.28 0-409.6-184.32-409.6-409.6s184.32-409.6 409.6-409.6 409.6 184.32 409.6 
                    409.6-184.32 409.6-409.6 409.6z m0-68.266666c187.733333 0 341.333333-153.6 
                    341.333334-341.333334s-153.6-341.333333-341.333334-341.333333-341.333333 153.6-341.333333 341.333333 153.6 
                    341.333333 341.333333 341.333334z m252.586667 54.613333c-13.653333-13.653333-10.24-37.546667 
                    3.413333-47.786667s37.546667-10.24 47.786667 3.413334l64.853333 78.506666c13.653333 13.653333 10.24 
                    37.546667-3.413333 47.786667s-37.546667 10.24-47.786667-3.413333l-64.853333-78.506667z"
                        fill="#515151" p-id="21859"></path>
                </svg>
                <input class="searchinput" />
            </div>
            <button class="searchAdminBtn">搜索</button>
        </div>
        <!-- </div> -->

        <!-- 添加按钮 -->
        <div>
            <button class="addAdminBtn" @click="addAdminBtn">
                <svg t="1688519056341" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                    p-id="2704" width="20" height="20">
                    <path d="M514.972672 25.220096c-261.41696 0-473.339904 211.922944-473.339904 473.339904 0 261.424128 211.922944 473.344 
                    473.339904 473.344 261.419008 0 473.34912-211.919872 473.34912-473.344C988.321792 237.14304 776.39168 25.220096 
                    514.972672 25.220096zM810.990592 516.393984l-277.533696 0.64-0.584704 278.121472c-0.039936 10.202112-8.31488 
                    18.477056-18.516992 18.477056l-0.039936 
                    0c-10.202112-0.039936-18.477056-8.31488-18.477056-18.556928l0.582656-277.955584-277.376 0.64-0.039936 
                    0c-10.202112 0-18.477056-8.274944-18.516992-18.477056 0-10.202112 8.233984-18.516992 18.477056-18.556928l277.533696-0.64 
                    0.584704-278.121472c0.039936-10.202112 8.31488-18.477056 18.516992-18.477056l0.039936 0c10.202112 0.039936 
                    18.477056 8.31488 18.477056 18.556928L533.53472 480l277.376-0.64 0.039936 0c10.202112 0 18.477056 8.274944 
                    18.516992 18.477056C829.467648 508.039168 821.233664 516.353024 810.990592 516.393984z"
                        fill="#2c2c2c" p-id="2705"></path>
                </svg>
                <span>添加</span>

            </button>
        </div>
    </div>

     <!-- 添加信息弹出框 -->
     <div>
        <el-dialog v-model="addAdminVisible" title="修改信息" style="width:550px;">
                <div style="margin-left:30px;width:450px;height:210px;">
                <el-form-item label="姓名：" style="margin-left: 32px;">
                    <el-input v-model="addData.name" style="width:300px" placeholder="请输入姓名" />
                </el-form-item>
                <el-form-item label="真实姓名：" style="margin-left: 32px;">
                    <el-input v-model="addData.real_name" style="width:300px" placeholder="请输入真实姓名" />
                </el-form-item>
                <el-form-item label="性别：" style="margin-left: 32px;">
                    <el-radio-group v-model="addData.genre">
                        <el-radio label="女" size="large">女</el-radio>
                        <el-radio label="男" size="large">男</el-radio>
                    </el-radio-group>
                </el-form-item>
                <el-form-item label="邮箱：" style="margin-left: 32px;">
                    <el-input v-model="addData.email" style="width:300px" placeholder="请输入邮箱" />
                </el-form-item>
                <el-form-item label="电话：" style="margin-left: 32px;">
                    <el-input v-model="addData.phone" style="width:300px" placeholder="请输入电话" />
                </el-form-item>
                
                </div>
            
            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="addAdminVisible = false">取消</el-button>
                    <el-button type="primary" @click="addAdmin">
                        确定
                    </el-button>
                </span>
            </template>
        </el-dialog>
    </div>


    <!-- 工作人员数据表格 -->
    <div>
        <el-table :data="tableData" style="width: 100%">
            <el-table-column fixed prop="oldno" label="序号" width="70" />
            <el-table-column fixed prop="name" label="姓名" width="120" />
            <el-table-column prop="real_name" label="用户真实姓名" width="120" />
            <el-table-column prop="sex" label="性别" width="120" />
            <el-table-column prop="email" label="邮箱" width="100" />
            <el-table-column prop="phone" label="电话" width="150" />
            <el-table-column fixed="right" label="操作" width="250">
                <template #default>
                    <!-- <el-button link type="primary" size="small" @click="handleClick">详情</el-button> -->
                    <el-button link type="primary" size="small" @click="modifyAdminBtn">修改</el-button>
                    <el-button link type="primary" size="small" @click="deleteAdmin">删除</el-button>
                </template>
            </el-table-column>
        </el-table>
    </div>

    <!-- 修改信息弹出框 -->
    <div>
        <el-dialog v-model="modifyAdminVisible" title="修改信息" style="width:550px;">
                <div style="margin-left:30px;width:450px;height:210px;">
                <el-form-item label="姓名：" style="margin-left: 32px;">
                    <el-input v-model="modifyData.name" style="width:300px" placeholder="请输入姓名" />
                </el-form-item>
                <el-form-item label="真实姓名：" style="margin-left: 32px;">
                    <el-input v-model="modifyData.real_name" style="width:300px" placeholder="请输入真实姓名" />
                </el-form-item>
                <el-form-item label="性别：" style="margin-left: 32px;">
                    <el-radio-group v-model="modifyData.genre">
                        <el-radio label="女" size="large">女</el-radio>
                        <el-radio label="男" size="large">男</el-radio>
                    </el-radio-group>
                </el-form-item>
                <el-form-item label="邮箱：" style="margin-left: 32px;">
                    <el-input v-model="modifyData.email" style="width:300px" placeholder="请输入邮箱" />
                </el-form-item>
                <el-form-item label="电话：" style="margin-left: 32px;">
                    <el-input v-model="modifyData.phone" style="width:300px" placeholder="请输入电话" />
                </el-form-item>
                
                </div>
            
            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="modifyAdminVisible = false">取消</el-button>
                    <el-button type="primary" @click="modifyAdmin">
                        确定
                    </el-button>
                </span>
            </template>
        </el-dialog>
    </div>
</template>

<script>
export default {
    data() {
        return {
            addAdminVisible: false,
            addData:{},
            modifyAdminVisible: false,
            tableData: [
                {
                    date: '2016-05-03',
                    name: 'Tom',
                    state: 'California',
                    city: 'Los Angeles',
                    address: 'No. 189, Grove St, Los Angeles',
                    zip: 'CA 90036',
                    tag: 'Home',
                },
                {
                    date: '2016-05-02',
                    name: 'Tom',
                    state: 'California',
                    city: 'Los Angeles',
                    address: 'No. 189, Grove St, Los Angeles',
                    zip: 'CA 90036',
                    tag: 'Office',
                },
                {
                    date: '2016-05-04',
                    name: 'Tom',
                    state: 'California',
                    city: 'Los Angeles',
                    address: 'No. 189, Grove St, Los Angeles',
                    zip: 'CA 90036',
                    tag: 'Home',
                },
                {
                    date: '2016-05-01',
                    name: 'Tom',
                    state: 'California',
                    city: 'Los Angeles',
                    address: 'No. 189, Grove St, Los Angeles',
                    zip: 'CA 90036',
                    tag: 'Office',
                },
            ],
            modifyData:{
                name:null,
            }
        }
    },
    methods: {
        //添加按钮
        addAdminBtn() {
            this.addAdminVisible = true;
        },
        //弹出框中的添加按钮
        addAdmin() {
            this.addAdminVisible = false;
        },
        //表格中修改按钮
        modifyAdminBtn() {
            this.modifyAdminVisible = true;
        },
        //弹出框中的修改按钮
        modifyAdmin() {
            this.modifyAdminVisible = false;
        },
        deleteAdmin() {

        }
    }
}
</script>

<style>
/* 搜索框样式 */
.searchinput {
    width: 250px;
    height: 27px;
    border: 0;
    appearance: none;
    outline: 0;
}

.searchinput:focus {
    border: 0;
    appearance: none;
}

.searchinput:hover {
    border: 0;
    appearance: none;
}

/* 搜索按钮样式 */
.searchAdminBtn {
    line-height: 15px;
    width: 150px;
    font-size: 20px;
    margin-left: 10px;
    background-color: rgb(91, 171, 125);
    padding: 14px 40px;
    color: #fff;
    text-transform: uppercase;
    letter-spacing: 2px;
    cursor: pointer;
    border-radius: 10px;
    border: 2px dashed rgb(91, 171, 125);
    box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
    transition: .4s;
}

.searchAdminBtn span:last-child {
    display: none;
}

.searchAdminBtn:hover {
    transition: .4s;
    border: 2px dashed rgb(91, 171, 125);
    background-color: #fff;
    color: rgb(91, 171, 125);
}

.searchAdminBtn:active {
    background-color: #87dbd0;
}

/* 添加按钮样式 */
.addAdminBtn {
    border: 1px solid rgb(91, 171, 125);
    border-radius: 5px;
    background: rgb(255, 255, 255);
    color: rgb(91, 171, 125);
    font-style: italic;
    padding: 10px;
    padding-right: 14px;
    padding-left: 12px;
    font-size: 17px;
    display: flex;
    flex-direction: row;
    align-content: center;
    align-items: center;
}

.addAdminBtn:hover {
    background-color: rgb(91, 171, 125);
    color: white;
    border: 1px solid rgb(91, 171, 125);
}
</style>