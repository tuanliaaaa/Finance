        
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
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Tìm cookie có tên "name"
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
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
            console.log(tokenResponse);
            localStorage.setItem("Token", tokenResponse.data.access);
            window.location='/ahihi';
            
        }
        else
        {
            console.log(tokenResponse);
            document.getElementById("error").innerText=tokenResponse.data['message']
            document.getElementById("form__content__text__error").style="display:block"
        }
    }         
    const userInfo={
        username:document.getElementById("Username").value,
        password:document.getElementById("Password").value
    }
    postData=JSON.stringify(userInfo)
    var csrftoken = getCookie('csrftoken');

    xhttp.open("POST", "/api/v1/login",false);
    xhttp.setRequestHeader("Content-type","application/json");
    xhttp.setRequestHeader('X-CSRFToken', csrftoken);
    xhttp.send(postData)
}
