import {request} from "./request";
import {request2} from "./request";

//用户登录请求
export function login_user(user) {
    console.log('login_user')
    console.log(user)
    console.log(JSON.stringify(user))
    return request({
        url: '/user/login/',
        method: 'post',
        data: JSON.stringify(user),
        headers: {
            'Content-Type': 'application/json',
          },
    })
}

//用户退出登录请求
export function logout_user() {
    console.log('logout_user')
    return request({
        url: '/user/logout/',
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
            'token':window.localStorage.getItem('token'),
          },
    })
}

//管理员登录请求
export function login_admin(user_admin) {
    console.log('login_admin')
    return request({
        url: '/admin/login/',
        method: 'post',
        data: JSON.stringify(user_admin),
        headers: {
            'Content-Type': 'application/json',
        },
    })
}

//用户注册请求
export function register_user(registerData) {
    console.log('register')
    return request({
        url: '/user/register/',
        method: 'post',
        data: JSON.stringify(registerData),
        headers: {
            'Content-Type': 'application/json',
        },
    })
}

//模糊查找电影国家
export function getcountry(countryKey,limit) {
    console.log('getcountry')
    return request({
        url: '/country/',
        method: 'get',
        params:{
            countryKey: countryKey,
            limit:limit,
        }
    })
}

//模糊查找电影语言
export function getlanguage(languageKey,limit) {
    console.log('getlanguage')
    return request({
        url: '/language/',
        method: 'get',
        params:{
            languageKey: languageKey,
            limit:limit,
        }
    })
}

//添加电影
export function movieadd(movieData) {
    console.log('movieadd')
    return request({
        url: '/movie/',
        method: 'post',
        data: JSON.stringify(movieData),
        headers: {
            'Content-Type': 'application/json',
        },
    })
}

//添加类目
export function genreadd(genre) {
    console.log('genreadd')
    return request({
        url: '/genre/',
        method: 'post',
        data: JSON.stringify(genre),
        headers: {
            'Content-Type': 'application/json',
            'token':window.localStorage.getItem('token'),
        },
    })
}

//模糊搜索电影名
export function getmovie(movieNameKey,limit) {
    console.log('getmovie')
    return request({
        url: '/movie/',
        method: 'get',
        params:{
            movieNameKey: movieNameKey,
            limit:limit,
        },
        headers: {
            'token':window.localStorage.getItem('token'),
        },
    })
}

//模糊搜索类目
export function getgenre(genreKey,limit) {
    console.log('getgenre')
    return request({
        url: '/genre/',
        method: 'get',
        params:{
            genreKey: genreKey,
            limit:limit,
        },
        headers: {
            'token':window.localStorage.getItem('token'),
        },
    })
}


//添加电影到类目
export function movieaddgenre(movieaddgenreData) {
    console.log('movieaddgenre')
    return request({
        url: '/movieGenre/',
        method: 'post',
        data: JSON.stringify(movieaddgenreData),
        headers: {
            'Content-Type': 'application/json',
            'token':window.localStorage.getItem('token'),
        },
    })
}

//返回所有类目
export function getAllGenre() {
    console.log('getAllGenre')
    return request({
        url: '/genre/',
        method: 'get',
        headers: {
            'token':window.localStorage.getItem('token'),
        },
    })
}

//得到常见语言
export function getMostLanguage(limit) {
    console.log('getMostLanguage')
    return request({
        url: '/language/most/',
        method: 'get',
        params:{
            limit:limit,
        },
        headers: {
            'token':window.localStorage.getItem('token'),
        },
    })
}

//得到常见国家
export function getMostCountry(limit) {
    console.log('getMostCountry')
    return request({
        url: '/country/most/',
        method: 'get',
        params:{
            limit:limit,
        },
        headers: {
            'token':window.localStorage.getItem('token'),
        },
    })
}

//搜索电影
export function searchMovie(searchData) {
    console.log('searchMovie')
    return request({
        url: '/movie/page/',
        method: 'get',
        params:{
            current:searchData.current,
            size:searchData.size,
            movieNameKey:searchData.movieNameKey,
            countryName:searchData.countryName,
            genreName:searchData.genreName,
            languageIso:searchData.languageIso,
            year:searchData.year,
            rating:searchData.rating,
        },
        headers: {
            'token':window.localStorage.getItem('token'),
        },
    })
}

//高分热门电影
export function hotOrRatingMovie(current,size,status) {
    console.log('hotOrRatingMovie')
    return request({
        url: '/movie/page/',
        method: 'get',
        params:{
            current:current,
            size:size,
            status:status,
        },
        headers: {
            'token':window.localStorage.getItem('token'),
        },
    })
}

//电影详情页，获取电影数据
export function getMovieData(movieId) {
    console.log('getMovieData')
    return request({
        url: '/movie/'+movieId,
        method: 'get',
        headers: {
            'token':window.localStorage.getItem('token'),
        },
    })
}

//根据id查询用户
export function getUserData() {
    console.log('getUserData')
    return request({
        url: '/user/info',
        method: 'get',
        headers: {
            'token':window.localStorage.getItem('token'),
        },
    })
}

//根据用户id查询评分信息
export function getUserRatingData() {
    console.log('getUserRatingData')
    return request({
        url: '/ratings/',
        method: 'get',
        headers: {
            'token':window.localStorage.getItem('token'),
        },
    })
}

//修改密码
export function modifyPwd(pwdData) {
    console.log('modifyPwd')
    return request({
        url: '/user/modifyPwd',
        method: 'put',
        data: JSON.stringify(pwdData),
        headers: {
            'Content-Type': 'application/json',
            'token':window.localStorage.getItem('token'),
        },
    })
}

//查询用户对某个电影评分
export function searchUserMovieRating(movieId) {
    console.log('searchUserMovieRating')
    return request({
        url: '/ratings/'+movieId,
        method: 'get',
        headers: {
            'token':window.localStorage.getItem('token'),
        },
    })
}

//新增评分或修改评分
export function addOrModifyRating(ratingData) {
    console.log('addOrModifyRating')
    return request({
        url: '/ratings/',
        method: 'post',
        data: JSON.stringify(ratingData),
        headers: {
            'Content-Type': 'application/json',
            'token':window.localStorage.getItem('token'),
        },
    })
}

//调用推荐算法
export function callRecommendAlg(recommendData) {
    console.log('callRecommendAlg')
    return request2({
        url: '/recommend/',
        method: 'post',
        data: JSON.stringify(recommendData),
        headers: {
            'Content-Type': 'application/json',
            'token':window.localStorage.getItem('token'),
        },
    })
}