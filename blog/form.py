from django import forms
import re
from blog.models import  Category


chenghu_error_set={
	'required':'亲爱的，请填写您的昵称',
	'max_length':'称呼太长咯！请修改至30字以内.',
}

email_error_set={
    'required':'亲爱的，请填写您的邮箱',
}

content_error_set={
	'required':'亲爱的，请填写您的评论内容!',
    'max_length':'评论内容太长咯',
}
class BlogForm(forms.Form):
    title = forms.CharField(required=True,label='博客标题', max_length=60)
    content = forms.CharField(required=False,label='博客内容',widget=forms.TextInput(),max_length=30000)
    category = forms.CharField(required=True,label='分类',max_length=30)
    def clean_category(self):
        category=self.cleaned_data['category']
        if category not in ["0","1","2","3","4","5","6","7"]:
            raise forms.ValidationError("请输入正确的标签号哦")
        return category
    #tag = forms.CharField(required=False,label='标签',max_length=30)
class CommentForm(forms.Form):
    name=forms.CharField(required=True,label='称呼',max_length=30,error_messages=chenghu_error_set)
    email=forms.EmailField(required=False,label='邮箱',error_messages=email_error_set)
    content = forms.CharField(required=True,label='内容',error_messages=content_error_set)
    def clean_email(self):
        email = self.cleaned_data['email']
        pattern = re.compile("^[0-9a-zA-Z]{1,19}@[0-9a-zA-Z]{1,13}\.(\d|\w)+$") # 设置正则验证
        if not pattern.match(email):
            raise forms.ValidationError("请输入正确的邮箱地址哟！")
              #msg = u"请输入正确的邮箱地址！"
              #self._errors["email"] = self.error_class([msg]) #设置输入框的告警文字
        return email

class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    def clean_username(self):
        username= self.cleaned_data['username']
        pattern = re.compile("^[0-9a-zA-Z]{1,20}$") # 设置正则验证
        if not pattern.match(username):
            raise forms.ValidationError("请输入正确的用户名哦！必须是字母和数字的组合！")
        elif len(username)>20:
            raise forms.ValidationError("请把名字控制在20字符以内哦！")
              #msg = u"请输入正确的邮箱地址！"
              #self._errors["email"] = self.error_class([msg]) #设置输入框的告警文字
        return username
    def clean_password(self):
        password= self.cleaned_data['password']
        pattern = re.compile("^[A-Z]{1,5}[0-9a-zA-Z]{1,13}$") # 设置正则验证
        if not pattern.match(password):
            raise forms.ValidationError("请输入正确的密码哦！首字母必须大写哦！")
        elif len(password)<8:
            raise forms.ValidationError("请输入至少8位字符哦！")
              #msg = u"请输入正确的邮箱地址！"
              #self._errors["email"] = self.error_class([msg]) #设置输入框的告警文字
        return password

