<template>
    <div
        style="display: flex;flex-direction: row;justify-content: space-between;align-items:center;width:1200px;margin-bottom: 30px;">
        <!-- 搜索框 -->
        <!-- <div style="display: inline-block;width: 800px;"> -->
        <div class="searchOld" style="display:flex;flex-direction: row;align-content:center;align-items:center;">
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
            <button class="searchOldBtn">搜索</button>
        </div>
        <!-- </div> -->

        <!-- 添加按钮 -->
        <div>
            <button class="addOldBtn" @click="addOldBtn">
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
        <el-dialog v-model="addOldVisible" title="修改信息" style="width:1050px;">
            <div style="display: flex;flex-direction: row;">
                <div style="margin-left:30px;width:450px;height:450px;">
                <el-form-item label="姓名：" style="margin-left: 32px;">
                    <el-input v-model="addData.name" style="width:300px" placeholder="请输入姓名" />
                </el-form-item>
                <el-form-item label="性别：" style="margin-left: 32px;">
                    <el-radio-group v-model="addData.genre">
                        <el-radio label="女" size="large">女</el-radio>
                        <el-radio label="男" size="large">男</el-radio>
                    </el-radio-group>
                </el-form-item>
                <el-form-item label="电话：" style="margin-left: 32px;">
                    <el-input v-model="addData.phone" style="width:300px" placeholder="请输入电话" />
                </el-form-item>
                <el-form-item label="身份证号：" style="margin-left: 32px;">
                    <el-input v-model="addData.id_card" style="width:300px" placeholder="请输入身份证号" />
                </el-form-item>
                <el-form-item label="出生日期：" style="margin-left: 32px;">
                    <el-input v-model="addData.birthday" style="width:300px" placeholder="请输入出生日期" />
                </el-form-item>
                <el-form-item label="入住养老院日期：" style="margin-left: 32px;">
                    <el-input v-model="addData.checkin_date" style="width:300px" placeholder="请输入入住养老院日期" />
                </el-form-item>
                <el-form-item label="离开养老院日期：" style="margin-left: 32px;">
                    <el-input v-model="addData.checkout_date" style="width:300px" placeholder="请输入离开养老院日期" />
                </el-form-item>
                <el-form-item label="房间号：" style="margin-left: 32px;">
                    <el-input v-model="addData.room_number" style="width:300px" placeholder="请输入离开房间号" />
                </el-form-item>
                <el-form-item label="健康状况：" style="margin-left: 32px;">
                    <el-input v-model="addData.health_state" style="width:300px" placeholder="请输入健康状况" />
                </el-form-item>
                
                </div>

                <div style="margin-left:30px;width:450px;height:450px;">
                    <el-form-item label="描述：" style="margin-left: 32px;">
                    <el-input v-model="addData.description" style="width:300px;" type="textarea" clearable
                        :autosize="{ minRows: 5, maxRows: 10 }" maxlength="1000" placeholder="请输入描述" />
                </el-form-item>
                <el-form-item label="第一监护人姓名：" style="margin-left: 32px;">
                    <el-input v-model="addData.firstguardian_name" style="width:300px" placeholder="请输入第一监护人姓名" />
                </el-form-item>
                <el-form-item label="与第一监护人关系：" style="margin-left: 32px;">
                    <el-input v-model="addData.firstguardian_relationship" style="width:300px" placeholder="请输入与第一监护人关系" />
                </el-form-item>
                <el-form-item label="第一监护人电话：" style="margin-left: 32px;">
                    <el-input v-model="addData.firstguardian_phone" style="width:300px" placeholder="请输入第一监护人电话" />
                </el-form-item>
                <el-form-item label="第一监护人微信：" style="margin-left: 32px;">
                    <el-input v-model="addData.firstguardian_wechat" style="width:300px" placeholder="请输入第一监护人微信" />
                </el-form-item>
                <el-form-item label="第二监护人姓名：" style="margin-left: 32px;">
                    <el-input v-model="addData.secondguardian_name" style="width:300px" placeholder="请输入第二监护人姓名" />
                </el-form-item>
                <el-form-item label="与第二监护人关系：" style="margin-left: 32px;">
                    <el-input v-model="addData.secondguardian_relationship" style="width:300px" placeholder="请输入与第二监护人关系" />
                </el-form-item>
                <el-form-item label="第二监护人电话：" style="margin-left: 32px;">
                    <el-input v-model="addData.secondguardian_phone" style="width:300px" placeholder="请输入第二监护人电话" />
                </el-form-item>
            </div>
            </div>
            
            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="addOldVisible = false">取消</el-button>
                    <el-button type="primary" @click=addOld>
                        确定
                    </el-button>
                </span>
            </template>
        </el-dialog>
    </div>


    <!-- 老年人数据表格 -->
    <div>
        <el-table :data="tableData" style="width: 100%">
            <el-table-column fixed type="expand">
                <template #default="props">
                    <div style="margin-left: 50px;">
                        <div style="margin-top: 5px;">
                            <span style="display: inline-block;width: 240px;font-size: 16px;">健康状况：{{
                                props.row.health_state }}</span>
                        </div>
                        <div style="margin-top: 5px;">
                            <span style="font-size: 16px;">描述：{{
                                props.row.description }}</span>
                        </div>
                        <div style="margin-top: 5px;">
                            <span style="display: inline-block;width: 240px;font-size: 16px;">第一监护人姓名：{{
                                props.row.firstguardian_name }}</span>
                            <span style="display: inline-block;width: 260px;font-size: 16px;">与第一监护人关系：{{
                                props.row.firstguardian_relationship }}</span>
                            <span style="display: inline-block;width: 290px;font-size: 16px;">第一监护人电话：{{
                                props.row.firstguardian_phone }}</span>
                            <span style="display: inline-block;width: 290px;font-size: 16px;">第一监护人微信：{{
                                props.row.firstguardian_wechat }}</span>
                        </div>
                        <div style="margin-top: 5px;">
                            <span style="display: inline-block;width: 240px;font-size: 16px;">第二监护人姓名：{{
                                props.row.secondguardian_name }}</span>
                            <span style="display: inline-block;width: 260px;font-size: 16px;">与第二监护人关系：{{
                                props.row.secondguardian_relationship }}</span>
                            <span style="display: inline-block;width: 290px;font-size: 16px;">第二监护人电话：{{
                                props.row.secondguardian_phone }}</span>
                            <span style="display: inline-block;width: 290px;font-size: 16px;">第二监护人微信：{{
                                props.row.secondguardian_wechat }}</span>
                        </div>
                        <div style="margin-top: 5px;">
                            <span style="display: inline-block;width: 240px;font-size: 16px;">创建时间：{{
                                props.row.created }}</span>
                            <span style="display: inline-block;width: 240px;font-size: 16px;">创建人：{{
                                props.row.createdby }}</span>
                        </div>
                    </div>
                </template>

            </el-table-column>
            <el-table-column fixed prop="oldno" label="序号" width="70" />
            <el-table-column fixed prop="name" label="姓名" width="120" />
            <el-table-column prop="gender" label="性别" width="70" />
            <el-table-column prop="phone" label="电话" width="120" />
            <el-table-column prop="id_card" label="身份证号" width="100" />
            <el-table-column prop="birthday" label="出生日期" width="100" />
            <el-table-column prop="checkin_date" label="入住养老院日期" width="150" />
            <el-table-column prop="checkout_date" label="离开养老院日期" width="150" />
            <el-table-column prop="room_number" label="房间号" width="120" />
            <el-table-column fixed="right" label="操作" width="250">
                <template #default>
                    <!-- <el-button link type="primary" size="small" @click="handleClick">详情</el-button> -->
                    <el-button link type="primary" size="small" @click="modifyOldBtn">修改</el-button>
                    <el-button link type="primary" size="small" @click="deleteOld">删除</el-button>
                </template>
            </el-table-column>
        </el-table>
    </div>

    <!-- 修改信息弹出框 -->
    <div>
        <el-dialog v-model="modifyOldVisible" title="修改信息" style="width:1050px;">
            <div style="display: flex;flex-direction: row;">
                <div style="margin-left:30px;width:450px;height:450px;">
                <el-form-item label="姓名：" style="margin-left: 32px;">
                    <el-input v-model="modifyData.name" style="width:300px" placeholder="请输入姓名" />
                </el-form-item>
                <el-form-item label="性别：" style="margin-left: 32px;">
                    <el-radio-group v-model="modifyData.genre">
                        <el-radio label="女" size="large">女</el-radio>
                        <el-radio label="男" size="large">男</el-radio>
                    </el-radio-group>
                </el-form-item>
                <el-form-item label="电话：" style="margin-left: 32px;">
                    <el-input v-model="modifyData.phone" style="width:300px" placeholder="请输入电话" />
                </el-form-item>
                <el-form-item label="身份证号：" style="margin-left: 32px;">
                    <el-input v-model="modifyData.id_card" style="width:300px" placeholder="请输入身份证号" />
                </el-form-item>
                <el-form-item label="出生日期：" style="margin-left: 32px;">
                    <el-input v-model="modifyData.birthday" style="width:300px" placeholder="请输入出生日期" />
                </el-form-item>
                <el-form-item label="入住养老院日期：" style="margin-left: 32px;">
                    <el-input v-model="modifyData.checkin_date" style="width:300px" placeholder="请输入入住养老院日期" />
                </el-form-item>
                <el-form-item label="离开养老院日期：" style="margin-left: 32px;">
                    <el-input v-model="modifyData.checkout_date" style="width:300px" placeholder="请输入离开养老院日期" />
                </el-form-item>
                <el-form-item label="房间号：" style="margin-left: 32px;">
                    <el-input v-model="modifyData.room_number" style="width:300px" placeholder="请输入离开房间号" />
                </el-form-item>
                <el-form-item label="健康状况：" style="margin-left: 32px;">
                    <el-input v-model="modifyData.health_state" style="width:300px" placeholder="请输入健康状况" />
                </el-form-item>
                
                </div>

                <div style="margin-left:30px;width:450px;height:450px;">
                    <el-form-item label="描述：" style="margin-left: 32px;">
                    <el-input v-model="modifyData.description" style="width:300px;" type="textarea" clearable
                        :autosize="{ minRows: 5, maxRows: 10 }" maxlength="1000" placeholder="请输入描述" />
                </el-form-item>
                <el-form-item label="第一监护人姓名：" style="margin-left: 32px;">
                    <el-input v-model="modifyData.firstguardian_name" style="width:300px" placeholder="请输入第一监护人姓名" />
                </el-form-item>
                <el-form-item label="与第一监护人关系：" style="margin-left: 32px;">
                    <el-input v-model="modifyData.firstguardian_relationship" style="width:300px" placeholder="请输入与第一监护人关系" />
                </el-form-item>
                <el-form-item label="第一监护人电话：" style="margin-left: 32px;">
                    <el-input v-model="modifyData.firstguardian_phone" style="width:300px" placeholder="请输入第一监护人电话" />
                </el-form-item>
                <el-form-item label="第一监护人微信：" style="margin-left: 32px;">
                    <el-input v-model="modifyData.firstguardian_wechat" style="width:300px" placeholder="请输入第一监护人微信" />
                </el-form-item>
                <el-form-item label="第二监护人姓名：" style="margin-left: 32px;">
                    <el-input v-model="modifyData.secondguardian_name" style="width:300px" placeholder="请输入第二监护人姓名" />
                </el-form-item>
                <el-form-item label="与第二监护人关系：" style="margin-left: 32px;">
                    <el-input v-model="modifyData.secondguardian_relationship" style="width:300px" placeholder="请输入与第二监护人关系" />
                </el-form-item>
                <el-form-item label="第二监护人电话：" style="margin-left: 32px;">
                    <el-input v-model="modifyData.secondguardian_phone" style="width:300px" placeholder="请输入第二监护人电话" />
                </el-form-item>
            </div>
            </div>
            
            <template #footer>
                <span class="dialog-footer">
                    <el-button @click="modifyOldVisible = false">取消</el-button>
                    <el-button type="primary" @click=modifyOld>
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
            addOldVisible:false,
            addData:{},
            modifyOldVisible: false,
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
        addOldBtn(){
            this.addOldVisible = true;
        },
        //弹出框中的添加按钮
        addOld() {
            this.addOldVisible = false;
        },
        //表格中修改按钮
        modifyOldBtn() {
            this.modifyOldVisible = true;
        },
        //弹出框中的修改按钮
        modifyOld() {
            this.modifyOldVisible = false;
        },
        deleteOld() {

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
.searchOldBtn {
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

.searchOldBtn span:last-child {
    display: none;
}

.searchOldBtn:hover {
    transition: .4s;
    border: 2px dashed rgb(91, 171, 125);
    background-color: #fff;
    color: rgb(91, 171, 125);
}

.searchOldBtn:active {
    background-color: #87dbd0;
}

/* 添加按钮样式 */
.addOldBtn {
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

.addOldBtn:hover {
    background-color: rgb(91, 171, 125);
    color: white;
    border: 1px solid rgb(91, 171, 125);
}
</style>