import Vue from 'vue'
import Router from 'vue-router'


Vue.use(Router)

import Layout from '@/views/Layout/Index'
import Home from '@/views/Home/Index'
import AboutDetail from '@/views/AboutDetail/Index'
// import Login from '@/views/Login/Index'


const routes = [
  // {
  //   path: "/login",
  //   name: "login",
  //   component: Login,
  // },
  {
    path: '/',
    component: Layout,
    children: [
      {
        path: '',
        name: 'Home',
        component: Home,
      },
      {
        path: '/aboutdetail',
        name: 'AboutDetail',
        component: AboutDetail,
      },
    ],
  },

]


const router = new Router({
  // mode: 'history',
  base: process.env.BASE_URL,
  routes
})
// // 导航守卫
// router.beforeEach((to, from, next) => {
//   console.log("页面进来了");
//
//   // const user = JSON.parse(window.localStorage.getItem('user'));
//   // if (to.path !== '/login') {
//   //   if(user) {
//   //     next
//   //   } else {
//   //     next('/login')
//   //   }
//   // } else {
//   //   next()
//   // }
//   const user = JSON.parse(window.localStorage.getItem('user'));
//   if(to.path === '/login') {
//     next()
//   } else {
//     if(user) {
//       next()
//     } else {
//       next('/login')
//     }
//   }
//
// });

export default router