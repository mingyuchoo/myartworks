from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Basic(models.Model):
    """
    Basic class
    """
    writer = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, )
    full_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return "{}:{}".format(self.pk, self.full_name)

    def get_absolute_url(self):
        return reverse('resume:index')


class Contact(models.Model):
    """
    Contact class
    """
    writer = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, )
    email = models.CharField(max_length=50)
    phone1 = models.CharField(max_length=50)
    phone2 = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
       pass

    def __str__(self):
        return "{}: {}".format(self.pk, self.email)

    def get_absolute_url(self):
        return reverse('resume:index')


class Letter(models.Model):
    """
    Letter class
    """
    writer = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, )
    content = models.CharField(max_length=10000)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return "{}: {}".format(self.writer.pk, self.writer.username)

    def get_absolute_url(self):
        return reverse('resume:index')


class Career(models.Model):
    """
    Career class
    """
    company = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    details = models.CharField(max_length=5000)
    writer = models.ForeignKey(User, related_name='resume_careers', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return "{}: {}".format(self.pk, self.company)

    def get_absolute_url(self):
        return reverse('resume:index')


class Education(models.Model):
    """
    Education class
    """
    school = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    details = models.CharField(max_length=5000)
    writer = models.ForeignKey(User, related_name='resume_educations', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return "{}: {}".format(self.pk, self.school)

    def get_absolute_url(self):
        return reverse('resume:index')


class Award(models.Model):
    """
    Award class
    """
    title = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    writer = models.ForeignKey(User, related_name='resume_awards', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return "{}: {}".format(self.pk, self.title)

    def get_absolute_url(self):
        return reverse('resume:index')


class Certificate(models.Model):
    """
    Certificate class
    """
    title = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    acquisition_date = models.DateField()
    writer = models.ForeignKey(User, related_name='resume_certificates', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return "{}: {}".format(self.pk, self.title)

    def get_absolute_url(self):
        return reverse('resume:index')


class Language(models.Model):
    """
    Language class
    """
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    writer = models.ForeignKey(User, related_name='resume_languages', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return "{}: {}".format(self.pk, self.name)

    def get_absolute_url(self):
        return reverse('resume:index')


class Skill(models.Model):
    """
    Skill class
    """
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    writer = models.ForeignKey(User, related_name='resume_skills', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return "{}: {}".format(self.pk, self.name)

    def get_absolute_url(self):
        return reverse('resume:index')

