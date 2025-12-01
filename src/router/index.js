
import {createRouter,createWebHistory } from 'vue-router'


const routerHistory = createWebHistory('/v2')

const routes = [
    {
        path: "/:pathMatch(.*)*",
        redirect: "/home"
    },
    {
        path: "/home",
        name: 'Home',
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

    history: routerHistory,
    routes

})

export default router