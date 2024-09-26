import { createWebHistory, createRouter } from "vue-router";
import Index from "./components/Index.vue";

const routes = [
  //一级路由
  { path: "/", redirect: "index" },
  {
    path: "/index",
    name: "Index",
    component: Index,
    //路由嵌套
    // children: [
    //   {
    //     path: "/index/vis_traj",
    //     component: () => import("./components/VisTraj.vue"),
    //   },
    //   {
    //     path: "/index/plot_opt",
    //     component: () => import("./components/PlotOpt.vue"),
    //   },
    //   {
    //     path: "/index/plot_ep",
    //     component: () => import("./components/PlotEP.vue"),
    //   },
    //   {
    //     path: "/index/plot_band",
    //     component: () => import("./components/PlotBand.vue"),
    //   },
    //   {
    //     path: "/index/plot_dos",
    //     component: () => import("./components/PlotDOS.vue"),
    //   },
    //   {
    //     path: "/index/plot_pes",
    //     component: () => import("./components/PlotPES.vue"),
    //   },
    // ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes: routes,
});

export default router;