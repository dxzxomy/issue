
import axios from "axios";


const request = axios.create({
  baseURL: 'http://127.0.0.1:5000/'
});



// 请求拦截器

// request.interceptors.request.use(
//   function (config) {
//     const user = JSON.parse(window.localStorage.getItem('user'));
//     if(user) {
//       config.headers.Authorization = "JWT " + user.token
//     }
//     console.log("YYYY");
//     return config
//   },
//   function (error) {
//     console.log("NNNN");
//     return Promise.reject(error)
//
//   }
// );

//导出请求方法
export default request
