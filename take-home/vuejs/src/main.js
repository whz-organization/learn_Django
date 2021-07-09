/*eslint no-console: ["error", { allow: ["warn", "error"] }] */

import Vue from 'vue';
import App from './App.vue';
import vuetify from '@/plugins/vuetify';
import Vuetify from 'vuetify';
import router from './router';
import Nprogress from 'nprogress';

import './lib/main-css';

Vue.config.productionTip = false;

Vue.use(Vuetify);

// eslint-disable-next-line
router.beforeEach((to, from, next) => {
  Nprogress.start();
  next();
});

// eslint-disable-next-line
router.afterEach((to, from) => {
  Nprogress.done();
});

// eslint-disable-next-line no-new
new Vue({
  vuetify,
  router,
  render: h => h(App),
}).$mount('#app');
