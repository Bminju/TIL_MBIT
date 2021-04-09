from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=50)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name  #클래스를 대표하는 문자열을 name으로 설정하겠다. 매직 method

class Question(models.Model):
    number = models.IntegerField(unique=True)
    content = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.number}. {self.content}'
class Choice(models.Model):
    content = models.CharField(max_length=100)
    question = models.ForeignKey(to='main.Question', on_delete=models.CASCADE) # ~model과 연결. on_delete = 연결된 model이 지워지면 함께 지워지는 옵션
    developer = models.ForeignKey(to='main.Developer',on_delete=models.CASCADE, null=True) #null > db가 비워있어도 됨. blank > 사용자가 입력할 때 비여있어도 됨

    def __str__(self):
        return self.content