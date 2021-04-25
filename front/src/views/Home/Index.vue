<template>
  <div class="home-container">
    <About></About>
    <News></News>
    <Video></Video>
  </div>
</template>

<script>
  import About from "./components/About";
  import News from "./components/News";
  import Video from "./components/Video";
  export default {
    name: "HomeIndex",
    components: {
      Video,
      News,
      About
    },
    data() {
      return {};
    },
    methods: {},
  }
</script>

<style scoped>

</style>
