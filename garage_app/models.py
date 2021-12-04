from django.db import models
from django.urls import reverse


class Timestamp(models.Model):
    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True


class Ticket(Timestamp):
    # Relationships
    employee = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name='الموظف')

    # Fields

    # Owner Data
    car_owner_name = models.CharField(max_length=30, verbose_name='اسم المالك')
    owner_mobile_number = models.CharField(max_length=30, verbose_name='جوال المالك')
    national_identification_number = models.CharField(max_length=30, verbose_name='السجل المدني')
    driver_license_number = models.CharField(max_length=30, verbose_name='رقم الرخصة')

    # Car Data
    car_model_year = models.IntegerField(verbose_name='موديل السيارة')
    car_registration_no = models.CharField(max_length=30, verbose_name='رقم اللوحة')
    car_model_name = models.CharField(max_length=30, verbose_name='اسم الموديل')
    car_manufacturer = models.CharField(max_length=30, verbose_name='الشركة المصنعة')
    car_chassis_no = models.CharField(max_length=30, verbose_name='رقم الشاسيه')
    car_color = models.CharField(max_length=30, verbose_name='لون السيارة')

    # Other Data
    reservation_time_per_day = models.CharField(max_length=30, verbose_name='ايام الحجز')
    ticket_total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='اجمالي التذكرة')
    parking_price_per_day = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='سعر اليوم')
    completed = models.BooleanField(default=False, verbose_name='منتهية')
    position_number = models.CharField(max_length=10, verbose_name='رقم حارة الركن')
    qr_code = models.CharField(max_length=300, verbose_name='رمز رابط التذكرة')

    class Meta:
        pass

    def __str__(self):
        return str(self.car_owner_name)

    def get_absolute_url(self):
        return reverse("garage_app_Ticket_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("garage_app_Ticket_update", args=(self.pk,))
