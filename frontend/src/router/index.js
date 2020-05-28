/*
 * @Author: your name
 * @Date: 2020-04-18 10:40:50
 * @LastEditTime: 2020-05-28 11:44:17
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /frontend/src/router/index.js
 */
import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'
//import About from '../views/About.vue'
//import Mainview from '../views/Main.vue'

import UserMng from '../views/mainviews/UserMng.vue'
import RoleMng from '../views/mainviews/RoleMng.vue'
import GroupMng from '../views/mainviews/GroupMng.vue'
import AuthConfig from '../views/mainviews/AuthConfig.vue'
import StationMng from '../views/mainviews/StationMng.vue'
import AuthView from '../views/Auth.vue'
import AuthLogin from '../views/authviews/Login.vue'
import AuthRegister from '../views/authviews/Register.vue'
import AuthForgetPassword from '../views/authviews/ForgetPassword.vue'
import MainPage from '../views/Main.vue'
import BlankPage from '../views/mainviews/Blank.vue'

Vue.use(VueRouter)

  const routes = [
  //鉴权界面
	{
    path: '/auth',
    name: 'Auth',
    component: AuthView,
    children: [
      {
        path: '/auth/login',
        name: 'AuthLogin',
        component: AuthLogin
      },
      {
        path: '/auth/register',
        name: 'AuthRegister',
        component: AuthRegister
      },
      {
        path: '/auth/forget-password',
        name: 'AuthForgetPassword',
        component: AuthForgetPassword
      },
    ]
  },
  //主界面
  {
    path: '/main-page',
    name: 'MainPage',
    component: MainPage,
    children:[
      {
        path: '/main-page/user-mng',
        name: 'UserMng',
        component: UserMng
      },
      {
        path: '/main-page/blank',
        name: 'Blank',
        component: BlankPage
      },
      {
        path: '/main-page/role-mng',
        name: 'RoleMng',
        component: RoleMng
      },
      {
        path: '/main-page/group-mng',
        name: 'GroupMng',
        component: GroupMng
      },
      {
        path: '/main-page/auth-config',
        name: 'AuthConfig',
        component: AuthConfig,
      },
      {
        path: '/main-page/station-mng',
        name: 'StationMng',
        component: StationMng,
      },
    ]
	},
  // {
  //   path: '/',
  //   name: 'Home',
  //   component: Home
	// },

  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  //   //component: About
	// }
	
]

const router = new VueRouter({
  routes
})

export default router
