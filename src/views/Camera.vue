<template>
    <div style="display: flex;flex-direction: row;justify-content: space-around;width:100%;height:100%;">
        <div style="height: 500px;width:900px;border: 2px dotted;">
            <img src="{{url_for('index.video_feed')}}" class="img-fluid" height="500">
        </div>
        <el-card style="width:300px;height:500px;">


        </el-card>
    </div>
</template>