<template>
    <div class="header">
        <!-- 折叠按钮 -->
        <div class="collapse-btn" @click="collapseChage">
            <i v-if="!collapse" class="el-icon-s-fold"></i>
            <i v-else class="el-icon-s-unfold"></i>
        </div>
        <div class="logo">OldCare系统</div>
        <div class="header-right">
            <div class="header-user-con">
                <!-- 全屏显示 -->
                <div class="btn-fullscreen" @click="handleFullScreen">
                    <el-tooltip effect="dark" :content="fullscreen?`取消全屏`:`全屏`" placement="bottom">
                        <i class="el-icon-rank"></i>
                    </el-tooltip>
                </div>
                <!-- 消息中心 -->
                <div class="btn-bell">
                    <el-tooltip
                        effect="dark"
                        :content="message?`有${message}条未读消息`:`消息中心`"
                        placement="bottom"
                    >
                        <router-link to="/tabs">
                            <i class="el-icon-bell"></i>
                        </router-link>
                    </el-tooltip>
                    <span class="btn-bell-badge" v-if="message"></span>
                </div>
                <!-- 用户头像 -->
                <div class="user-avator">
                    <img src="../../assets/img/img.jpg" />
                </div>
                <!-- 用户名下拉菜单 -->
                <el-dropdown class="user-name" trigger="click" @command="handleCommand">
                    <span class="el-dropdown-link">
                        <i class="el-icon-caret-bottom"></i>
                    </span>
                    <el-dropdown-menu slot="dropdown">
                        <el-dropdown-item command="infomation">我的信息</el-dropdown-item>
                        <el-dropdown-item divided command="loginout">退出登录</el-dropdown-item>
                    </el-dropdown-menu>
                </el-dropdown>
            </div>
        </div>


      <el-dialog title="修改我的信息" :visible.sync="dialogFormVisible">
        <el-form :label-position="labelPosition" label-width="80px" :model="formLabelAlign">
                <el-form-item label="邮箱">
                  <el-input v-model="tableData.email" :disabled="true"></el-input>
                </el-form-item>
                <el-form-item label="姓名">
                  <el-input v-model="tableData.nickname"></el-input>
                </el-form-item>
                <el-form-item label="电话">
                  <el-input v-model="tableData.phone"></el-input>
                </el-form-item>
                <el-form-item label="密码">
                  <el-input v-model="tableData.password" show-password></el-input>
                </el-form-item>
        </el-form>

        <div slot="footer" class="dialog-footer">
          <el-button @click="handleCancel()">取 消</el-button>
          <el-button type="primary" @click="handleEdit()">确 定</el-button>
        </div>
      </el-dialog>
    </div>
</template>
<script>
import bus from '../common/bus';
import Cookies from 'js-cookie'
import axios from 'axios'
export default {
    data() {
        return {
            dialogFormVisible: false,
            collapse: false,
            fullscreen: false,
            name: 'linxin',
            message: 2,


            form:{
              id:Cookies.get('userid'),
            },

            tableData: {
              email:'',
              nickname:'',
              phone:'',
              password:''
            },
          ModifyData:{
            id:Cookies.get('userid'),
            email:'',
            nickname:'',
            phone:'',
            password:''
          },
            editform:{
              nickname:'',
              email:'',
              phone:'',
            }
        };
    },
 // created() {
 //      this.init()
 // },

  methods: {

        // 用户名下拉菜单选择事件
        handleCommand(command) {
            if (command == 'loginout') {
                localStorage.removeItem('ms_username');
                this.$router.push('/login');
            }
            if(command == 'infomation'){
                /*this.dialogFormVisible=true;*/
               this.$router.push('/icon');
            }
        },
        // 侧边栏折叠
        collapseChage() {
            this.collapse = !this.collapse;
            bus.$emit('collapse', this.collapse);
        },
        // 全屏事件
        handleFullScreen() {
            let element = document.documentElement;
            if (this.fullscreen) {
                if (document.exitFullscreen) {
                    document.exitFullscreen();
                } else if (document.webkitCancelFullScreen) {
                    document.webkitCancelFullScreen();
                } else if (document.mozCancelFullScreen) {
                    document.mozCancelFullScreen();
                } else if (document.msExitFullscreen) {
                    document.msExitFullscreen();
                }
            } else {
                if (element.requestFullscreen) {
                    element.requestFullscreen();
                } else if (element.webkitRequestFullScreen) {
                    element.webkitRequestFullScreen();
                } else if (element.mozRequestFullScreen) {
                    element.mozRequestFullScreen();
                } else if (element.msRequestFullscreen) {
                    // IE11
                    element.msRequestFullscreen();
                }
            }
            this.fullscreen = !this.fullscreen;
        },
      handleCancel(){
          this.dialogFormVisible=false;
      },
      handleEdit(){

        this.ModifyData.email=this.tableData.email
        this.ModifyData.nickname=this.tableData.nickname
        this.ModifyData.phone=this.tableData.phone
        this.ModifyData.password=this.tableData.password
        axios({
          methods: 'get',
          url: axios.defaults.baseURL + 'update_SysUser',
          params: this.ModifyData
        }).then((res) => {
          if (res.data.error === '0') {
            this.$message.success("修改成功")
            this.dialogFormVisible=false
          }else{
            this.$message.error("error")
          }
        })
      }
    },
    mounted() {
        if (document.body.clientWidth < 1500) {
            this.collapseChage();
        }
    }
};
</script>
<style scoped>
.header {
    position: relative;
    box-sizing: border-box;
    width: 100%;
    height: 70px;
    font-size: 22px;
    color: #fff;
}
.collapse-btn {
    float: left;
    padding: 0 21px;
    cursor: pointer;
    line-height: 70px;
}
.header .logo {
    float: left;
    width: 250px;
    line-height: 70px;
}
.header-right {
    float: right;
    padding-right: 50px;
}
.header-user-con {
    display: flex;
    height: 70px;
    align-items: center;
}
.btn-fullscreen {
    transform: rotate(45deg);
    margin-right: 5px;
    font-size: 24px;
}
.btn-bell,
.btn-fullscreen {
    position: relative;
    width: 30px;
    height: 30px;
    text-align: center;
    border-radius: 15px;
    cursor: pointer;
}
.btn-bell-badge {
    position: absolute;
    right: 0;
    top: -2px;
    width: 8px;
    height: 8px;
    border-radius: 4px;
    background: #f56c6c;
    color: #fff;
}
.btn-bell .el-icon-bell {
    color: #fff;
}
.user-name {
    margin-left: 10px;
}
.user-avator {
    margin-left: 20px;
}
.user-avator img {
    display: block;
    width: 40px;
    height: 40px;
    border-radius: 50%;
}
.el-dropdown-link {
    color: #fff;
    cursor: pointer;
}
.el-dropdown-menu__item {
    text-align: center;
}
</style>
