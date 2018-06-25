$(document).ready(function(){
    $("form").submit(function(){
        var pwd = $("input[name='password']").val();
        var md5Pwd = md5(pwd);
        $("#pwd").val(md5Pwd);
    });
});