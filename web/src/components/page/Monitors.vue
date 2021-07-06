<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>
                    <i class="el-icon-pie-chart"></i> 监控信息
                </el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <p style="text-align: center">本页面拟存放摄像头监控画面</p>
            </div>

        </div>
    </div>
</template>

<script>
import Schart from 'vue-schart';
export default {
    name: 'Monitors',
    components: {

    },
    data() {
        return {

        };
    }
};
</script>

<style scoped>
.schart-box {
    display: inline-block;
    margin: 20px;
}
.schart {
    width: 600px;
    height: 400px;
}
.content-title {
    clear: both;
    font-weight: 400;
    line-height: 50px;
    margin: 10px 0;
    font-size: 22px;
    color: #1f2f3d;
}
</style>