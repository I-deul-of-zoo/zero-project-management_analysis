from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, login_id, password, **kwargs):
        user = self.model(
            login_id=login_id,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login_id=None, password=None, **extra_fields):
        superuser = self.create_user(
            login_id=login_id,
            password=password,
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser