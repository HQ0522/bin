from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# User数据表
class User(AbstractUser):
    realname = models.CharField('真实姓名', max_length=16,null = False, blank = False)
    email = models.EmailField('用户邮箱', unique = True, null = False, blank = False)
    phone = models.CharField('电话号码',max_length=24,unique = True,null = False, blank = False)

    def __str__(self):
        return self.username

# Course数据表
class Course(models.Model):
    title = models.CharField('课程标题',max_length=200, null = False,  blank = False)
    tag = models.CharField('课程标签', max_length=50, null=False, blank=False)
    description = models.TextField('课程描述')
    source = models.CharField('课程来源', max_length=100, null=False, blank=False)
    href = models.URLField('课程链接', unique = True,null = False,  blank = False)
    imgurl = models.URLField('图片链接', unique = True,null = False,  blank = False)


from django.db.models import Avg
# Rating数据表
class Rating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    mark = models.DecimalField('课程评分',max_digits=3, decimal_places=1)
    create_time = models.DateTimeField(verbose_name="发布时间", auto_now_add=True)

# Collection数据表
class Collection(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# Comment数据表
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('用户评论')
    created_time = models.DateTimeField(auto_now_add=True)

# Course_statistic数据表
class Course_statistic(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, primary_key=True)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    num_of_collection = models.IntegerField(null=True, blank=True)