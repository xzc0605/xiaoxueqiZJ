<template>
  <div class="layout">
    <!-- <div class="crumbs">
       <el-breadcrumb separator="/">
         <el-breadcrumb-item>
           <i class="el-icon-pie-chart"></i> 监控信息
         </el-breadcrumb-item>
       </el-breadcrumb>
     </div>-->


    <div>
      <!--      <el-row :gutter="70">
              &lt;!&ndash;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;房间-&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&ndash;&gt;
            <el-col :span="6">
                <div class="crumbs">
                  <el-breadcrumb separator="/">
                    <el-breadcrumb-item>
                      <i class="el-icon-pie-chart"></i> 房间
                    </el-breadcrumb-item>
                  </el-breadcrumb>
                </div>

                <div :visible.sync="fangjianShow">
                  <video ref="player" width="100%" height="450"></video>&lt;!&ndash;摄像头位置！！！！！！！！！！！！！！&ndash;&gt;
                </div>
                <div>
                  <el-button type="success" @click="playVideo(fangjian)">开始</el-button>
                  <el-button type="primary" @click="close()">关闭</el-button>
                </div>
              </el-col>
           <&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;桌子-&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&ndash;&gt;
              <el-col :span="6">
                <div class="crumbs">
                <el-breadcrumb separator="/">
                  <el-breadcrumb-item>
                    <i class="el-icon-pie-chart"></i> 桌子
                  </el-breadcrumb-item>
                </el-breadcrumb>
                </div>

                <div :visible.sync="zhuoziShow">
                  <video ref="player" width="100%" height="450"></video>&lt;!&ndash;//摄像头位置！！！！！！！！！！！！！！&ndash;&gt;
                </div>
                <div>
                  <el-button type="success" @click="playVideo(zhuozi)">开始</el-button>
                  <el-button type="primary" @click="close()">关闭</el-button>
                </div>
              </el-col>&ndash;&gt;
              &lt;!&ndash;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;走廊-&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&ndash;&gt;
              <el-col :span="6">
                <div class="crumbs">
                  <el-breadcrumb separator="/">
                    <el-breadcrumb-item>
                      <i class="el-icon-pie-chart"></i> 走廊
                    </el-breadcrumb-item>
                  </el-breadcrumb>
                </div>

                <div :visible.sync="zoulangShow">
                  <video ref="player1" width="100%" height="450"></video>&lt;!&ndash;//摄像头位置！！！！！！！！！！！！！！&ndash;&gt;
                </div>
                <div>
                  <el-button type="success" @click="playVideo1(zoulang)">开始</el-button>
                  <el-button type="primary" @click="close()">关闭</el-button>
                </div>
              </el-col>
            &lt;!&ndash;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;院子-&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&ndash;&gt;
              <el-col :span="6">
                <div class="crumbs">
                  <el-breadcrumb separator="/">
                    <el-breadcrumb-item>
                      <i class="el-icon-pie-chart"></i> 院子
                    </el-breadcrumb-item>
                  </el-breadcrumb>
                </div>
                <div :visible.sync="yuanziShow">
                  <video ref="player2" width="100%" height="450"></video>&lt;!&ndash;//摄像头位置！！！！！！！！！！！！！！&ndash;&gt;
                </div>
                <div>
                  <el-button type="success" @click="playVideo2(yuanzi)">开始</el-button>
                  <el-button type="primary" @click="close()">关闭</el-button>
                </div>
              </el-col>
            </el-row>-->
      <el-table
          :data="cameras"
          style="width: 100%">
        <el-table-column
            prop="id"
            label="名称"
            width="180">
        </el-table-column>
        <el-table-column
            prop="name"
            label="描述"
            width="180">
        </el-table-column>
        <el-table-column
            prop="desc"
            label="场景">
        </el-table-column>
        <el-table-column label="操作" width="180" align="center">
          <template slot-scope="scope">
            <el-button type="primary" size="small" @click="showVideo(scope.row)">查看</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <div class="crumbs" style="margin-top: 40px">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item>
          <i class="el-icon-pie-chart"></i> 事件信息
        </el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div class="container">

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
        <el-table-column prop="event_desc" label="描述" align="center"></el-table-column>
        <el-table-column prop="event_location" label="地点" align="center"></el-table-column>
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




    <el-dialog title="摄像头1" :visible.sync="fangjianShow">
      <video ref="player1" width="100%" height="450"></video>


    </el-dialog>

    <el-dialog title="摄像头2" :visible.sync="zhuoziShow">
      <video ref="player2" width="100%" height="450"></video>


    </el-dialog>

    <el-dialog title="摄像头3" :visible.sync="zoulangShow">
      <video ref="player3" width="100%" height="450"></video>


    </el-dialog>

    <el-dialog title="摄像头4" :visible.sync="yuanziShow">
      <video ref="player4" width="100%" height="450"></video>


    </el-dialog>

  </div>
</template>

<script>
/*import VideoModal from './VideoModal';*/
import flvjs from 'flv.js'
import axios from "axios";
export default {
  components: {

  },
  data () {
    return {
      fangjian:1,
      zhuozi:2,
      zoulang:3,
      yuanzi:4,
      //四个场景按钮判断
      fangjianShow:false,
      zhuoziShow:false,
      zoulangShow:false,
      yuanziShow:false,

      eventData:[],
      totalnums:0,
      pagesize: 10,
      currentPage: 1,

      rtspUrl1: 'rtsp://admin:admin@192.168.43.41:8554/live',
      rtspUrl2: 'rtsp://admin:admin@192.168.43.1:8554/live',
      rtspUrl3: 'rtsp://admin:admin@192.168.43.33:8554/live',
      rtspUrl4: 'rtsp://admin:admin@192.168.43.159:8554/live',
      cameras: [
        {
          id: 1,
          name: '摄像头1',
          desc: '房间'
        },{
          id: 2,
          name: '摄像头2',
          desc: '桌子'
        },{
          id: 3,
          name: '摄像头3',
          desc: '走廊'
        },{
          id: 4,
          name: '摄像头4',
          desc: '院子'
        }

      ],
      modalShow: false,
      modalData: null,
      yes:true
    }
  },
  /*  computed:{
      streamId () {
        return this.modalData ? this.modalData.id : 0

      }
    },*/
  /*  watch: {
      show () {
        if(this.yes) {
          this.playVideo()

        } else {
          this.destroyVideo()
        }
      }
    },*/
  mounted() {
     /*this.getEvent()*/
    this.timer = setInterval(() => {
      setTimeout(this.getEvent, 0)
    }, 2000)
  },
  methods: {
    //获取信息
    getEvent(){
      axios({
        methods: 'get',
        url: axios.defaults.baseURL + 'delivery_Event',
      }).then((res) => {
        if (res.data.error === '0') {
          this.eventData=res.data.data
          this.totalnums=res.data.event_num
        }else{
          /*this.$message.error(res.data.messages)*/
        }
      })

    },
    //分页操作
    handleSizeChange: function (val) {
      this.pagesize = val;
    },
    handleCurrentChange: function (currentPage) {
      this.currentPage = currentPage;
    },

    showVideo(row) {

      if(row.id===1){
        this.fangjianShow=true
        this.playVideo1(1)

      }else if(row.id===2){
        this.zhuoziShow=true
        this.playVideo2(2)

      }else if(row.id===3) {
        this.zoulangShow=true
        this.playVideo3(3)

      }else if(row.id===4){
        this.yuanziShow=true
        this.playVideo4(4)
      }
    },
    close(){
      this.destroyVideo()
       this.fangjianShow=false,
       this.zhuoziShow=false,
       this.zoulangShow=false,
       this.yuanziShow=false
    },
    destroyVideo () {
      if (this.player) {
        this.player.pause()
        this.player.unload()
        this.player.detachMediaElement()
        this.player.destroy()
        this.player = null
        document.removeEventListener('visibilitychange', this.justifyPlayTime)
      }
    },

    playVideo1 (index) {

      if (flvjs.isSupported()) {
        let video = this.$refs.player1

        if (video) {
          if (this.player) {
            this.destroyVideo()
          }
          this.player = flvjs.createPlayer({
            type: 'flv',
            isLive: true,
            hasAudio: false,
            enableStashBuffer: false, // Enable IO stash buffer. Set to false if you need realtime (minimal latency) for live stream playback, but may stalled if there's network jittering.
            url: `ws://localhost:8888/rtsp/${index}/?url=${this.rtspUrl1}`
          })
          this.player.attachMediaElement(video)
          try {
            this.player.load()
            this.player.play()

            console.log('play')
          } catch (error) {
            console.log(error)
            this.$message.error("播放错误")
          }

          if (document.hidden !== undefined) {
            document.addEventListener('visibilitychange', this.justifyPlayTime)
          }
        }
      }
    },
    playVideo2 (index) {

      if (flvjs.isSupported()) {
        let video = this.$refs.player2

        if (video) {
          if (this.player) {
            this.destroyVideo()
          }
          this.player = flvjs.createPlayer({
            type: 'flv',
            isLive: true,
            hasAudio: false,
            enableStashBuffer: false, // Enable IO stash buffer. Set to false if you need realtime (minimal latency) for live stream playback, but may stalled if there's network jittering.
            url: `ws://localhost:8888/rtsp/${index}/?url=${this.rtspUrl2}`
          })
          this.player.attachMediaElement(video)
          try {
            this.player.load()
            this.player.play()

            console.log('play')
          } catch (error) {
            console.log(error)
            this.$message.error("播放错误")
          }

          if (document.hidden !== undefined) {
            document.addEventListener('visibilitychange', this.justifyPlayTime)
          }
        }
      }
    },
    playVideo3 (index) {

      if (flvjs.isSupported()) {
        let video = this.$refs.player3

        if (video) {
          if (this.player) {
            this.destroyVideo()
          }
          this.player = flvjs.createPlayer({
            type: 'flv',
            isLive: true,
            hasAudio: false,
            enableStashBuffer: false, // Enable IO stash buffer. Set to false if you need realtime (minimal latency) for live stream playback, but may stalled if there's network jittering.
            url: `ws://localhost:8888/rtsp/${index}/?url=${this.rtspUrl3}`
          })
          this.player.attachMediaElement(video)
          try {
            this.player.load()
            this.player.play()

            console.log('play')
          } catch (error) {
            console.log(error)
            this.$message.error("播放错误")
          }

          if (document.hidden !== undefined) {
            document.addEventListener('visibilitychange', this.justifyPlayTime)
          }
        }
      }
    },
    playVideo4 (index) {

      if (flvjs.isSupported()) {
        let video = this.$refs.player4

        if (video) {
          if (this.player) {
            this.destroyVideo()
          }
          this.player = flvjs.createPlayer({
            type: 'flv',
            isLive: true,
            hasAudio: false,
            enableStashBuffer: false, // Enable IO stash buffer. Set to false if you need realtime (minimal latency) for live stream playback, but may stalled if there's network jittering.
            url: `ws://localhost:8888/rtsp/${index}/?url=${this.rtspUrl4}`
          })
          this.player.attachMediaElement(video)
          try {
            this.player.load()
            this.player.play()

            console.log('play')
          } catch (error) {
            console.log(error)
            this.$message.error("播放错误")
          }

          if (document.hidden !== undefined) {
            document.addEventListener('visibilitychange', this.justifyPlayTime)
          }
        }
      }
    },
    justifyPlayTime () {
      console.log(document.hidden)
      if (!document.hidden) {
        // 显示
        let video = this.$refs.player
        let buffered = video.buffered
        if (buffered.length > 0) {
          let end = buffered.end(0)
          if (end - video.currentTime > 0.15) {
            video.currentTime = end - 0.1
          }
        }
      } else {
        // 隐藏
      }
    },
  }
}
</script>

<style >
.container {
  padding: 30px;
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 5px;
}
.layout{
  position: relative;
  overflow: hidden;
  padding: 20px;
}
</style>
