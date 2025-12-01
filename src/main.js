import {createApp} from 'vue'
import router from './router'
import 'element-plus/lib/theme-chalk/index.css'
import '@/styles/global.css' 
import axios from 'axios'
import App from './App.vue'



const app = createApp(App)
app.use(router)


app.config.globalProperties.$axios = axios
app.mount('#app')




