<template>
  <div class="about">
    <el-row  class="about-container" >
      <el-col :xs="24" :sm="24" :md="13">
        <div class="grid-content bg-purple">
          <h4>2019新型冠状病毒</h4>
          <p style="color: #989898">2019新型冠状病毒，2020年1月12日，世界卫生组织正式将其命名为2019-nCoV 。冠状病毒是一个大型病毒家族，已知可引起感冒以及中东呼吸综合征(MERS)和严重急性呼吸综合征(SARS)等较严重疾病。新型冠状病毒是以前从未在人体中发现的冠状病毒新毒株 。 2019年12月以来，湖北省武汉市持续开展流感及相关疾病监测，发现多起病毒性肺炎病例，均诊断为病毒性肺炎/肺部感染。 人感染了冠状病毒后常见体征有呼吸道症状、发热、咳嗽、气促和呼吸困难等。在较严重病例中，感染可导致肺炎、严重急性呼吸综合征、肾衰竭，甚至死亡。对于新型冠状病毒所致疾病没有特异治疗方法。但许多症状是可以处理的，因此需根据患者临床情况进行治</p>
          <p>>><a href="">了解更多</a></p>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :md="11">
        <div class="grid-content bg-purple-light" style="text-align: center">
            <img src="@/assets/images/one.png" alt="" class="image_1">
        </div>
      </el-col>
    </el-row>
  </div>

</template>

<script>
  export default {
    name: "About"
  }
</script>

<style scoped>
p {
  text-align:justify;
}
.about-container {
  margin: 0 10%;
}

  .image_1 {
    text-align: center;
    margin-top: 2rem;
    width:20rem;
  }
</style>