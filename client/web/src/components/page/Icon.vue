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
              <div class="grid-num">{{ oldperson_num }}</div>
              <div>老人数量</div>
            </div>
          </div>
        </el-card>

        <el-card style="margin-top: 20px" shadow="hover" :body-style="{padding: '0px'}">
          <div  class="grid-content grid-con-2">
            <i class="el-icon-coordinate grid-con-icon"></i>
            <div class="grid-cont-right">
              <div class="grid-num">{{ employee_num }}</div>
              <div>工作人员数量</div>
            </div>
          </div>
        </el-card>

        <el-card style="margin-top: 20px" shadow="hover" :body-style="{padding: '0px'}">
          <div  class="grid-content grid-con-3">
            <i class="el-icon-mouse grid-con-icon"></i>
            <div class="grid-cont-right">
              <div class="grid-num">{{ volunteer_num }}</div>
              <div>义工数量</div>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
    <el-button style="float: left; padding: 3px 0" type="text" @click="showDetails()">查看详情</el-button>
    <div style="display: flex;margin-top: 20px">

      <el-card style="height: 250px;width: 50%;margin-right: 10px" shadow="hover">

        <div id="BarChart" style="width: 100%;height: 200px"></div>
      </el-card >
      <el-card  shadow="hover" style="width: 50%;">
        <div id="pieChart" style="width: 100%;height: 200px"></div>
      </el-card>
    </div>

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
    import * as echarts from "echarts";

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

              oldperson_num:0,
              employee_num:0,
              volunteer_num:0,

              yearData:[],
              yearList:[],
              monthList:{'01':0,'02':0,'03':0,'04':0,
                '05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0,'12':0},
              yearNow:'2022',
              monthArray:[],
              allyeayData:[],
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
                  this.tableData.password=res.data.data.password,
                  this.oldperson_num=res.data.oldperson_num,
                  this.employee_num=res.data.employee_num,
                  this.volunteer_num=res.data.volunteer_num
            }else{
              this.$message.error("error")
            }
            axios.get(axios.defaults.baseURL+'analysis_oldpeople').then(res=>{
              res.data.data.forEach(item=>{
                for(var key in item){
                  this.yearData.push({name:key,value:item[key]})
                }
              })
              this.drawPieChart()
              axios.get(axios.defaults.baseURL+'analysis_oldpeolpe_checkin').then(
                  res=>{
                    this.allyeayData=res.data.data[0].年份
                    this.allyeayData.forEach(item=>{
                      if(item[0]==this.yearNow){
                        this.monthList[item[1]]=item[2]
                      }
                      this.yearList.push(item[0])
                    })
                    this.yearList=Array.from(new Set(this.yearList))
                    for(var key in this.monthList){
                      this.monthArray.push(this.monthList[key])
                    }
                    this.drawBarchart()
                  }
              )
            })
          })
        },

        showDetails(){
          this.$router.push('/health')
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
        drawPieChart(){
          let myChart = echarts.init(document.getElementById('pieChart'));
          let option = {
            title: {
              text: '年度访问比率',
              left: 'center'
            },
            tooltip: {
              trigger: 'item'
            },
            legend: {
              orient: 'vertical',
              left: 'left',
            },
            series: [
              {
                name: '访问来源',
                type: 'pie',
                radius: '50%',
                data: this.yearData,
                emphasis: {
                  itemStyle: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0,0,0,0.5)'
                  }
                }
              }
            ]
          };
          myChart.setOption(option)
        },
        drawBarchart(){
          let myChart = echarts.init(document.getElementById('BarChart'));
          let option = {
            // title: {
            //     text: this.yearNow+'年龄分布',//
            // },
            tooltip: {
              trigger: 'axis'
            },
            // legend: {
            //     data: ['男', '女']
            // },
            legend: {
              data: ['人数分布']
            },
            toolbox: {
              show: true,
              feature: {
                dataView: {show: true, readOnly: false},
                magicType: {show: true, type: ['line', 'bar']},
                restore: {show: true},
                saveAsImage: {show: true}
              }
            },
            calculable: true,
            xAxis: [
              {
                type: 'category',
                data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
              }
            ],
            yAxis: [
              {
                type: 'value'
              }
            ],
            grid:{
              y:30,
              y2:30
            },
            series: [
              {
                name: '人数分布',
                type: 'bar',
                data: this.monthArray,
                // markPoint: {
                //     data: [
                //         {type: 'max', name: '最大值'},
                //         {type: 'min', name: '最小值'}
                //     ]
                // },
                // markLine: {
                //     data: [
                //         {type: 'average', name: '平均值'}
                //     ]
                // }
              },
              // {
              //     name: '女',
              //     type: 'bar',
              //     data: [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
              //     // markPoint: {
              //     //     data: [
              //     //         {name: '年最高', value: 182.2, xAxis: 7, yAxis: 183},
              //     //         {name: '年最低', value: 2.3, xAxis: 11, yAxis: 3}
              //     //     ]
              //     // },
              //     // markLine: {
              //     //     data: [
              //     //         {type: 'average', name: '平均值'}
              //     //     ]
              //     // }
              // }
            ]
          };
          myChart.setOption(option,true)
        },
        changeYear(item1){
          this.yearNow=item1
          this.monthArray=[]
          this.monthList={'01':0,'02':0,'03':0,'04':0,
            '05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0,'12':0},
              this.allyeayData.forEach(item=>{
                if(item[0]==this.yearNow){
                  this.monthList[item[1]]=item[2]
                }
              })
          for(var key in this.monthList){
            this.monthArray.push(this.monthList[key])
          }
          this.drawBarchart()
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
