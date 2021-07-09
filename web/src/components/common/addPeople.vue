<template>
    <div>
<!--        占位-->
<!--        <el-image></el-image>-->
<!--        <video ref="video" style="width: 100%;height: 200px" autoplay></video>-->
        <div v-if="peopleType==0">
            <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>姓名 ：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="姓名" v-model="workform.username"
                               autosize ></el-input>
                </div>
            </div>
            <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>性别 ：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="性别" v-model="workform.gender"
                               autosize ></el-input>
                </div>
            </div>
            <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>电话 ：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="电话" v-model="workform.phone"
                               autosize ></el-input>
                </div>
            </div>
            <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>身份证号码 ：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="身份证号码" v-model="workform.id_card"
                               autosize ></el-input>
                </div>
            </div>
            <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>出生日期 ：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="出生日期" v-model="workform.birthday"
                               autosize ></el-input>
                </div>
            </div>
            <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>	入职日期 ：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="入职日期" v-model="workform.hire_date"
                               autosize ></el-input>
                </div>
            </div>
            <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>离职日期 ：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="离职日期"  v-model="workform.resign_date"
                               autosize ></el-input>
                </div>
            </div>
            <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>图像目录 ：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="图像目录" v-model="workform.imgset_dir"
                               autosize ></el-input>
                </div>
            </div>
            <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>头像：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="头像" v-model="workform.profile_photo"
                               autosize ></el-input>
                </div>
            </div>
        </div>
        <div v-if="peopleType==1">
            <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>姓名 ：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="姓名" v-model="VolunteerForm.name"
                               autosize ></el-input>
                </div>
            </div>
            <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>性别 ：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="性别" v-model="VolunteerForm.gender"
                               autosize ></el-input>
                </div>
            </div>
            <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>电话 ：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="电话" v-model="VolunteerForm.phone"
                               autosize ></el-input>
                </div>
            </div>
            <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>身份证号码 ：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="身份证号码" v-model="VolunteerForm.id_card"
                               autosize ></el-input>
                </div>
            </div>
            <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>出生日期 ：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="出生日期" v-model="VolunteerForm.birthday"
                               autosize ></el-input>
                </div>
            </div>
            <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>	访问日期 ：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="入职日期" v-model="VolunteerForm.checkin_date"
                               autosize ></el-input>
                </div>
            </div>
            <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>离开日期 ：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="离职日期"  v-model="VolunteerForm.checkout_date"
                               autosize ></el-input>
                </div>
            </div>
            <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>图像目录 ：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="图像目录" v-model="VolunteerForm.imgset_dir"
                               autosize ></el-input>
                </div>
            </div>
            <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>头像：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="头像" v-model="VolunteerForm.profile_photo"
                               autosize ></el-input>
                </div>
            </div>
        </div>
        <div v-if="peopleType==2" style="display: flex">
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
                    <el-input  placeholder="性别" v-model="olderform.gender"
                               autosize ></el-input>
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
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>身份证号码 ：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="身份证号码" v-model="olderform.id_card"
                               autosize ></el-input>
                </div>
            </div>
            <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>出生日期 ：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="出生日期" v-model="olderform.birthday"
                               autosize ></el-input>
                </div>
            </div>
            <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>	入养老院日期 ：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="入养老院日期" v-model="olderform.checkin_date"
                               autosize ></el-input>
                </div>
            </div>
            <div style="margin-top:20px;align-items: center;justify-content: center;width: 100%" class="display-row">
                <div style="margin-left: 1rem;width: 20%;text-align: right"><p>离开养老院日期 ：</p></div>
                <div class="titleinput row-right">
                    <el-input  placeholder="离开养老院日期"  v-model="olderform.checkout_date"
                               autosize ></el-input>
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
    </div>
</template>

<script>
    export default {
        name: "addPeople",
        props:{
            peopleType:{
                type:Number,//0工作人员 ,1志愿者,2老人
                default:4,
            }
        },
        data(){
            return{
                olderform:{
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
                    room_number:'',
                    firstguardian_name:'',
                    firstguardian_relationship:'',
                    firstguardian_phone:'',
                    firstguardian_wechat:'',
                    secondguardian_name:'',
                    secondguardian_relationship:'',
                    secondguardian_phone:'',
                    secondguardian_wechat:'',
                    health_state:'',
                },
                workform:{
                    id:'',
                    username:'',
                    gender:'',
                    phone:'',
                    id_card:'',
                    birthday:'',
                    hire_date:'',
                    resign_date:'',
                    imgset_dir:'',
                    profile_photo:'',
                },
                VolunteerForm:{
                    id:'',
                    name:'',
                    gender:'',
                    phone:'',
                    id_card:'',
                    birthday:'',
                    checkin_date:'',
                    checkout_date:'',
                    imgset_dir:'',
                    profile_photo:'',
                }
            }
        },
        mounted() {
            this.callCamera()
        },
        methods:{
            callCamera () {
                // H5调用电脑摄像头API
                navigator.mediaDevices.getUserMedia({
                    video: true
                }).then(success => {
                    // 摄像头开启成功
                    this.$refs['video'].srcObject = success
                    // 实时拍照效果
                    this.$refs['video'].play()
                }).catch(error => {
                    console.error('摄像头开启失败，请检查摄像头是否可用！')
                })
            },
        }
    }
</script>

<style scoped>
    .display-row {
        display: -webkit-flex; /* Safari */
        -webkit-justify-content: flex-start; /* Safari 6.1+ */
        display: flex;
        justify-content: flex-start;
        width: 100%;
    }

    .row-left {
        width: 6%;
    }

    .row-right{
        width: 50%;
    }

    .titleClass {
        color: gray;
    }

    .row {
        display: flex;
        align-items: center;
        justify-content: center
    }

    .row-margin {
        margin-top: 20px;
    }

    .text {
        font-weight: bold;
    }
</style>
