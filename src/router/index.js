import { createRouter } from 'vue-router'
import { createWebHashHistory } from 'vue-router'
import Register from '../views/Register.vue'
import Login from '../views/Login.vue'
import Home from '../views/Home.vue'
import OldManage from '../views/OldManage.vue'
import VolunteerManage from '../views/VolunteerManage.vue'
import AdminManage from '../views/AdminManage.vue'
import Camera from '../views/Camera.vue'
import Information from '../views/Information.vue'

const routes = [
  {
    path: "/",
    name: "/",
    component: Login,
  },
  {
    path: "/register",
    name: "/register",
    component: Register,
  },
  {
    path: "/home",
    name: "/home",
    component: Home,
    children:[
      {
        path: "/camera",
        name: "/camera",
        component: Camera,
      },
      {
        path: "/information",
        name: "/information",
        component: Information,
      },
      {
        path: "/oldmanage",
        name: "/oldmanage",
        component: OldManage,
      },
      {
        path: "/volunteermanage",
        name: "/volunteermanage",
        component: VolunteerManage,
      },
      {
        path: "/adminmanage",
        name: "/adminmanage",
        component: AdminManage,
      }
    ]
  }

]

// const routes = [
//   {
//     path: '/',
//     component: Home,
//     children: [
//       {
//         path: "/search",
//         name: "/search",
//         component: Search,
//       },
//       {
//         path: "/login",
//         name: "/login",
//         component: Login,
//       },
//       {
//         path: "/register",
//         name: "/register",
//         component: Register,
//       },
//       {
//         path: "/homepage",
//         name: "/homepage",
//         component: Homepage,
//       },
//       {
//         path: "/recommend/:page",
//         name: "/recommend",
//         component: Recommend,
//       },
//       {
//         path: "/highrating/:page",
//         name: "/highrating",
//         component: HighRating,
//       },
//       {
//         path: "/hot/:page",
//         name: "/hot",
//         component: Hot,
//       },
//       {
//         path: "/moviedetails/:id",
//         name: "/moviedetails",
//         component: Moviedetails,
//       },
//       {
//         path: "/userpage",
//         name: "/userpage",
//         component: Userpage,
//       },
//     ]
//   },
//   {path:'/add',component:Add},
//   // {path:'/login',component:Login},
//   // {path:'/register',component:Register},
//   // {path:'/search',component:Search},
// ]
const router = createRouter({
  history: createWebHashHistory(),
  routes: routes
})

export default router