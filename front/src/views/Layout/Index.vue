<template>
  <div class="layout-container">
    <el-menu
      :default-active="activerouter"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      background-color="#545c64"
      text-color="#fff"
      router
      active-text-color="#ffd04b">
      <el-menu-item index="/">首页</el-menu-item>
      <el-menu-item index="/aboutdetail">关于病毒</el-menu-item>
      <el-menu-item index="3">实时检测</el-menu-item>
      <el-menu-item index="4">新闻咨询</el-menu-item>
      <el-menu-item index="5">视频资源</el-menu-item>
      <el-menu-item index="6">个人中心</el-menu-item>
<!--      <el-menu-item index="4"><a href="https://www.ele.me" target="_blank">订单管理</a></el-menu-item>-->
    </el-menu>
    <Carousel></Carousel>
    <router-view />
  </div>
</template>

<script>
  import Carousel from "./components/Carousel";
  export default {
    name: "LayoutIndex",
    components: {
      Carousel
    },
    data() {
      return {
        activerouter: this.$route.path
      }
    }
  }
</script>

<style scoped>

</style>