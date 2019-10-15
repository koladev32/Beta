import Vue from 'vue'
import App from './App.vue'
import { router } from './router'
import BootstrapVue from 'bootstrap-vue'
import { store } from '@/store/store'
import VeeValidate from 'vee-validate'
import Bulma from 'bulma'

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
Vue.use(Bulma)

Vue.use(VeeValidate);

Vue.use(BootstrapVue);

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
