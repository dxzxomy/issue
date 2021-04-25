<template>
  <div class="about-detail">
    <div class="about-content">
      <div class="about-header">
      <h1>新型冠状病毒肺炎</h1>
      <h6 style="color: rgb(152, 152, 152)">新冠肺炎一般指新型冠状病毒肺炎</h6>
      <p>新型冠状病毒肺炎（Corona Virus Disease 2019，COVID-19），简称“新冠肺炎”，世界卫生组织命名为“2019冠状病毒病” [1-2]  ，是指2019新型冠状病毒感染导致的肺炎。2019年12月以来，湖北省武汉市部分医院陆续发现了多例有华南海鲜市场暴露史的不明原因肺炎病例，证实为2019新型冠状病毒感染引起的急性呼吸道传染病。 [3-6]
2020年2月11日，世界卫生组织总干事谭德塞在瑞士日内瓦宣布，将新型冠状病毒感染的肺炎命名为“COVID-19” [7]  。
      <p>2020年2月11日，世界卫生组织总干事谭德塞在瑞士日内瓦宣布，将新型冠状病毒感染的肺炎命名为“COVID-19” [7]  。2月22日，国家卫生健康委发布通知，“新型冠状病毒肺炎”英文名称修订为“COVID-19” [8]  。3月11日，世卫组织认为当前新冠肺炎疫情可被称为全球大流行 [9]  。4月4日，中国举行全国性哀悼活动 [10]  。8月18日，国家卫健委修订完成了新型冠状病毒肺炎诊疗方案（试行第八版） [11]  。9月3日，世卫组织新冠肺炎疫情应对评估专家组共同主席在成员国吹风会上宣布了专家组成员名单，钟南山入选。 [12]</p>
      <p>截至2021年2月20日24时，据31个省（自治区、直辖市）和新疆生产建设兵团报告，现有确诊病例423例（其中重症病例2例），累计治愈出院病例84772例，累计死亡病例4636例，累计报告确诊病例89831例，现有疑似病例3例。累计追踪到密切接触者976157人，尚在医学观察的密切接触者7929人。 [13]</p>
      <p>2021年3月30日，中国—世卫组织新冠病毒溯源联合研究报告在日内瓦发布。</p>
      <p>截至欧洲中部时间2021年4月2日18时23分，全球确诊病例较前一日增加659917例，达到129215179例；死亡病例增加11626例，达到2820098例。 [54]</p>
    </div>
      <div class="demo-image__placeholder">
        <div class="block"  v-for="src in srcs" :key="src">
          <el-image :src="src">
            <div slot="placeholder" class="image-slot">
              加载中<span class="dot">...</span>
            </div>
          </el-image>

        </div>
      </div>

    </div>
  </div>
</template>

<script>
  export default {
    name: "AboutDetailIndex",
    data() {
      return {
        // src: 'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg',
        srcs: [
          'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg',
          'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg',
          'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg',
          'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg',
          'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg',
          'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg',
        ],
      }
    }
  }
</script>

<style scoped>
  .demo-image__placeholder {
    display: flex;
  }
  .el-image {
    width: 90%;
  }
  .about-content {
    margin: 0 10%;
  }

  p {
    text-indent: 2em;
    text-align:justify;
}
</style>