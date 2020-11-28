//ajax工具对象:1.兼容问题;2.便捷问题


function ajax(){
    //1.兼容性
    //检测XMLHttpRequest是否存在
    if(window.XMLHttpRequest){
        var xhr = new XMLHttpRequest();
    }else if(window.ActiveXObject){
        console.log('创建IE的xhr对象,此处省略')//遍历逐个试验
    }else{
        return false
    }
    //继续简化
    function check_use(callback) {
        xhr.onreadystatechange=function () {
            if(xhr.readyState === 4){
                //检测响应
                if(xhr.status === 200){
                    callback(xhr.responseText);
                }
            }
        };
    }

    //定义get
    function ajaxGet(url,callback) {
        //new 一个xhr对象,上面已经new过了
        //建立链接
        xhr.open('get',url);
        //发送数据
        xhr.send(null);
        //检测请求与响应
        check_use(callback);
    }

    function ajaxPost(url,data,callback) {
        //new 一个xhr对象,上面已经new过了
        //建立链接
        xhr.open('post',url);
        //设置post专用头信息
        xhr.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
        //发送数据
        xhr.send(data);
        //检测请求与响应
        check_use(callback);
    }

    //
    return{
        //ajax的功能对象
        get:ajaxGet,//实现ajax的get异步传输
        post:ajaxPost//实现ajax的post异步传输
    }
}

// //使用
// ajax();