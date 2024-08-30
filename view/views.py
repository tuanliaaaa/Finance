from django.shortcuts import render
from rest_framework.views import APIView
from entity.models import User
from rest_framework.response import Response
import jwt
from finance.settings import SECRET_KEY
from datetime import datetime,timedelta,timezone
from django.views import View
from .response import CustomResponse
class Login(APIView):
    def post(self,request):
        exp=datetime.now(tz=timezone.utc) + timedelta(minutes=50)
        userRequestToken =request.data     
        if 'username' not in userRequestToken or not userRequestToken['username']:
            return Response({"message":"Vui lòng nhập username"},400)
        if 'password' not in userRequestToken or not userRequestToken['password']:
            return Response({"message":"Vui lòng nhập password"},400)
        users = User.objects.filter(username=userRequestToken['username'], password=userRequestToken['password'])
        if(len(users)==0):
           return Response({"message":"mật khẩu sai rồi thằng ngu"},400)
        user=users[0]
        payLoad = {'UserID':user['id'],"UserName":user['username'],"Role":user["role"],"exp":exp}
        jwtData = jwt.encode(payLoad,SECRET_KEY,) 
        jwtUser={"access":jwtData}
        return Response(CustomResponse(200,"succes",jwtUser),201)
        
class L(View):
    def get(self,request):
        return render(request,'ok.html')