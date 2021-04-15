<template>
  <div class="test">
<!--        <el-button type="text" @click="centerDialogVisible = true">点击打开 Dialog</el-button>-->

<!--      <el-dialog-->
<!--        title="提示"-->
<!--        :visible.sync="centerDialogVisible"-->
<!--        width="30%"-->
<!--        center>-->
<!--        <span>需要注意的是内容是默认不居中的</span>-->
<!--        <span slot="footer" class="dialog-footer">-->
<!--          <el-button @click="centerDialogVisible = false">取 消</el-button>-->
<!--          <el-button type="primary" @click="centerDialogVisible = false">确 定</el-button>-->
<!--        </span>-->
<!--      </el-dialog>-->
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="活动名称">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
    <el-form-item>
    <el-button type="primary" @click="onSubmit">立即创建</el-button>
    <el-button>取消</el-button>
  </el-form-item>
</el-form>



  </div>
</template>

<script>
  export default {
    name: "TestIndex",
    data() {
      return {
        form: {
          node: ''
        }
      };
    },


  }
</script>

<style scoped>

</style>