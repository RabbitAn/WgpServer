from tortoise import Model, fields
import uuid



class User(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4);
    username = fields.CharField(max_length=255, unique=True);
    role = fields.CharField(max_length=255);
    email = fields.CharField(max_length=255,null=True);#可为空
    password = fields.CharField(max_length=255);
    is_active = fields.BooleanField(default=True);
    created_at = fields.DatetimeField(auto_now_add=True);
    phone = fields.CharField(max_length=255, null=True);
    class Meta:
        table = "users";

    #TODO: 增加密码验证方法
    def check_password(self, password):
        return self.password == password;


