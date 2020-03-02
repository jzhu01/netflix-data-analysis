import Vue from 'vue';
import VueRouter from 'vue-router';
import App from './App.vue';
import fullView from './components/fullView.vue';
import individualView from './components/individualView.vue';

Vue.config.productionTip = false;
Vue.use(VueRouter);

const routes = [
  { path: '/', component: fullView },
  { path: '/individualView', component: individualView },
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
