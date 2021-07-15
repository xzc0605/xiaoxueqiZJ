<template>
    <div style="display: flex">
        <!--        <div style="display: flex;margin-left: 10px;-->
        <!--                    flex-flow: column;width: 50%;margin-right: 20px">-->
        <el-card style="height: 500px;width: 50%;margin-right: 10px" shadow="hover">
            <el-dropdown @command="changeYear">
              <span class="el-dropdown-link">
                {{this.yearNow+'年龄分布'}}<i class="el-icon-arrow-down el-icon--right"></i>
              </span>
                <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item v-for="item in yearList" :command="item"
                                      >{{item}}</el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown>
            <div id="BarChart" style="width: 100%;height: 400px"></div>
        </el-card >
        <el-card  shadow="hover" style="width: 50%;">
            <div id="pieChart" style="width: 100%;height: 400px"></div>
        </el-card>
        <!--        </div>-->

        <div>

        </div>
    </div>
</template>

<script>
    import * as echarts from 'echarts'
    import axios from 'axios'
    export default {
        name: 'dashboard',
        data() {
            return {
                yearData:[],
                yearList:[],
                monthList:{'01':0,'02':0,'03':0,'04':0,
                    '05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0,'12':0},
                yearNow:'2022',
                monthArray:[],
                allyeayData:[],
            };
        },
        mounted() {

            axios.get('http://172.30.95.28:8080/analysis_oldpeople').then(res=>{
                res.data.data.forEach(item=>{
                    for(var key in item){
                        this.yearData.push({name:key,value:item[key]})
                    }
                })
                this.drawPieChart()
                axios.get('http://172.30.95.28:8080/analysis_oldpeolpe_checkin').then(
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


        },
        methods: {
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
            }
        }
    };
</script>


<style scoped>
    .el-row {
        margin-bottom: 20px;
    }

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
        color: rgb(45, 140, 240);
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

    .todo-item {
        font-size: 14px;
    }

    .todo-item-del {
        text-decoration: line-through;
        color: #999;
    }

    .schart {
        width: 100%;
        height: 300px;
    }
</style>
<!--                <el-card shadow="hover" class="mgb20" style="height:252px;">-->
<!--                    <div class="user-info">-->
<!--                        <img src="../../assets/img/img.jpg" class="user-avator" alt />-->
<!--                        <div class="user-info-cont">-->
<!--                            <div class="user-info-name">{{name}}</div>-->
<!--                            <div>{{role}}</div>-->
<!--                        </div>-->
<!--                    </div>-->
<!--                    <div class="user-info-list">-->
<!--                        上次登录时间：-->
<!--                        <span>2019-11-01</span>-->
<!--                    </div>-->
<!--                    <div class="user-info-list">-->
<!--                        上次登录地点：-->
<!--                        <span>东莞</span>-->
<!--                    </div>-->
<!--                </el-card>-->
