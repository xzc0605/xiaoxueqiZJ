<template>
    <div>
<!--        占位-->
<!--        <el-image></el-image>-->
        <video ref="video" style="width: 100%;height: 200px" autoplay></video>
        <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
            <div style="margin-left: 1rem"><p>原因（必填）：</p></div>
            <div class="titleinput row-right">
                <el-input  placeholder="原因"
                           autosize ></el-input>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "addPeople",
        mounted() {
            this.callCamera()
        },
        methods:{
            callCamera () {
                // H5调用电脑摄像头API
                navigator.mediaDevices.getUserMedia({
                    video: true
                }).then(success => {
                    // 摄像头开启成功
                    this.$refs['video'].srcObject = success
                    // 实时拍照效果
                    this.$refs['video'].play()
                }).catch(error => {
                    console.error('摄像头开启失败，请检查摄像头是否可用！')
                })
            },
        }
    }
</script>

<style scoped>

</style>
