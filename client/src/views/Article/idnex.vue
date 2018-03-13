<template>
  <div>

      <div class="Artcle">
            <label>专利号</label>
            <h1 style="display: inline-block">专利详情名字</h1>
   <Tabs value="name1">
        <TabPane class='Tabpane' label="专利详细" name="name1">
            <ul>
                <li class="Tabpane_li">
                    <label for="">价值评估(USD)</label>
                </li>             
                <li class="Tabpane_li">
                    <label for="">无法获取估值</label>
                </li>             
                <li class="Tabpane_li">
                    <label for=""></label>
                </li>             
                <li class="Tabpane_li">
                    <label for=""></label>
                </li>
            </ul>
        </TabPane>
        <TabPane :label="label" name="name2">标签二的内容</TabPane>
        <TabPane label="同族专利" name="name3">标签三的内容</TabPane>
        <TabPane label="法律信息" name="name3">标签三的内容</TabPane>
    </Tabs>
      </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      label: h => {
        return h("div", [
          h("span", "引用信息"),
          h("Badge", {
            props: {
              count: 3
            }
          })
        ]);
      },
      name: "2017-07-28",
      age: "吉林省长春市东南湖大路3888号",
      age1:
        "CHANGCHUN INST OF OPTICS, FINE MECHANICS & PHYSICS - CHINESE ACAD OF SCI"
    };
  }
};
</script>

<style>
.Artcle {
  margin: 0 15%;
}
.Artcle > ul {
  border: 1px red solid;
}
.Tabpane {
  border: 1px red solid;
}
.Tabpane_li {
  width: 20%;
  margin: 5px;
}
</style>
