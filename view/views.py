from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import jwt
import json
from finance.settings import SECRET_KEY
from datetime import datetime,timedelta,timezone
from rest_framework.decorators import APIView
from repository.UserRepo import UserRepo
from django.views import View
class Login(APIView):
    def post(self,request):
        exp=datetime.now(tz=timezone.utc) + timedelta(minutes=50)
        userRequestToken =request.data     
        if 'username' not in userRequestToken or not userRequestToken['username']:
            return Response({"message":"Vui lòng nhập username"},400)
        if 'password' not in userRequestToken or not userRequestToken['password']:
            return Response({"message":"Vui lòng nhập password"},400)
        try:
            users = UserRepo().find_by_key("username",userRequestToken['username'])
            print('d')
            if(len(users)>0):
                if(users[0]['password']!=userRequestToken['password']): return Response({"message":"mật khẩu sai rồi thằng ngu"},400)
        except:      
            return Response({"message":"User này không tồn tại"},403)
        user=users[0]
        payLoad = {'UserID':user['id'],"UserName":user['username'],"Role":user["role"],"exp":exp}
        jwtData = jwt.encode(payLoad,SECRET_KEY,) 
        jwtUser={"access":jwtData}
        return Response(jwtUser,201)
        
class L(View):
    def get(self,request):
        return render(request,'ok.html')