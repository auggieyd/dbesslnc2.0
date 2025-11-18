//配置路由相关的信息
// import Vue from 'vue'
// import VueRouter from 'vue-router'
import {createRouter,createWebHistory } from 'vue-router'


const routerHistory = createWebHistory('/v2')
 
//2.创建VueRouter对象
const routes = [
    {
        path: "/:pathMatch(.*)*",
        redirect: "/home"
    },
    {
        path: "/home",
        name: 'Home',
        // 使用动态导入来实现懒加载
        component: () => import('../views/Home.vue') 
    },
    {
        path: "/browse",
        name: 'Browse',
        component: () => import('../views/Browse.vue')
    },
    {
        path: "/search",
        name: 'Search',
        component: () => import('../views/Search.vue')
    },
    {
        path: "/blast",
        name: 'Blast',
        component: () => import('../views/Blast.vue')
    },
    {
        path: "/download",
        name: 'Download',
        component: () => import('../views/Download.vue')
    },
    {
        path: "/help",
        name: 'Help',
        component: () => import('../views/Help.vue')
    },
    {
        path: "/visual",
        name: 'Visual',
        component: () => import('../views/Visual.vue')
    },
    {
        path: "/gene",
        name: 'Gene',
        component: () => import('../views/Gene.vue')
    }
];
const router =new createRouter({
    //配置路由和组件之间的应用关系
    history: routerHistory,
    routes

})
//3.将router对象传入到Vue实例中
export default router