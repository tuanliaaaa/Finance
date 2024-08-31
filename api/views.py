from rest_framework.views import APIView
from entity.models import User,Human,Finance
from rest_framework.response import Response
import jwt
from finance.settings import SECRET_KEY
from datetime import datetime,timedelta,timezone
from django.views import View
from .response import CustomResponse
from finance.roleLoginDecorator import RoleRequest
from django.utils.decorators import method_decorator
import datetime
class Login(APIView):
    def post(self,request):
        exp=datetime.datetime.now(tz=timezone.utc) + timedelta(minutes=50)
        userRequestToken =request.data     
        if 'username' not in userRequestToken or not userRequestToken['username']:
            return Response({"message":"Vui lòng nhập username"},400)
        if 'password' not in userRequestToken or not userRequestToken['password']:
            return Response({"message":"Vui lòng nhập password"},400)
        users = User.objects.filter(username=userRequestToken['username'], password=userRequestToken['password'])
        if(len(users)==0):
           return Response({"message":"mật khẩu sai rồi thằng ngu"},400)
        user=users[0]
        payLoad = {'UserID':user.id,"UserName":user.username,"Role":user.role,"exp":exp}
        jwtData = jwt.encode(payLoad,SECRET_KEY,) 
        jwtUser={"access":jwtData}
        return Response(CustomResponse(200,"success",jwtUser).to_dict(),201)
class Humen(APIView):
    @method_decorator(RoleRequest(allowed_roles=['user',]))
    def get(self,request):
        user = User.objects.get(id=request.UserID)
        finances = Finance.objects.filter(user=user)
        humans = Human.objects.filter(id__in=finances.values('humanName'))
        humansJson=[]
        for human in humans:
            humansJson.append({"id":human.pk,"humanName":human.humanName})
        return Response({"status":200,"message":"success","data":humansJson,"time":datetime.datetime.now().isoformat()},200)
class Finances(APIView):
    @method_decorator(RoleRequest(allowed_roles=['user',]))
    def get(self,request):
        finances = Finance.objects.select_related('humanName').filter(user_id=request.UserID,status=request.GET.get('status'))
        
        # Tạo danh sách các đối tượng với thông tin Finance và Human
        financesJson = [
            {
                "id": finance.id,
                "humanName": finance.humanName.humanName,  # Thay đổi để lấy tên của Human
                "type": finance.type,
                "price": finance.price,
                "des": finance.des,
                "status": finance.status,
                "createAt": finance.createAt,
                "endAt": finance.endAt,
                "deadline": finance.deadline
            }
            for finance in finances
        ]

        # Trả về phản hồi
        return Response({
            "status": 200,
            "message": "success",
            "data": financesJson,
            "time": datetime.datetime.now().isoformat()
        }, status=200)


        