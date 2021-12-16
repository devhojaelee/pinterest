from django.contrib.auth.forms import UserCreationForm


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True

# 간단히 설명하면, self.fields~ 문장이 없으면 Creation이랑 Update랑 똑같아
# 그런데 저게 있음으로써 달라지거든?
# 초기화 이후에 저 값을 딱 바꿔주는거야.
# 일케하면 혹시라도 브라우저에서 이전 캐시에 남아있던 값이 넘어가도, disabled 되어있어서 반영 안됨.