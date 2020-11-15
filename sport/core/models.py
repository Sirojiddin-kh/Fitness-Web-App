from django.db import models


PROGRAMME = (
    ('Cardio', 'Cardio Classes'),
    ('Swimming', "Swimming Lesson"),
    ('Yoga', "Yoga Classes"),
    ("Aerobics", "Aerobics"),
    ("Zumba", "Zumba"),
    ('Massage', "Massage"),
    ("Body Building ", "Body Building")
)
PLANS = (
    ('Starter', 'Starter'),
    ('Basic', 'Basic'),
    ('Pro', 'Pro'),
    ('Unlimited', 'Unlimited')
)


class Menu(models.Model):
    order = models.IntegerField(null=True)
    name = models.CharField(max_length=40)
    link = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SportProgramme(models.Model):
    name = models.CharField(max_length=200, choices=PROGRAMME)
    long_descr= models.TextField(null=True)
    short_descr = models.TextField()
    img = models.ImageField(upload_to='programme') #Image of Programme
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FitnessExpert(models.Model):
    name = models.CharField(max_length=50) # Name of Expert
    status = models.CharField(max_length=50) #Rule of Expert
    img = models.ImageField(upload_to='expert') #Image of expert
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Gallary(models.Model):
    name = models.ForeignKey(SportProgramme, on_delete=models.CASCADE)
    description = models.TextField()
    img = models.ImageField(upload_to='gym')  #Image of Training
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.description}'


# class Price(models.Model):
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.tariff


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, null=True, choices=PLANS)
    price = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def traings(self):
        return Traings.objects.filter(category=self)

    def __str__(self):
        return self.name


class Traings(models.Model):
    category = models.ForeignKey(ServiceCategory, null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    participations = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.category}  | {self.name}'


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    img = models.ImageField(upload_to='category', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def blogs(self):
        return Blog.objects.filter(category=self)

    def __str__(self):
        return f'{self.name}'


class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)
    short_descr = models.CharField(max_length=200, null=True)
    full_descr = models.CharField(max_length=400, null=True)
    img = models.ImageField(upload_to='Personal')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.category}  {self.title}'


class Gratitude(models.Model):
    fullname = models.CharField(max_length=40)
    Sentance = models.TextField()
    via = models.CharField(max_length=50, null=True)
    img = models.ImageField(upload_to='circle', null=True)

    def __str__(self):
        return self.fullname


class UserName(models.Model):
    name = models.CharField(max_length=200, null = True)
    surname = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=200, null=True)
    subject = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    status = models.BooleanField(null=True, verbose_name="Ko'rildi")
    request_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

    def __str__(self):
        return f"{self.name} + {self.surname}"






