import Vue from "vue";
import iView from "iview";
import VueRouter from "vue-router";
import Routers from "./router";
import Util from "./libs/util";
import App from "./app.vue";
import "iview/dist/styles/iview.css";

Vue.use(VueRouter);
Vue.use(iView);

// 路由配置

import TOP from "./views/Page/TOP/index.vue";
import middle from "./views/Page/middle/index.vue";
import Form from "./views/Details/DetailsForm/index.vue";

export default new VueRouter({
  routes: [
    {
      path: "/TOP",
      name: "TOP",
      component: TOP
    },
    {
      path: "/",
      redirect: "/TOP"
    },
    {
      path: "/middle",
      name: "middle",
      component: middle
    },
    {
      path: "/Form",
      component: Form
    }
  ]
});

const RouterConfig = {
  mode: "history",
  routes: Routers
};
const router = new VueRouter(RouterConfig);

router.beforeEach((to, from, next) => {
  iView.LoadingBar.start();
  Util.title(to.meta.title);
  next();
});

router.afterEach((to, from, next) => {
  iView.LoadingBar.finish();
  window.scrollTo(0, 0);
});

new Vue({
  el: "#app",
  router: router,
  render: h => h(App)
});
