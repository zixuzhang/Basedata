<template id="Middle">
  <div class='bob'>

    <div class='sos'>
      <label>文章推荐</label>
      <div class='articleConten'>
          <h4>文章标题</h4>
            <p class='recommended'>1991年，美国得克萨斯州维多市，34岁的离异女子Kathy 
              Page被人发现死在自己车里。据推断，她在死前遭受了殴打、勒颈和强奸。 经历了绝
              望的两年后，鉴于警方的低效之举，死者的父亲James Fulton开始在各类街边广告...</p>
      </div> 
      <div class='articleConten'>
          <h4>文章标题</h4>
            <p class='recommended'>1991年，美国得克萨斯州维多市，34岁的离异女子Kathy 
              Page被人发现死在自己车里。据推断，她在死前遭受了殴打、勒颈和强奸。 经历了绝
              望的两年后，鉴于警方的低效之举，死者的父亲James Fulton开始在各类街边广告...</p>
        </div> 
        <div class='articleConten'>
          <h4>文章标题</h4>
            <p class='recommended'>1991年，美国得克萨斯州维多市，34岁的离异女子Kathy 
              Page被人发现死在自己车里。据推断，她在死前遭受了殴打、勒颈和强奸。 经历了绝
              望的两年后，鉴于警方的低效之举，死者的父亲James Fulton开始在各类街边广告...</p>
        </div>
        <div class='articleConten'>
          <h4>文章标题</h4>
            <p class='recommended'>1991年，美国得克萨斯州维多市，34岁的离异女子Kathy 
            Page被人发现死在自己车里。据推断，她在死前遭受了殴打、勒颈和强奸。 经历了绝
            望的两年后，鉴于警方的低效之举，死者的父亲James Fulton开始在各类街边广告...</p>
        </div> 

        
    </div>

    <div class='niu'>
          <h1 class='Labelcolumn'>标签</h1>
       <div>
        <Button class='labelVersion' type="primary" shape="circle" size="small">Small</Button>
        <Button class='labelVersion' type="primary" shape="circle" size="small">Small</Button>
        <Button class='labelVersion' type="primary" shape="circle" size="small">Small</Button>
      </div>          
      <h1 class='Labelcolumn'>推荐文章附带的标签</h1>
       <div>
          <Button class='labelVersion' type="primary" shape="circle" size="small">Small</Button>
          <Button class='labelVersion' type="primary" shape="circle" size="small">Small</Button>
          <Button class='labelVersion' type="primary" shape="circle" size="small">Small</Button>
      </div> 
    </div>
 
  </div>
</template>
<style>
.bob {
  margin: 20px;
  margin-left: 500px;
}
.sos {
  padding: 15px;
  width: 30%;
  float: left;
  border: 1px red solid;
}
.sos > label {
  font-size: 25px;
  color: red;
}

.articleConten {
  margin-top: 15px;
  padding: 25px;
  background-color: #f8f8f8;
}

.recommended {
  padding-top: 15px;
  font-size: 13px;
}
.niu {
  width: 20%;
  float: left;
  border-width: 1px;
  border-style: solid;
  margin-left: 100px;
  padding: 15px;
}
.Labelcolumn {
  padding: 15px;
  font-size: 25px;
}
.labelVersion {
  margin: 5px;
}
.Buttom_div {
  width: 100%;
  line-height: 60px;
}
li {
  line-height: 60px;
  list-style: none;
  float: left;
}
label {
  margin-left: 20px;
}
img {
  float: right;
  padding: 6px;
}
</style>


<script>
export default {
  data() {
    return {
      msg: "123",
      value: ""
    };
  },
  methods: {
    layOut() {
      this.$router.push({ path: "/login" });
    },
    Add() {
      console.log("1111");
    }
  },
  mounted() {}
};
</script>

