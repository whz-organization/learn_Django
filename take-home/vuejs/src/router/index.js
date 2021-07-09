import Vue from 'vue';

import VueRouter from 'vue-router';

import Home from '../components/routes/Home.vue';

Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    // Global routes
    {
      name: 'home',
      path: '/',
      component: Home,
    },
  ],
});
