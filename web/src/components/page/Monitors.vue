<template>
  <div>
    <div class="crumbs">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-pie-chart"></i> 监控信息
        </el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div class="camera_outer">
      <video id="videoCamera" :width="videoWidth" :height="videoHeight" autoplay></video>
      <canvas style="display:none;" id="canvasCamera" :width="videoWidth" :height="videoHeight"></canvas>
      <div v-if="imgSrc" class="img_bg_camera">
        <p>效果预览</p>
        <img :src="imgSrc" alt class="tx_img" />
      </div>
      <div class="button">
        <el-button @click="getCompetence()">打开摄像头</el-button>
        <el-button @click="stopNavigator()">关闭摄像头</el-button>
      </div>
    </div>


<!--        <el-card>
            <el-button @click="callCamera()" >1111</el-button>
            &lt;!&ndash;canvas截取流&ndash;&gt;
            <canvas ref="canvas" width="640" height="480"></canvas>
            &lt;!&ndash;图片展示&ndash;&gt;
            <video ref="video" width="640" height="480" autoplay></video>
            &lt;!&ndash;确认&ndash;&gt;
            <el-button size="mini" type="primary" @click="photograph">222222</el-button>
        </el-card>-->

        <div class="container">
           <!-- <p style="text-align: center">本页面拟存放摄像头监控画面</p>-->
          <el-table
              :data="eventData.slice((currentPage-1)*pagesize,currentPage*pagesize)"
              border
              class="table"
              ref="multipleTable"
              header-cell-class-name="table-header"
          >
            <el-table-column type="selection" width="55" align="center"></el-table-column>
            <el-table-column prop="id" label="ID" width="55" align="center"></el-table-column>
            <el-table-column prop="event_type" label="事件类型" align="center"></el-table-column>
            <el-table-column prop="event_location" label="地点" align="center"></el-table-column>
            <el-table-column prop="event_desc" label="描述" align="center"></el-table-column>
            <el-table-column prop="oldperson_id" label="老人id" align="center"></el-table-column>
          </el-table>

          <div style="text-align: center;margin-top: 30px;">
            <el-pagination
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                :current-page="currentPage"
                :page-sizes="[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]"
                :page-size="pagesize"
                :total="totalnums"
                layout="total, prev, pager, next">
            </el-pagination>
          </div>
        </div>
  </div>
</template>

<script>
import Schart from 'vue-schart';
import axios from "axios";
export default {
    inject:['reload'],
    name: 'Monitors',
    components: {

    },
    data() {
        return {
          videoWidth: 350,
          videoHeight: 350,
          imgSrc: "",
          thisCancas: null,
          thisContext: null,
          thisVideo: null,
          openVideo:false,






          timer:null,
          eventData:[],
          totalnums:0,
          pagesize: 10,
          currentPage: 1,
        };
    },
   mounted() {
      this.getEvent()                                                                                        /* 记得注释掉*/
 /*    this.timer = setInterval(() => {
       setTimeout(this.getEvent, 0)
     }, 2000*6)*/
  },
  destroyed () {
    clearInterval(this.timer)
  },
  methods: {
      getEvent(){
        axios({
          methods: 'get',
          url: axios.defaults.baseURL + 'delivery_Event',
        }).then((res) => {
          if (res.data.error === '0') {
            this.eventData=res.data.data
            this.totalnums=res.data.event_num
          }else{
            this.$message.error(res.data.messages)
          }
        })

      },

/*        // 调用摄像头
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
        },*/


    // 调用权限（打开摄像头功能）
    getCompetence() {
      var _this = this;
      _this.thisCancas = document.getElementById("canvasCamera");
      _this.thisContext = this.thisCancas.getContext("2d");
      _this.thisVideo = document.getElementById("videoCamera");
      _this.thisVideo.style.display = 'block';
      // 获取媒体属性，旧版本浏览器可能不支持mediaDevices，我们首先设置一个空对象
      if (navigator.mediaDevices === undefined) {
        navigator.mediaDevices = {};
      }
      // 一些浏览器实现了部分mediaDevices，我们不能只分配一个对象
      // 使用getUserMedia，因为它会覆盖现有的属性。
      // 这里，如果缺少getUserMedia属性，就添加它。
      if (navigator.mediaDevices.getUserMedia === undefined) {
        navigator.mediaDevices.getUserMedia = function(constraints) {
          // 首先获取现存的getUserMedia(如果存在)
          var getUserMedia =
              navigator.webkitGetUserMedia ||
              navigator.mozGetUserMedia ||
              navigator.getUserMedia;
          // 有些浏览器不支持，会返回错误信息
          // 保持接口一致
          if (!getUserMedia) {//不存在则报错
            return Promise.reject(
                new Error("getUserMedia is not implemented in this browser")
            );
          }
          // 否则，使用Promise将调用包装到旧的navigator.getUserMedia
          return new Promise(function(resolve, reject) {
            getUserMedia.call(navigator, constraints, resolve, reject);
          });
        };
      }
      var constraints = {
        audio: false,
        video: {
          width: this.videoWidth,
          height: this.videoHeight,
          transform: "scaleX(-1)"
        }
      };
      navigator.mediaDevices
          .getUserMedia(constraints)
          .then(function(stream) {
            // 旧的浏览器可能没有srcObject
            if ("srcObject" in _this.thisVideo) {
              _this.thisVideo.srcObject = stream;
            } else {
              // 避免在新的浏览器中使用它，因为它正在被弃用。
              _this.thisVideo.src = window.URL.createObjectURL(stream);
            }
            _this.thisVideo.onloadedmetadata = function(e) {
              _this.thisVideo.play();
            };
          })
          .catch(err => {
            console.log(err);
          });
    },
    //关闭摄像头
    stopNavigator() {
      this.thisVideo.srcObject.getTracks()[0].stop();
    },



        // 拍照
/*        photograph () {
            navigator.mediaDevices.getUserMedia({
                video: false
            }).then(success => {
                // 摄像头开启成功
                this.$refs['video'].srcObject = success
                // 实时拍照效果
                this.$refs['video'].play()
            }).catch(error => {
                console.error('摄像头开启失败，请检查摄像头是否可用！')
            })
            return

            let ctx = this.$refs['canvas'].getContext('2d')
            // 把当前视频帧内容渲染到canvas上
            ctx.drawImage(this.$refs['video'], 0, 0, 640, 480)
            // 转base64格式、图片格式转换、图片质量压缩
            let imgBase64 = this.$refs['canvas'].toDataURL('image/jpeg', 0.7)

            // 由字节转换为KB 判断大小
            let str = imgBase64.replace('data:image/jpeg;base64,', '')
            let strLength = str.length
            let fileLength = parseInt(strLength - (strLength / 8) * 2)
            // 图片尺寸  用于判断
            let size = (fileLength / 1024).toFixed(2)
            console.log(size)

            // 上传拍照信息  调用接口上传图片 .........

            // 保存到本地
            this.dialogCamera = false
            let ADOM = document.createElement('a')
            ADOM.href = this.headImgSrc
            ADOM.download = new Date().getTime() + '.jpeg'
            ADOM.click()
        },*/
        // 关闭摄像头
        closeCamera () {
            if (!this.$refs['video'].srcObject) {
                this.dialogCamera = false
                return
            }
            let stream = this.$refs['video'].srcObject
            let tracks = stream.getTracks()
            tracks.forEach(track => {
                track.stop()
            })
            this.$refs['video'].srcObject = null
        },

    handleSizeChange: function (val) {
      this.pagesize = val;
    },
    handleCurrentChange: function (currentPage) {
      this.currentPage = currentPage;
    },
    }
};
</script>

<style scoped>
.table {
  width: 100%;
  font-size: 14px;
}
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
