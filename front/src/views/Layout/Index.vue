<template>
  <div class="layout-container">
    <el-menu
      :default-active="activeIndex2"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item index="1">首页</el-menu-item>
      <el-menu-item index="2">消息中心</el-menu-item>
      <el-menu-item index="3">个人中心</el-menu-item>
<!--      <el-menu-item index="4"><a href="https://www.ele.me" target="_blank">订单管理</a></el-menu-item>-->
    </el-menu>
    <Carousel></Carousel>
  </div>
</template>

<script>
  import Carousel from "./components/Carousel";
  export default {
    name: "LayoutIndex",
    components: {
      Carousel
    },
  }
</script>

<style scoped>

</style>