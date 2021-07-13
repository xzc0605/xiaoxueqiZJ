<template>
    <div class="">
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-lx-copy"></i> 义工信息</el-breadcrumb-item>
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
              <el-option key="7" label="登入日期" value="checkin_date"></el-option>
              <el-option key="8" label="登出日期" value="checkout_date"></el-option>
            </el-select>

            <el-input v-model="query.key" placeholder="搜索内容" class="handle-input mr10"></el-input>
            <el-button type="primary" icon="el-icon-search" @click="handleSearch()">搜索</el-button>
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
                <el-table-column prop="username" label="用户名"></el-table-column>
                <el-table-column prop="gender" label="性别"></el-table-column>
                <el-table-column prop="id_card" label="身份证"></el-table-column>
                <el-table-column prop="phone" label="联系方式"></el-table-column>
                <el-table-column prop="birthday" label="出生日期"></el-table-column>
                <el-table-column prop="checkin_date" label="登入日期"></el-table-column>
                <el-table-column prop="checkout_date" label="登出日期"></el-table-column>
                <el-table-column label="操作" width="180" align="center">
                    <template slot-scope="scope">
                        <el-button
                                type="text"
                                icon="el-icon-edit"
                                @click="handleEdit(scope.$index, scope.row)"
                        >编辑</el-button>
                        <el-button
                                type="text"
                                icon="el-icon-delete"
                                class="red"
                                @click="deleteNewWorker(scope.row)"
                        >删除</el-button>
                    </template>
                </el-table-column>
            </el-table>
            <div style="margin-bottom: 40px;margin-top: 10px;">
                <el-pagination
                        @size-change="handleSizeChange"
                        @current-change="handlePageChange"
                        :page-sizes="[10, 20, 50, 100, 500, 1000]"
                        :current-page="listForm1.page"
                        :page-size="listForm1.size"
                        :total="listForm1.total"
                        layout="total, sizes, prev, pager, next, jumper"
                        style="float: left;padding: 0px"
                ></el-pagination>
                <div style="float: right"><el-button type="primary" size="mini" @click="()=>{this.addVisible=true;
                                                                                    this.isEdit=false;
                                                                                    }">添加人员</el-button></div>
            </div>
        </div>
        <el-dialog
                :title="'添加人员'"
                :visible.sync="addVisible"
                width="500px"
                @opened="handleEditDialog"
                cente
                :modal-append-to-body="false">
            <div>
                <!--                缺啥到时候补什么-->
                <addPeople :people-type="1" ref="addPeople"></addPeople>
            </div>
            <span slot="footer" class="dialog-footer">
                <el-button @click="updateNewVolunteer()" type="primary">确 定</el-button>
                <el-button @click="addVisible = false">取 消</el-button>
              </span>
        </el-dialog>
    </div>
</template>

<script>
    import addPeople from "../common/addPeople";
    import axios from 'axios';
    import API from "../../api";
    export default {
        name: 'tabs',
        components:{addPeople},
        data() {
            return {
              query: {
                form:'volunteer_info',
                field:'',
                key:'',
              },

                message: 'first',
                showHeader: false,
                listForm1:{},
                addVisible:false,
                isEdit:true,
                tableIndex:'',
                tableData: [
                ],
            }
        },
        mounted() {
         this.getTableData()
        },
        methods: {
            getTableData(){
                axios.get(axios.defaults.baseURL+'select_Volunteer',{params:{

                    }}).then(res=>{
                    // if(res.data.error=='1'){
                    //     this.$message.error(res.data.messages)
                    //     return
                    // }
                    this.tableData=res.data.data
                })
            },
            updateNewVolunteer(){
                let data=this.$refs.addPeople.VolunteerForm
                // insert_Employee
                // update_Employee
                let url='update_Volunteer'
                if(!this.isEdit)
                    url='insert_Volunteer'
                axios.get(axios.defaults.baseURL+url,{params:
                    data
                }).then(res=>{
                    if(res.data.error!=0){
                        this.$message.error(res.data.messages)
                        this.addVisible=false
                        return
                    }
                    this.addVisible=false
                    this.$message.success('操作成功')
                    this.getTableData()
                })
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
                url: axios.defaults.baseURL + 'delete_Volunteer',
                params: this.multipleSelection[i]
              }).then((res) => {

                if (res.data.error === '0') {
                  this.$message.success(res.data.messages)
                  this.multipleSelection = [];
                  this.getTableData()
                }else{
                  this.$message.error(res.data.messages)
                }
              })
            }

          },

          //删除工作人员
            deleteNewWorker(index){

              this.$confirm('确定要删除吗？', '提示', {
                type: 'warning'
              })
                  .then(() => {
                    axios.get(axios.defaults.baseURL+'delete_Volunteer',{params:
                      index
                    }).then(res=>{
                      if(res.data.error!=0){
                        this.$message.error(res.data.messages)
                        return
                      }
                      this.$message.success('操作成功')
                      this.getTableData()
                    })
                  })

            },

            handleEdit(index, row){
                this.isEdit=true
                this.tableIndex=index;
                this.addVisible=true;
            },
            handleEditDialog(){
                if(!this.isEdit){
                    this.$refs.addPeople.VolunteerForm={
                        id:'',
                        username:'',
                        gender:'',
                        phone:'',
                        id_card:'',
                        birthday:'',
                        checkin_date:'',
                        checkout_date:'',
                        imgset_dir:'',
                        profile_photo:'',
                    }
                    return
                }
                this.$refs.addPeople.VolunteerForm=this.tableData[this.tableIndex]
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
        },
        computed: {
            unreadNum(){
                return this.unread.length;
            }
        }
    }

</script>

<style>

.handle-input {
  width: 300px;
  display: inline-block;
}
 .handle-box {
   margin-bottom: 20px;
 }

.handle-select {
  width: 120px;
}
.mr10 {
  margin-right: 10px;
}
.display-row {
        display: -webkit-flex; /* Safari */
        -webkit-justify-content: flex-start; /* Safari 6.1+ */
        display: flex;
        justify-content: flex-start;
        width: 100%;
    }
    .message-title{
        cursor: pointer;
    }
    .handle-row{
        margin-top: 30px;
    }
    .row-left {
        width: 6%;
    }

    .row-right{
        width: 50%;
    }
</style>

