<template>
  <div class="webtitle">
    <nav>
      <ul class="topnav" id="dropdownClick">
        <li >
          <img
            alt="dbEssLnc"
            src="../../public/assets/img/title.svg"
            style="height: 65px; width: auto; vertical-align: bottom; margin-right: 10px;margin-left: 10px;margin-top: 5px;"
          />
        </li>
        <li
          :index="item.id"
          v-for="item in menus"
          v-on:click="setname(item.name)"
          :class="{ 'is-active': item.name == checkName }"
          :key="item.id"
        >    
           <router-link :to="item.url" @click="renew()"> 
             {{item.name}}
           </router-link>  
        </li> 
        <li>
          <a href="https://esslnc.pufengdu.org/v1/">
            <img
            alt="V1.0"
            src="../../public/assets/img/jump.svg"
            style="height: 28px; vertical-align: middle;"/>
            V1.0
          </a>
        </li>
        <li class="dropdownIcon">
          <a href="javascript:void(0);" @click="dropdownMenu()">&#9776;</a>
        </li>
      </ul>
    </nav>
    
  </div>
</template>

<script>
export default {
  name: "Header",
  inject:['reload'],
  data() {
    return {
      title: "dbEssLnc",
      menus: [
        {
          id: 1,
          url: "/home",
          name: "Home"
        },
        {
          id: 2,
          url: "/browse",
          name: "Browse"
        },
        {
          id: 3,
          url: "/search",
          name: "Search"
        },
        {
          id: 4,
          url: "/blast",
          name: "Blast"
        },
        {
          id: 5,
          url: "/download",
          name: "Download"
        },
        {
          id: 6,
          url: "/help",
          name: "Help"
        }

      ],
      checkName: this.$route.name
    };
  },
  methods: {
    setname(val) {
      this.checkName = val;

    },

    dropdownMenu() {
      let x = document.getElementById("dropdownClick");
      if (x.className === "topnav") {
        x.className += " responsive";
      
      } else {
        x.className = "topnav";
        
      }
    },
    renew(){
      this.reload()
    }
  },
  watch: {
  
    $route: {
      handler() {
        let linkName = this.$route.name;
        this.checkName = linkName;

      }
    }
  }
};
</script>

<style>

nav {
  display: block;
  width: 100%;
  margin: 0;
  height: 70px;
  background-color: rgb(250, 250, 250);

  background-size: 180px 70px;
}



ul.topnav {
  margin: 0;
  padding: 0;
  overflow: hidden;
}

ul.topnav li {
  float: left;
  color: rgb(115, 200, 200);
  /* height: 100%; */
}

ul.topnav li.title {
  padding: 0 30px;
  line-height: 70px;
  height: 70px;
}


ul.topnav li a {
  display: block;
  padding: 20px 15px;
  color: rgb(115, 200, 200);
  font-weight: bold;
  font-family: "Source Sans Pro", sans-serif !important;
  height: 30px;
  line-height: 30px;
  text-align: center;
  font-size: 1.3em;
}

ul.topnav li a:hover {
  background: lightgray;
}

ul.topnav li.dropdownIcon {
  display: none;
}

ul.topnav .is-active a {
  background: rgb(115, 200, 200);
  color: white;
}

@media screen and (max-width: 800px) {
  ul.topnav li:not(:nth-child(1)) {
    display: none;
  }

  ul.topnav li.dropdownIcon {
    display: block;
    float: right;
  }

  ul.topnav.responsive {
    position: relative;
    background-color: rgb(250, 250, 250);
    z-index: 999;
  }

  ul.topnav.responsive li {
    float: none;
    display: block;
  }

  ul.topnav.responsive li:not(:nth-child(9)) a {
    text-align: left;
    height: 0 !important;
    line-height: 0 !important;
    font-size: 1em !important;
  }

  ul.topnav.responsive li.dropdownIcon {
    position: absolute;
    top: 0;
    right: 0;
  }
}
</style>
