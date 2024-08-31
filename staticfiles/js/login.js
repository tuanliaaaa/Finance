        
if (localStorage.getItem("Token") )
{
}   
function loginByEnter()
{
    if(event.keyCode==13)
    {
        login();
    }
}
function login()
{
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() 
    {
        var tokenResponseJson=xhttp.responseText
        var tokenResponse= JSON.parse(tokenResponseJson)
        if(xhttp.status==201)
        {
            localStorage.setItem("Token", tokenResponse.data.access);
            window.location='/ahihi';
            
        }
        else
        {
            document.getElementById("error").innerText=tokenResponse.data['message']
            document.getElementById("form__content__text__error").style="display:block"
        }
    }         
    const userInfo={
        username:document.getElementById("Username").value,
        password:document.getElementById("Password").value
    }
    postData=JSON.stringify(userInfo)
    xhttp.open("POST", "/api/v1/login",false);
    xhttp.setRequestHeader("Content-type","application/json")
    xhttp.send(postData)
}
