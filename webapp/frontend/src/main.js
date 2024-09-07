import { createApp } from "vue";
// import "./style.css";
import App from "./App.vue";
import router from "./router";

import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import * as ElementPlusIconsVue from "@element-plus/icons-vue";

import axios from "axios";

const app = createApp(App);

app.config.globalProperties.$axios = axios;

app.use(ElementPlus).use(router);

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component);
}

app.mount("#app");
