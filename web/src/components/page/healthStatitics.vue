<template>
    <div style="display: flex">
        <!--        <div style="display: flex;margin-left: 10px;-->
        <!--                    flex-flow: column;width: 50%;margin-right: 20px">-->
        <el-card style="height: 500px;width: 50%;margin-right: 10px" shadow="hover">
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
    import API from "../../api";
    export default {
        name: 'dashboard',
        data() {
            return {
                name: localStorage.getItem('ms_username'),
                todoList: [
                    {
                        title: '今天要修复100个bug',
                        status: false
                    },
                    {
                        title: '今天要修复100个bug',
                        status: false
                    },
                    {
                        title: '今天要写100行代码加几个bug吧',
                        status: false
                    },
                    {
                        title: '今天要修复100个bug',
                        status: false
                    },
                    {
                        title: '今天要修复100个bug',
                        status: true
                    },
                    {
                        title: '今天要写100行代码加几个bug吧',
                        status: true
                    }
                ],
                data: [
                    {
                        name: '2018/09/04',
                        value: 1083
                    },
                    {
                        name: '2018/09/05',
                        value: 941
                    },
                    {
                        name: '2018/09/06',
                        value: 1139
                    },
                    {
                        name: '2018/09/07',
                        value: 816
                    },
                    {
                        name: '2018/09/08',
                        value: 327
                    },
                    {
                        name: '2018/09/09',
                        value: 228
                    },
                    {
                        name: '2018/09/10',
                        value: 1065
                    }
                ],
                options: {
                    type: 'bar',
                    title: {
                        text: '最近一周各品类销售图'
                    },
                    xRorate: 25,
                    labels: ['周一', '周二', '周三', '周四', '周五'],
                    datasets: [
                        {
                            label: '家电',
                            data: [234, 278, 270, 190, 230]
                        },
                        {
                            label: '百货',
                            data: [164, 178, 190, 135, 160]
                        },
                        {
                            label: '食品',
                            data: [144, 198, 150, 235, 120]
                        }
                    ]
                },
                options2: {
                    type: 'line',
                    title: {
                        text: '最近几个月各品类销售趋势图'
                    },
                    labels: ['6月', '7月', '8月', '9月', '10月'],
                    datasets: [
                        {
                            label: '家电',
                            data: [234, 278, 270, 190, 230]
                        },
                        {
                            label: '百货',
                            data: [164, 178, 150, 135, 160]
                        },
                        {
                            label: '食品',
                            data: [74, 118, 200, 235, 90]
                        }
                    ]
                }
            };
        },
        computed: {
            role() {
                return this.name === 'admin' ? '超级管理员' : '普通用户';
            }
        },
        mounted() {
            // // 测试
            // let data={"arg":{"channelType":2,"collapseType":0,
            //         "commentTagId":0,"pageIndex":2,"pageSize":10,
            //         "poiId":10758959,"sourceType":1,"sortType":3,
            //         "starType":0},"head":{"cid":"09031091314687468312"
            //         ,"ctok":"","cver":"1.0","lang":"01","sid":"8888",
            //         "syscode":"09","auth":"","xsid":"","extension":[]}}
            // API.test(data).then(res=>{
            //     console.log(res)
            // })
            this.drawBarchart()
            this.drawPieChart()
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
                            data: [
                                {value: 1048, name: '2021'},
                                {value: 735, name: '2020'},
                                {value: 580, name: '2019'},
                                {value: 484, name: '2018'},
                                {value: 300, name: '2017'}
                            ],
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
            changeDate() {
                const now = new Date().getTime();
                this.data.forEach((item, index) => {
                    const date = new Date(now - (6 - index) * 86400000);
                    item.name = `${date.getFullYear()}/${date.getMonth() + 1}/${date.getDate()}`;
                });
            },
            drawBarchart(){
                let myChart = echarts.init(document.getElementById('BarChart'));
                let option = {
                    title: {
                        text: '2019年龄分布',//
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    legend: {
                        data: ['男', '女']
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
                            name: '男',
                            type: 'bar',
                            data: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
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
                        {
                            name: '女',
                            type: 'bar',
                            data: [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
                            // markPoint: {
                            //     data: [
                            //         {name: '年最高', value: 182.2, xAxis: 7, yAxis: 183},
                            //         {name: '年最低', value: 2.3, xAxis: 11, yAxis: 3}
                            //     ]
                            // },
                            // markLine: {
                            //     data: [
                            //         {type: 'average', name: '平均值'}
                            //     ]
                            // }
                        }
                    ]
                };
                myChart.setOption(option)
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
