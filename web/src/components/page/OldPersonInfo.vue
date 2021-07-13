<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>
                    <i class="el-icon-lx-cascades"></i> 老人信息
                </el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="handle-box">
                <el-button
                    type="primary"
                    icon="el-icon-delete"
                    class="handle-del mr10"
                    @click="delAllSelection"
                >批量删除</el-button>
                <el-select v-model="query.field" placeholder="属性" class="handle-select mr10">
                    <el-option key="1" label="ID" value="id"></el-option>
                    <el-option key="2" label="姓名" value="username"></el-option>
                   <el-option key="3" label="性别" value="gender"></el-option>
                    <el-option key="4" label="出生日期" value="birthday"></el-option>
                    <el-option key="5" label="身份证号" value="id_card"></el-option>
                    <el-option key="6" label="电话号" value="phone"></el-option>
                    <el-option key="7" label="健康状态" value="health_state"></el-option>
                </el-select>

                <el-input v-model="query.key" placeholder="搜索内容" class="handle-input mr10"></el-input>
                <el-button type="primary" icon="el-icon-search" @click="handleSearch">搜索</el-button>
                <el-button style="float: right" type="primary" icon="el-icon-plus" @click="addOld()">添加老人</el-button>
            </div>
          <el-table
              :data="tableData"
              border
              class="table"
              ref="multipleTable"
              header-cell-class-name="table-header"
              @selection-change="handleSelectionChange"
          >
            <el-table-column type="selection" width="55" align="center"></el-table-column>
            <el-table-column prop="id" label="ID" width="55" align="center"></el-table-column>
            <el-table-column prop="username" label="姓名" align="center"></el-table-column>
            <el-table-column prop="gender" label="性别" align="center"></el-table-column>

            <el-table-column prop="birthday" label="出生日期" align="center"></el-table-column>

            <el-table-column prop="id_card" label="身份证号" align="center"></el-table-column>
            <el-table-column prop="phone" label="电话号" align="center"></el-table-column>
            <!--<el-table-column prop="room_number" label="房间号" align="center"></el-table-column>-->
            <el-table-column prop="health_state" label="健康状态" align="center"></el-table-column>
            <el-table-column label="操作" width="180" align="center">
              <template slot-scope="scope">
                <el-button
                    type="text"
                    icon="el-icon-edit"
                    @click="handleEdit(scope.row)"
                >编辑</el-button>
                <el-button
                    type="text"
                    icon="el-icon-delete"
                    class="red"
                    @click="handleDelete(scope.row)"
                >删除</el-button>
              </template>
            </el-table-column>
          </el-table>
            <div class="pagination">
                <el-pagination
                    background
                    layout="total, prev, pager, next"
                    :current-page="query.pageIndex"
                    :page-size="query.pageSize"
                    :total="pageTotal"
                    @current-change="handlePageChange"
                ></el-pagination>
            </div>
        </div>

        <!-- 编辑弹出框 -->
        <el-dialog title="修改老人信息" :visible.sync="editVisible" width="1000px">
         <!--老人信息添加修改框-->
          <div style="display: flex">
            <div style="width: 50%;margin-right: 20px">
              <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>姓名 ：</p></div>
                <div class="titleinput row-right">
                  <el-input  placeholder="姓名" v-model="olderform.username"
                             autosize ></el-input>
                </div>
              </div>
              <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>性别 ：</p></div>
                <div class="titleinput row-right">
                  <el-select placeholder="性别" v-model="olderform.gender" style="width: 100%">
                    <el-option name="男" value="男"></el-option>
                    <el-option name="女" value="女"></el-option>
                  </el-select>
                </div>

              </div>
              <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>电话 ：</p></div>
                <div class="titleinput row-right">
                  <el-input  placeholder="电话" v-model="olderform.phone"
                             autosize ></el-input>
                </div>
              </div>
              <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>身份证号 ：</p></div>
                <div class="titleinput row-right">
                  <el-input  placeholder="身份证号码" v-model="olderform.id_card"
                             autosize ></el-input>
                </div>
              </div>
              <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>出生日期 ：</p></div>
                <div class="titleinput row-right">
                  <el-date-picker
                      style="width: 100%"
                      value-format="yyyy-MM-dd"
                      placeholder="出生日期(必填)"
                      v-model="olderform.birthday"></el-date-picker>
                </div>
              </div>
              <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>	入院日期 ：</p></div>
                <div class="titleinput row-right">
                  <el-date-picker
                      style="width: 100%"
                      value-format="yyyy-MM-dd"
                      placeholder="进入养老院日期(必填)"
                      v-model="olderform.checkin_date"></el-date-picker>
                </div>
              </div>
              <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>离院日期 ：</p></div>
                <div class="titleinput row-right">
                  <el-date-picker
                      style="width: 100%"
                      value-format="yyyy-MM-dd"
                      placeholder="离开养老院日期(必填)"
                      v-model="olderform.checkout_date"></el-date-picker>
                </div>
              </div>
              <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>图像目录 ：</p></div>
                <div class="titleinput row-right">
                  <el-input  placeholder="图像目录" v-model="olderform.imgset_dir"
                             autosize ></el-input>
                </div>
              </div>
              <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>头像：</p></div>
                <div class="titleinput row-right">
                  <el-input  placeholder="头像" v-model="olderform.profile_photo"
                             autosize ></el-input>
                </div>
              </div>
              <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>健康状况：</p></div>
                <div class="titleinput row-right">
                  <el-input  placeholder="健康状况" v-model="olderform.health_state"
                             autosize ></el-input>
                </div>
              </div>
            </div>
            <div style="width: 50%">
              <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 30%;text-align: right"><p>房间号 ：</p></div>
                <div class="titleinput row-right">
                  <el-input  placeholder="房间号" v-model="olderform.room_number"
                             autosize ></el-input>
                </div>
              </div>
              <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 30%;text-align: right"><p>第一监护人姓名 ：</p></div>
                <div class="titleinput row-right">
                  <el-input  placeholder="第一监护人姓名" v-model="olderform.firstguardian_name"
                             autosize ></el-input>
                </div>
              </div>
              <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 30%;text-align: right"><p>与第一监护人关系 ：</p></div>
                <div class="titleinput row-right">
                  <el-input  placeholder="与第一监护人关系" v-model="olderform.firstguardian_relationship"
                             autosize ></el-input>
                </div>
              </div>
              <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 30%;text-align: right"><p>第一监护人电话 ：</p></div>
                <div class="titleinput row-right">
                  <el-input  placeholder="第一监护人电话" v-model="olderform.firstguardian_phone"
                             autosize ></el-input>
                </div>
              </div>
              <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 30%;text-align: right"><p>第一监护人微信 ：</p></div>
                <div class="titleinput row-right">
                  <el-input  placeholder="第一监护人微信" v-model="olderform.firstguardian_wechat"
                             autosize ></el-input>
                </div>
              </div>
              <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 30%;text-align: right"><p>	第二监护人姓名 ：</p></div>
                <div class="titleinput row-right">
                  <el-input  placeholder="第二监护人姓名" v-model="olderform.secondguardian_name"
                             autosize ></el-input>
                </div>
              </div>
              <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 30%;text-align: right"><p>与第二监护人关系 ：</p></div>
                <div class="titleinput row-right">
                  <el-input  placeholder="与第二监护人关系"  v-model="olderform.secondguardian_relationship"
                             autosize ></el-input>
                </div>
              </div>
              <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 30%;text-align: right"><p>第二监护人电话：</p></div>
                <div class="titleinput row-right">
                  <el-input  placeholder="第二监护人电话" v-model="olderform.secondguardian_phone"
                             autosize ></el-input>
                </div>
              </div>
              <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 30%;text-align: right"><p>第二监护人微信：</p></div>
                <div class="titleinput row-right">
                  <el-input  placeholder="第二监护人微信" v-model="olderform.secondguardian_wechat"
                             autosize ></el-input>
                </div>
              </div>
            </div>
          </div>






            <span slot="footer" class="dialog-footer">
                <el-button @click="editVisible = false">取 消</el-button>
                <el-button v-if="isShowEdit" type="primary" @click="saveEdit()">确 定</el-button>
                <el-button v-if="isShowAdd" type="primary" @click="saveAdd()">确 定</el-button><!--设置成了条件显示的按钮-->
            </span>
        </el-dialog>
    </div>
</template>

<script>
import axios from 'axios'

import addPeople from "@/components/common/addPeople";
export default {
    name: 'OldPersonInfo',
    components:{addPeople},
    data() {
        return {
          query: {
           /* sex:'',
            health:'',
            pageIndex: 1,
            pageSize: 10*/
            form:'oldperson_info',
            field:'',
            key:'',
          },
          tableData: [],
          multipleSelection: [],
          isShowEdit:false,
          isShowAdd:false,
          editVisible: false,
          addVisible: false,
          pageTotal: 0,
          form: {},
          olderform: {
            id: '',
            username: '',
            gender: '',
            phone: '',
            id_card: '',
            birthday: '',
            checkin_date: '',
            checkout_date: '',
            imgset_dir: '',
            profile_photo: '',
            room_number: '',
            firstguardian_name: '',
            firstguardian_relationship: '',
            firstguardian_phone: '',
            firstguardian_wechat: '',
            secondguardian_name: '',
            secondguardian_relationship: '',
            secondguardian_phone: '',
            secondguardian_wechat: '',
            health_state: '',
        }
        };
    },
  //从created改为了mounted函数
    mounted() {
        // this.getData();
        this.init()
    },
    methods: {
      //读取老人信息
      async init(){
        await axios({
          methods: 'get',
          url: axios.defaults.baseURL + 'select_OldPerson',
          params: this.form
        }).then((res) => {
          if (res.data.error === '0') {
                this.tableData=res.data.data
          }else{
            this.$message.error(res.data.message)
          }
        })
      },

        // 触发搜索按钮
        handleSearch() {
          /*  this.$set(this.query, 'pageIndex', 1);
            this.getData();*/
          if(this.query.field ===''){
                alert("搜索条件不能为空")
                this.query.key=''//清空搜索值
                this.query.field=''
          }else{
            if(this.query.key===''){
              this.query.field=''
            }else{
               axios({
           methods: 'get',
           url: axios.defaults.baseURL + 'select_Information',
           params: this.query
         }).then((res) => {
           if (res.data.error === '0') {
             if(res.data.state ==='1'){
               this.query.key=''//清空搜索值
               this.query.field=''
             }else{
               this.$message.success(res.data.messages)
               this.tableData=res.data.data
               this.query.key=''//清空搜索值
               this.query.field=''
             }
           }else{
             this.$message.error(res.data.messages)
           }
         })
            }
          }

        },
        // 删除操作
        handleDelete(index) {
            // 二次确认删除
            this.$confirm('确定要删除吗？', '提示', {
                type: 'warning'
            })
                .then(() => {
                  /*console.log(1111111111111111,index)*/
                  axios({
                    methods: 'get',
                    url: axios.defaults.baseURL + 'delete_OldPerson',
                    params: index
                  }).then((res) => {
                    if (res.data.error === '0') {
                      this.$message.success(res.data.messages)
                      this.init()
                    }else{
                      this.$message.error(res.data.messages)
                    }
                  })
                })
                .catch(() => {});

        },

        // 多选操作
        handleSelectionChange(val) {
            this.multipleSelection = val;

        },

      //批量删除
        delAllSelection()   {
            const length = this.multipleSelection.length;

            for (let i = 0; i < length; i++) {
              axios({
                methods: 'get',
                url: axios.defaults.baseURL + 'delete_OldPerson',
                params: this.multipleSelection[i]
              }).then((res) => {

                if (res.data.error === '0') {
                  this.$message.success(res.data.messages)
                  this.multipleSelection = [];
                  this.init()
                }else{
                  this.$message.error(res.data.messages)
                }
              })
            }

        },

        // 编辑操作
        handleEdit(info) {
          this.editVisible=true
          this.isShowAdd=false
          this.isShowEdit=true
          axios({
            methods: 'get',
            url: axios.defaults.baseURL + 'update_Information',
            params: {"id":info.id}
          }).then((res) => {
            if (res.data.error === '0') {

              this.olderform=res.data.data
            }else{
              this.$message.error(res.data.messages)
            }
          })

        },

        // 保存编辑
        saveEdit() {
            this.editVisible = false;
            let id =this.olderform.id
            let update=this.olderform
          axios({
            methods: 'get',
            url: axios.defaults.baseURL + 'update_OldPerson',
            params: {id,update}
          }).then((res) => {
            if (res.data.error === '0') {
              this.$message.success("修改信息成功")
              this.olderform={}//将olderform的值清空

              this.init()
            } else {
              this.$message.error(res.data.messages)
            }
          })

        },

        // 分页导航
        handlePageChange(val) {
            this.$set(this.query, 'pageIndex', val);
            this.getData();
        },
      //添加老人
      addOld(){
        this.editVisible = true
        this.isShowAdd = true
        this.isShowEdit = false

        this.olderform={}
      },

      //保存添加老人结果
      saveAdd() {
        this.editVisible =false
        axios({
          methods: 'get',
          url: axios.defaults.baseURL + 'insert_OldPerson',
          params: this.olderform
        }).then((res) => {
          if (res.data.error === '0') {
            this.$message.success("修改信息成功")
            this.init()
          } else {
            this.$message.error(res.data.messages)
          }
        })

      }
    }
};
</script>

<style scoped>
.display-row {
  display: -webkit-flex; /* Safari */
  -webkit-justify-content: flex-start; /* Safari 6.1+ */
  display: flex;
  justify-content: flex-start;
  width: 100%;
}
.handle-box {
    margin-bottom: 20px;
}

.handle-select {
    width: 120px;
}

.handle-input {
    width: 300px;
    display: inline-block;
}
.table {
    width: 100%;
    font-size: 14px;
}
.red {
    color: #ff0000;
}
.mr10 {
    margin-right: 10px;
}
.table-td-thumb {
    display: block;
    margin: auto;
    width: 40px;
    height: 40px;
}
</style>
