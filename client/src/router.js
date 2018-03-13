const routers = [
  {
    path: "/",
    meta: {
      title: ""
    },
    component: resolve =>
      require(["./views/Details/DetailsForm/index.vue"], resolve),
    component: resolve => require(["./views/moowei/index.vue"], resolve)
  }
];

export default routers;
