<template>
  <div class="container">
    <el-row :gutter="70">
      <!--<el-col :span="5">
          <p>dsd</p>
      </el-col>-->
      <el-col :span="15">
        <el-card shadow="hover" class="mgb20" style="height:max-content;">
          <el-button style="float: right; padding: 3px 0" type="text" @click="showEditDialog()">修改个人信息</el-button>

          <div class="user-info">
            <img src="../../assets/img/img.jpg" class="user-avator" alt />
            <div class="user-info-cont">
              <div class="user-info-name">{{tableData.nickname}}</div>

            </div>
          </div>
          <div class="user-info-list">
            邮  箱：
            <span>{{tableData.email }}</span>
          </div>
          <div class="user-info-list">
            昵  称：
            <span>{{tableData.nickname }}</span>
          </div>
          <div class="user-info-list">
            性  别：
            <span>{{ tableData.sex }}</span>
          </div>
          <div class="user-info-list">
            电  话：
            <span>{{ tableData.phone }}</span>
          </div>
<!--          <el-dialog title="修改我的信息" :visible.sync="dialogFormVisible">
            <el-form :model="editform">
              <el-form-item label="邮箱：" :label-width="formLabelWidth">
                <el-input v-model="tableData.email" clearable></el-input>
              </el-form-item>
              <el-form-item label="昵称：" :label-width="formLabelWidth">
                <el-input v-model="tableData.nickname" clearable></el-input>
              </el-form-item>
              <el-form-item label="描述：" :label-width="formLabelWidth">
                <el-input v-model="tableData.descri" clearable></el-input>
              </el-form-item>
              <el-form-item label="电话号：" :label-width="formLabelWidth">
                <el-input v-model="tableData.phone" clearable></el-input>
              </el-form-item>

            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="">取 消</el-button>
              <el-button type="primary" @click="">确 定</el-button>
            </div>
          </el-dialog>-->
        </el-card>
      </el-col>
      <el-col :span="9">
        <el-card shadow="hover" :body-style="{padding: '0px'}">
          <div class="grid-content grid-con-1">
            <i class="el-icon-lx-people grid-con-icon"></i>
            <div class="grid-cont-right">
              <div class="grid-num">{{ comment_num }}</div>
              <div>老人数量</div>
            </div>
          </div>
        </el-card>

        <el-card style="margin-top: 50px" shadow="hover" :body-style="{padding: '0px'}">
          <div  class="grid-content grid-con-2">
            <i class="el-icon-coordinate grid-con-icon"></i>
            <div class="grid-cont-right">
              <div class="grid-num">{{ comment_num }}</div>
              <div>工作人员数量</div>
            </div>
          </div>
        </el-card>

        <el-card style="margin-top: 50px" shadow="hover" :body-style="{padding: '0px'}">
          <div  class="grid-content grid-con-3">
            <i class="el-icon-mouse grid-con-icon"></i>
            <div class="grid-cont-right">
              <div class="grid-num">{{ comment_num }}</div>
              <div>义工数量</div>
            </div>
          </div>
        </el-card>
      </el-col>



      <!--<el-col :span="16">
        <el-row :gutter="20" class="mgb20">
          <el-col :span="12">
            <el-card shadow="hover" :body-style="{padding: '0px'}">
              <div class="grid-content grid-con-1">
                <i class="el-icon-lx-people grid-con-icon"></i>
                <div class="grid-cont-right">
                  <div class="grid-num">{{ this.comment_num }}</div>
                  <div>评价数量</div>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </el-col>-->

    </el-row>

    <el-dialog title="修改我的信息" :visible.sync="dialogFormVisible">
      <el-form :label-position="labelPosition" label-width="80px" :model="formLabelAlign">
        <el-form-item label="邮箱">
          <el-input v-model="editform.email" :disabled="true"></el-input>
        </el-form-item>
        <el-form-item label="姓名">
          <el-input v-model="editform.nickname"></el-input>
        </el-form-item>
        <el-form-item label="电话">
          <el-input v-model="editform.phone"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="editform.password" show-password></el-input>
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
    import axios from "axios";
    import Cookies from "js-cookie";

    export default {
        data() {
            return {
              dialogFormVisible: false,
              form:{
                id:Cookies.get('userid'),
              },

              tableData: {
                email:'',
                sex:'',
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
                password:'',
              },

              comment_num:2,


            }
        },
      created() {
        this.init()
      },
      methods:{
        init(){
          axios({
            methods: 'get',
            url: axios.defaults.baseURL + 'select_SysUser',
            params: this.form
          }).then((res) => {
            if (res.data.error === '0') {
              this.tableData.nickname=res.data.data.username,
                  this.tableData.sex=res.data.data.gender,
                  this.tableData.email=res.data.data.email,
                  this.tableData.phone=res.data.data.phone,
                  this.tableData.password=res.data.data.password
            }else{
              this.$message.error("error")
            }
          })
        },
        showEditDialog(){
          this.dialogFormVisible = true;
          this.editform.email=this.tableData.email
          this.editform.nickname=this.tableData.nickname
          this.editform.phone=this.tableData.phone
          this.editform.password=this.tableData.password
        },
        handleEdit(){
          this.ModifyData.email=this.editform.email
          this.ModifyData.nickname=this.editform.nickname
          this.ModifyData.phone=this.editform.phone
          this.ModifyData.password=this.editform.password
          axios({
            methods: 'get',
            url: axios.defaults.baseURL + 'update_SysUser',
            params: this.ModifyData
          }).then((res) => {
            if (res.data.error === '0') {
              this.$message.success("修改成功")
              this.dialogFormVisible=false
              this.init()
            }else{
              this.$message.error("error")
            }
          })
        },
        handleCancel(){
          this.dialogFormVisible=false;
        },
      }
    }
</script>

<style scoped>
.grid-content {
  display: flex;
  align-items: center;
  height: 100px;
}

.grid-cont-right {
  flex: 1;
  text-align: center;
  font-size: 14px;
  color: #999;
}

.grid-num {
  font-size: 30px;
  font-weight: bold;
}

.grid-con-icon {
  font-size: 50px;
  width: 100px;
  height: 100px;
  text-align: center;
  line-height: 100px;
  color: #fff;
}

.grid-con-1 .grid-con-icon {
  background: rgb(45, 140, 240);
}

.grid-con-1 .grid-num {
  color: rgb(45, 140, 240);
}

.grid-con-2 .grid-con-icon {
  background: rgb(100, 213, 114);
}

.grid-con-2 .grid-num {

  color: #f0c78a;
}

.grid-con-3 .grid-con-icon {
  background: rgb(242, 94, 67);
}

.grid-con-3 .grid-num {
  color: rgb(242, 94, 67);
}

.user-info {
  display: flex;
  align-items: center;
  padding-bottom: 20px;
  border-bottom: 2px solid #ccc;
  margin-bottom: 20px;
}

.user-avator {
  width: 120px;
  height: 120px;
  border-radius: 50%;
}

.user-info-cont {
  padding-left: 50px;
  flex: 1;
  font-size: 14px;
  color: #999;
}

.user-info-cont div:first-child {
  font-size: 30px;
  color: #222;
}

.user-info-list {
  font-size: 14px;
  color: #999;
  line-height: 25px;
}

.user-info-list span {
  margin-left: 70px;
}

.mgb20 {
  margin-bottom: 20px;
}
</style>