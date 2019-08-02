import Vue from 'vue'
import Router from 'vue-router'
import Landing from './views/Landing.vue'
import Auth from './components/Auth.vue'
import Home from './views/Home.vue'
import Register from './components/Register.vue'

Vue.use(Router)

export const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [{
      path: '/login',
      name: 'auth',
      component: Auth
    },
    {
      path:'/',
      name:'home',
      component:Home
    },

    {

      path: '/land',
      name: 'landing',
      component: Landing
    },
    {
      path: '/register',
      name: 'register',
      component: Register

    },

    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import( /* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path:'*',redirect:'/'
    }


  ]
});

router.beforeEach((to,from,next)=>{
  //redirect to login page if not logged and trying to acess restricted pages

  const publicPages = ['/login','/register','/land'];
  const authRequired = !publicPages.includes(to.path)
  const loggedIn = localStorage.getItem('user');

  if (authRequired && !loggedIn){
    return next('/login');
  }
  next()
})