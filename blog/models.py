from django.db import models



class Category(models.Model):         #定义博客的类别
    name=models.CharField('名称',max_length=30)
    class Meta:
        verbose_name='类别'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name              #选择性显示博客所属类别名称

'''
class Tag(models.Model):              #定义博客的标签
    name = models.CharField('名称', max_length=30,unique = False)
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name              #选择性显示博客所属标签名称
'''

class User(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    class Meta:
        verbose_name='用户'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.username

class Blog(models.Model):             #定义博客主体属性
    title=models.CharField('博客标题', max_length=60)
    user=models.ForeignKey(User,verbose_name='用户',on_delete=models.CASCADE)
    content=models.TextField('内容',max_length=30000)
    pub_time=models.DateField('发布时间', auto_now_add=True)
    category=models.ForeignKey(Category,verbose_name='分类',on_delete=models.CASCADE)
    #tag=models.ManyToManyField(Tag,verbose_name='标签',default='')
    class Meta:
        verbose_name='博客'
        verbose_name_plural=verbose_name
    def __str__(self):
        return '%s'%(self.title)            #选择性显示博客名称

class Comment(models.Model):
    blog=models.ForeignKey(Blog,verbose_name='博客',on_delete=models.CASCADE)
    name=models.CharField('称呼',max_length=30)
    email=models.EmailField('邮箱')
    content=models.CharField('评论内容',max_length=300)
    pub=models.DateField('评论时间', auto_now_add=True)
    class Meta:
        verbose_name='评论'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.content

