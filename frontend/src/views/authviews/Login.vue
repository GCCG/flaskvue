<!--
 * @Author: your name
 * @Date: 2020-04-22 09:36:15
 * @LastEditTime: 2020-04-22 10:57:00
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /frontend/src/views/authviews/login.vue
 -->
<template>
    <div class="main">
        <div class="title">
            <span>密码登录</span>
        </div>

        <div class="title-msg">
            <span>请输入登录帐号和密码</span>
        </div>
        <!--
        <form class="login-form" method="post" novalidate>
        -->
        <form class="login-form" novalidate>
            <div class="input-content">
                <div>
                    <input type="text" autocomplete="off" placeholder="用户名" name="userNameOrEmailAddress" required/>
                </div>

                <div>
                    <input type="password" autocomplete="off" placeholder="登录密码" name="password" required maxlength="32"/>
                </div>

            </div>

            <div style="text-align: center">
                <button type="submit" class="enter-btn" v-on:click="onBnClick">登录</button>
            </div>

            <div class="foor">
                <div class="left">
                    <router-link to="/auth/forget-password" style="text-decoration: none">忘记密码？</router-link>
                </div>
                <div class="right">
                    <router-link to="/auth/register" style="text-decoration: none">注册用户</router-link>
                </div>
            </div>

        </form>
    </div>
</template>
<script>
//const FORGET_PASSWORD_URL = "/auth/forgetpasswordd"
//const REGISTER_URL = "/auth/register"
const MAIN_PAGE_URL = "/main-page"
export default {
    methods:{
        onBnClick: function(){
            this.$parent.$router.push(MAIN_PAGE_URL)
        }
    }
}
</script>

<style scoped>
.main {
    margin: 0 auto;
    padding-left: 25px;
    padding-right: 25px;
    padding-top: 15px;
    width: 350px;
    height: 350px;
    background: rgba(255, 255, 255, 0.85);
    /*以下css用于让登录表单垂直居中在界面,可删除*/
    position: absolute;
    top: 50%;
    left: 50%;
    margin-top: -175px;
    margin-left: -175px;

    /*控制登录表单的border */
    border-style: outset;
        
    border-radius: 20px;
}
 
.title {
    
    width: 100%;
    height: 40px;
    line-height: 40px;
}
 
.title span {
        
    font-size: 18px;
    color: #353f42;
}
 
.title-msg {
    text-align: left;
    width: 100%;
    height: 64px;
    line-height: 64px;
}
 
.title:hover{
    cursor: default	;
}
 
.title-msg:hover{
    cursor: default	;
}
 
.title-msg span {
        
    font-size: 12px;
    color: #707472;
}
 
.input-content {
    width: 100%;
    height: 120px;
}
 
.input-content input {
    width: 330px;
    height: 40px;
    border: 1px solid #dad9d6;
    background: #ffffff;
    padding-left: 10px;
    padding-right: 10px;
}
 
.enter-btn {
    width: 350px;
    height: 40px;
    color: #fff;
    background: #0bc5de;
    line-height: 40px;
    text-align: center;
    border: 0px;
}
 
.foor{
    width: 100%;
    height: auto;
    color: #9b9c98;
    font-size: 12px;
    margin-top: 20px;
}
 
.enter-btn:hover {
    cursor:pointer;
    background: #1db5c9;
}
 
.foor div:hover {
    cursor:pointer;
    color: #484847;
    font-weight: 600;
}
 
.left{
    float: left;
}
.right{
    float: right;
}
 
</style>