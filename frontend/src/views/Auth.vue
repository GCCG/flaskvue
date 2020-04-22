<!--
 * @Author: ccg
 * @Date: 2020-04-21 22:00:36
 * @LastEditTime: 2020-04-22 11:01:50
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /frontend/src/views/Auth.vue
 -->
<template>
    <div class="authview">
        <router-view />
    </div>
</template>

<script>

const LOGIN_URL = "/auth/login"


export default {

    created: function(){
        this.$router.push(LOGIN_URL)
    }
}
</script>

<style scoped>
.authview {
    position: absolute;
    top:0px;
    bottom: 0px;
    left: 0px;
    right: 0px;
    
    background-image: url("../assets/auth_background.jpeg");
    background-size: 100% 100%;
    background-repeat: no-repeat;
}

</style>