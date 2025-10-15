from tortoise import fields, models



class UserRole(models.Model):
    id = fields.UUIDField(pk=True);
    user = fields.ForeignKeyField("models.User", related_name="user_roles", on_delete=fields.CASCADE); # 用户外键
    role = fields.ForeignKeyField("models.Role", related_name="role_users", on_delete=fields.CASCADE); # 角色外键
    assigned_at = fields.DatetimeField(auto_now_add=True); # 分配时间

    class Meta:
        table = "user_roles"
