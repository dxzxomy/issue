<template>
  <div class="news">
    <el-row class="news-container">
      <el-col :xs="24" :sm="24" :md="6">
        <div class="grid-content bg-purple" style="width: 15rem">
          <img src="@/assets/images/one.png" alt="" class="image_1">
          <span></span>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :md="8">
        <div class="grid-content bg-purple-light">
          <div>
            <p class="title" style="margin-top: 0; font-size: 15px;">工业大数据价值化是智能化制造的根本问题</p>
            <p style="color: rgb(152, 152, 152); font-size:14px;width: 85%">全球制造业战略当中，德国工业4.0、中国制造2025和美国的工业互联网这三个是最强的。美国代表了先进技术，德国代表了先进制造，中国制造的体量则是全球最大的...</p>

          </div>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :md="8">
        <div class="grid-content bg-purple-light">
          <el-card class="box-card">
            <div v-for="o in 7" :key="o" class="text item">
              {{'列表内容 ' + o }}
            </div>
          </el-card>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  export default {
    name: "News"
  }
</script>

<style scoped>
  .news{
    padding: 40px;
    background-color: #EEEEEE;
  }
.news-container {
  margin: 0 10%;
}
.image_1 {
  width: 15rem;
}
  p {
  text-align:justify;
}
</style>