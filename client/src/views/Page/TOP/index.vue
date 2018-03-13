<style>
li {
  list-style: none;
  float: left;
  line-height: 50px;
}

.Tops {
  width: 100%;
  height: 80px;
  padding: 10px;
}

.logo {
  margin-left: 150px;
}

.search_div_INP {
  margin-left: 250px;
}

.search_div_But2 {
  margin-left: 500px;
}
</style>
<template id="TOP">

    <!-- 头 -->
    <div>
        <!-- 头 -->
        <div class='Tops'>
            <ul>
                <li>
                    <img class='logo' src="../../4logo1.png" alt="" srcset="">
                </li>
                <li class='search'>
                    <div class='search_div'>
                        <Input    class='search_div_INP' v-model="value"  placeholder="EnterSomething..." style="width: 300px"></Input>
                        
                        <router-link to="/connect">
                        <Button to='/Form' id="search_div_But" v-on:click="search" type="primary" icon="ios-search">搜索</Button>
                        <p></p></router-link>
                        
                    </div>
                </li>
                <li class='private'>
                    <div>
                        <Button class='search_div_But2' type="warning"><Icon type="email-unread"></Icon>私人空间</Button>
                    </div>
                </li>
            </ul>
        </div>

        <!-- 中 -->
        <div>
                <h1 style="margin: 39px 27%;">最新动态</h1>
        </div>
    </div>




</template>
<script>
export default {
  name: "Top",
  data() {
    return {
      value: "请输入关键词"
    };
  },
  methods: {
    search: function(e) {
      console.log("111");
      console.log(e.data);
    }
  }
};
</script>