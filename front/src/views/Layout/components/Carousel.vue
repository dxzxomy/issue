<template>
  <div class="block">
    <el-carousel height="400px">
      <el-carousel-item v-for="item in srcs" :key="item.id">
<!--        <h3 class="small">{{ item }}</h3>-->
        <el-image :src="item.idViews" style="display: contents">
            <div slot="placeholder" class="image-slot">
              加载中<span class="dot">...</span>
            </div>
        </el-image>
      </el-carousel-item>

    </el-carousel>
  </div>
</template>

<script>
  export default {
    name: "Carousel",
    data() {
      return {
        srcs: [
          {id: 2, idViews: require('@/assets/images/index/header.jpg')},
          {id: 2, idViews: require('@/assets/images/index/header1.png')},
          {id: 3, idViews: require('@/assets/images/index/header2.png')},
          {id: 4, idViews: require('@/assets/images/index/header3.jpg')}
        ]
      }
    },
  }
</script>

<style scoped>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
     background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
     background-color: #d3dce6;
  }

</style>