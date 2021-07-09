<template>
    <div class="">
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-lx-copy"></i> tab选项卡</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
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
                                @click="handleDelete(scope.$index, scope.row)"
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
                <div style="float: right"><el-button type="primary" size="mini" @click="addVisible=true">添加人员</el-button></div>
            </div>
        </div>
        <el-dialog
                :title="'添加人员'"
                :visible.sync="addVisible"
                width="500px"
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
        <el-dialog
                :title="'确定要删除'"
                :visible.sync="deleteVisible"
                width="500px"
                cente
                :modal-append-to-body="false">
            <span slot="footer" class="dialog-footer">
                <el-button @click="deleteNewWorker" type="primary">确 定</el-button>
                <el-button @click="deleteVisible = false">取 消</el-button>
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
                deleteVisible:false,
                message: 'first',
                showHeader: false,
                listForm1:{},
                addVisible:false,
                unread: [{
                    date: '2018-04-19 20:00:00',
                    title: '【系统通知】该系统将于今晚凌晨2点到5点进行升级维护',
                },{
                    date: '2018-04-19 21:00:00',
                    title: '今晚12点整发大红包，先到先得',
                }],
                read: [{
                    date: '2018-04-19 20:00:00',
                    title: '【系统通知】该系统将于今晚凌晨2点到5点进行升级维护'
                }],
                recycle: [{
                    date: '2018-04-19 20:00:00',
                    title: '【系统通知】该系统将于今晚凌晨2点到5点进行升级维护'
                }],
                tableData: [
                ],
            }
        },
        mounted() {
         this.getTableData()
        },
        methods: {
            getTableData(){
                axios.get('http://172.30.83.51:8080/select_Volunteer',{params:{

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
                axios.get(axios.defaults.baseURL+'insert_Volunteer',{params:
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
            handleDelete(index, row) {
                this.id=this.tableData[index].id
                this.deleteVisible=true
            },
            deleteNewWorker(){
                let data={id:this.id}
                axios.get(axios.defaults.baseURL+'delete_Volunteer',{params:
                    data
                }).then(res=>{
                    if(res.data.error!=0){
                        this.$message.error(res.data.messages)
                        this.deleteVisible=false
                        return
                    }
                    this.deleteVisible=false
                    this.$message.success('操作成功')
                    this.getTableData()
                })
            }
        },
        computed: {
            unreadNum(){
                return this.unread.length;
            }
        }
    }

</script>

<style>
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

