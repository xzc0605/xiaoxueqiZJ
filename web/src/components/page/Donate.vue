<template>
  <div class="video">
    <div class="con">{{video}}</div>
    <div class="video-wrap">
      <video-player class="vjs-custom-skin" :options="playerOptions"></video-player>
    </div>
  </div>
</template>

<script>
// require styles
import 'video.js/dist/video-js.css'
import 'vue-video-player/src/custom-theme.css'
// video-player
import  { videoPlayer }  from 'vue-video-player'
// rtmp video-flash
import 'videojs-flash'
export default {
  name: 'Donate',
  data () {
    return {
      video: 'hello video',
      playerOptions: {
        height: '260',
        language: 'en',
        playbackRates: [0.5, 1.0, 1.5, 2.0],
        sources: [{
          type: "rtmp/mp4",
         /* src: "rtmp://58.200.131.2:1935/livetv/hunantv"*/
          // src:"rtmp://live.hkstv.hk.lxdns.com/live/hks"
          src:'rtmp://localhost:8080/stream'
        }],
        techOrder: ['flash'],
        autoplay: false,
        controls: true,
        poster: "../../assets/images/video2.jpg",
        notSupportedMessage: '不支持的视频格式'
      }
    }
  },
  components: {
    videoPlayer
  },
  mounted() {},
  methods: {}
}
</script>

<style>
.video {
  width: 100%;
  padding: 20px;
  box-sizing: border-box;
}
  .con {
    width: 100%;
    height: 30px;
    line-height: 30px;
  }
  .video-wrap {
    width: 500px;
    height: 300px;
  }

</style>
