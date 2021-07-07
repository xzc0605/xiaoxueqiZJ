<template>
    <div class="login-wrap">
        <div class="ms-login">
            <div class="ms-title">OldCare系统</div>
            <el-form :model="form" :rules="rules" ref="login" label-width="0px" class="ms-content">
                <el-form-item prop="username" v-show="showL">
                    <el-input v-model="form.email" placeholder="email">
                        <el-button slot="prepend" icon="el-icon-lx-people"></el-button>
                    </el-input>
                </el-form-item>
                <el-form-item prop="password" v-show="showL">
                    <el-input
                        type="password"
                        placeholder="password"
                        v-model="form.password"
                        @keyup.enter.native="Login()"
                    >
                        <el-button slot="prepend" icon="el-icon-lx-lock"></el-button>
                    </el-input>
                </el-form-item>

              <el-form-item prop="username" v-show="showR">
                <el-input v-model="form.email" placeholder="email">
                  <el-button slot="prepend" icon="el-icon-lx-people"></el-button>
                </el-input>
              </el-form-item>
              <el-form-item prop="username" v-show="showR">
                <el-input v-model="form.phone" placeholder="phone">
                  <el-button slot="prepend" icon="el-icon-lx-people"></el-button>
                </el-input>
              </el-form-item>
              <el-form-item prop="username" v-show="showR">
                <el-input v-model="form.nickname" placeholder="nickname">
                  <el-button slot="prepend" icon="el-icon-lx-people"></el-button>
                </el-input>
              </el-form-item>
              <el-form-item prop="password" v-show="showR">
                <el-input
                    type="password"
                    placeholder="password"
                    v-model="form.password"
                >
                  <el-button slot="prepend" icon="el-icon-lx-lock"></el-button>
                </el-input>
              </el-form-item>
              <el-form-item prop="password" v-show="showR">
                <el-input
                    type="password"
                    placeholder="password again"
                    v-model="form.repassword"
                >
                  <el-button slot="prepend" icon="el-icon-lx-lock"></el-button>
                </el-input>
              </el-form-item>



                <div class="login-btn">
                    <el-button type="primary" @click="Login()" v-show="showL">登录</el-button>
                </div>
              <div class="login-btn">
                <el-button type="primary" @click="toRegister()" v-show="showL">去注册</el-button>
              </div>
              <div class="login-btn">
                <el-button type="primary" @click="Register()" v-show="showR">注册</el-button>
              </div>
              <div class="login-btn">
                <el-button type="primary" @click="toLogin()" v-show="showR">去登录</el-button>
              </div>
                <p class="login-tips">Tips : 用户名和密码随便填。</p>
            </el-form>
        </div>
    </div>
</template>

<script>
export default {
    data: function() {
        return {
          showL: true,
          showR: false,

          form: {
            email: "",
            password: "",
            repassword: "",
            nickname: "",
            phone: ""
          },

            param: {
                username: 'admin',
                password: '123123',
            },

          //表单的验证规则对象
          rules: {
            email: [
              {required: true, message: '请输入用户账户（邮箱）', trigger: 'blur'},
            ],
            password: [
              {required: true, message: '请输入密码', trigger: 'blur'},
              {min: 3, max: 10, message: '长度在3到10个字符之间', trigger: 'blur'}
            ]
          }
           /* rules: {
                username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
                password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
            },*/
        };
    },
    methods: {
        async Login() {
            this.$refs.login.validate(async valid => {
                if (valid) {
                    this.$message.success('登录成功');
                    localStorage.setItem('ms_username', this.param.username);
                    this.$router.push('/');
                } else {
                    this.$message.error('请输入账号和密码');
                    console.log('error submit!!');
                    return false;
                }
            });
        },
      Register(){
        if (this.form.email.length === 0) {
          this.$message.error("邮箱不得为空")
          return;
        }

        this.$refs.login.validate(async valid => {
              if (!valid) {
                this.$message.error("输入格式错误")
                return;
              }
              if (this.form.password !== this.form.repassword) {
                this.$message.error("两次输入密码不一致")
                return;
              }

        })
      },
      toRegister() {
        this.showL = false;
        this.showR = true;
        this.form.repassword = "";
        this.form.password = "";
        this.form.email = "";
        this.form.phone = "";
      },
      toLogin() {
        this.showL = true;
        this.showR = false;
        this.form.passAgain = "";
        this.form.password = "";
        this.form.email = "";
        this.form.nickname="";
      }
    },
};
</script>

<style scoped>
.login-wrap {
    position: relative;
    width: 100%;
    height: 100%;
    background-image: url(../../assets/img/login-bg.jpg);
    background-size: 100%;
}
.ms-title {
    width: 100%;
    line-height: 50px;
    text-align: center;
    font-size: 20px;
    color: #fff;
    border-bottom: 1px solid #ddd;
}
.ms-login {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 350px;
    margin: -190px 0 0 -175px;
    border-radius: 5px;
    background: rgba(255, 255, 255, 0.3);
    overflow: hidden;
}
.ms-content {
    padding: 30px 30px;
}
.login-btn {
    text-align: center;
}
.login-btn button {
    width: 100%;
    height: 36px;
    margin-bottom: 10px;
}
.login-tips {
    font-size: 12px;
    line-height: 30px;
    color: #fff;
}
</style>