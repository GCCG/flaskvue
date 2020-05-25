/*
 * @Author: your name
 * @Date: 2020-05-18 10:22:45
 * @LastEditTime: 2020-05-22 15:10:29
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /frontend/src/backend_api/restful_api.js
 */ 

 export const BACKEND_API_PREFIX = 'http://127.0.0.1:5000/api'

 export default {
    user: BACKEND_API_PREFIX+'/user',
    role: BACKEND_API_PREFIX+'/role',
    group: BACKEND_API_PREFIX+'/group',
    privilege: BACKEND_API_PREFIX+'/privilege',
    group_roles: BACKEND_API_PREFIX+'/group_roles',
    role_privileges: BACKEND_API_PREFIX+'/role_privileges',
    group_users: BACKEND_API_PREFIX+'/group_users',
    login: BACKEND_API_PREFIX+'/auth/login',
    forget_password: BACKEND_API_PREFIX+'/auth/forget_password',
    register: BACKEND_API_PREFIX+'/auth/register',
 }