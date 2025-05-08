from django.db import models


class orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=100, default="")
    order_date = models.DateField()
    # phone_number = models.
    

    order_types = [
        ('Video', 'Video'),
        ("Graphics", "Graphics"),
        ('Web', 'Web'),
        ('Thumbnail', 'Thumbnail'),
        ('digital marketting', 'digital marketing'),
        ('Social media management', 'Social media management'),

    ]
    ordertype = models.CharField(name='ordertype', max_length=100, choices=order_types, default='Video')
    description = models.TextField(name='description',max_length=500,default="")

    def __str__(self):
        return f"Order {self.order_id} by {self.customer_name}"

class contact_us(models.Model):
    full_name = models.CharField(name='full_name', max_length=30, null=False, blank = False)
    email = models.EmailField(name='email')
    phone_number = models.IntegerField(name='phone_number')
    subject = models.CharField(name='subject', max_length=100)
    message = models.TextField(name='message')



# class video(models.Model):
#     title = models.CharField(name='title', max_length= 255)
#     videos = models.