<template>
  <div class="login-container">

    <el-form
      ref="login-form"
      :model="user"
      class="login-form"
      :rules="formRules"
    >
      <div class="login-head"></div>
      <el-form-item prop="username">
        <el-input placeholder="请输入手机号" v-model="user.username"></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input
          type="password"
          autocomplete="off"
          placeholder="请输入密码"
          v-model="user.password"
        ></el-input>
      </el-form-item>

      <el-form-item prop="isAgree">
        <el-checkbox v-model="user.isAgree">我已阅读并同意该条款</el-checkbox>
      </el-form-item>
      <el-form-item>
        <el-button
          class="login-btn"
          type="primary"
          @click="onLogin"
          :loading="loginLoading"
        >登录</el-button>
      </el-form-item>

    </el-form>
  </div>
</template>

<script>

  import Qs from 'qs'
  import { login } from'@/api/user'
  export default {
    name: "LoginIndex",
    data() {
      return {
        user: {
          username:'15675323192',
          password: 'dxzxomy',
          isAgree: false,
        },
        loginLoading: false,
        formRules: {
          username: [
            { required: true, message: '请输入手机号', trigger: 'change' },
            { pattern: /^1[3|5|7|8|9]\d{9}$/, message: '请输入正确的号码格式 ', trigger: 'change' }
          ],
          password: [
            { required: true, message: '请输入密码', trigger: 'change' },
            { pattern: /\w{5,}/, message: '请输入正确的密码 '},
          ],
          isAgree: [{
            validator: (rule, value, callback) => {
              if(value) {
                callback()
              } else {
                callback(new Error('请同意用户协议'))
              }
           },
            trigger: 'change'
          }]
        }
      }
    },
    methods: {
      onLogin() {
        // 表单验证
        // validate 方法是一部的
        this.$refs["login-form"].validate(valid => {
          if(!valid) {
            return
          }
          this.login()
        });
      },
      login() {
        this.loginLoading = true;
        login(Qs.stringify(this.user
        )).then(res => {
          console.log(res.data);

          this.$message({
            message: "登录成功",
            type: 'success'
          });
          this.loginLoading = false;
          window.localStorage.setItem('user', JSON.stringify(res.data));
          this.$router.push({
            name: 'Home',
          })
        }).catch(err => {
          console.log(err);
          this.$message.error('账号或密码错误');
          this.loginLoading = false;
        })
      }
    }
  }
</script>

<style scoped>
  .login-head {
    background: url(../../assets/logo.png) no-repeat;
    width: 100%;
    height: 57px;
  }
  .login-container {
    background: url(../../assets/2.jpg) no-repeat;;
    background-size:cover;
    position: fixed;
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    flex-direction: column;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .login-form {
    background: url(http://demo.kangjingept.com:8020/cssthemes6/1124zh5/images/1.png);
    padding: 60px;
    min-width: 300px;
  }
  .login-btn {
    width: 100%;
  }
</style>
