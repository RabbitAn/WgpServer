from tortoise import fields, models

class Role(models.Model):
    id = fields.UUIDField(pk=True);
    role_name = fields.CharField(max_length=50, unique=True);#角色名称
    description = fields.TextField(null=True,); # 角色描述
    created_at = fields.DatetimeField(auto_now_add=True);#创建时间
    updated_at = fields.DatetimeField(auto_now=True);#更新时间
    class Meta:
        table = "roles"

