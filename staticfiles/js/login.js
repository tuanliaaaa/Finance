        
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
        if(xhttp.status==200)
        {
            localStorage.setItem("Token", tokenResponse['access']);
            
        }
        else
        {
            document.getElementById("error").innerText=tokenResponse['message']
            document.getElementById("form__content__text__error").style="display:block"
        }
    }         
    const userInfo={
        Username:document.getElementById("username").value,
        Password:document.getElementById("password").value
    }
    postData=JSON.stringify(userInfo)
    xhttp.open("POST", "/api/v1/login",false);
    xhttp.setRequestHeader("Content-type","application/json")
    xhttp.setRequestHeader("X-CSRFToken", csrfToken);
    xhttp.send(postData)
}
