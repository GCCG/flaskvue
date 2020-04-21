import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
//import About from '../views/About.vue'
//import Mainview from '../views/Main.vue'
import Searchblock from '../components/searchblock.vue'
import UserMng from '../views/UserMng.vue'

Vue.use(VueRouter)

  const routes = [
	
  {
    path: '/',
    name: 'Home',
    component: Home
	},
	
	{
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/search-block',
    name: 'Search-Block',
    component: Searchblock
  },
  {
    path: '/authmng/usermng',
    name: 'User-Mng',
    component: UserMng
	},
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    //component: About
	}
	
]

const router = new VueRouter({
  routes
})

export default router
