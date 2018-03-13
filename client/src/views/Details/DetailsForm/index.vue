<template id="Form">
  <div style="margin-left: 25%;padding: 40px;border: 1px red solid;width: 40%;background-color:#f5f5f5">
    <label style="font-size: 1.625rem /* 26/16 */;color: #ff7010" for="">为你查询到轮多少条数据</label>
    <div class='article' @click="Add">
      <label style="font-size: 20px" for="">文章名字</label>
      <button style="border-radius: 50px;padding: 2px;width: 37px;height: 21px;">状态</button>
      <p style="margin: 10px;">成都天府新区、成都高新区、各区（市）县工业和信息化主管部门、
        财政主管部门：为贯彻落实《关于印发贯彻〈创新要素供给培育产业
        生态提升国家中心城市产业能级若干政策措施的意见〉项目申报指南的通知》
        （成经信财〔2017〕89号）等文件精神，</p>
           <label for="">公开时间:张三</label>
            <label for="">申请人:2018-01-18</label>
            <label for="">申请时间:2018-01-18</label>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    name: "Form";
    return {
      name: "张三",
      apply_time: "2018-01-18",
      tite: "2018-01-18"
    };
  },
  methods: {
    Add(e, data) {
      console.log("1111");
      console.log(e);
      console.log(data);
    }
  },
  mounted() {}
};
</script>

<style>
.article {
  margin-top: 15px;
  padding: 15px;
  padding: 0px, 30%;
  background-color: #ffffff;
}
</style>
