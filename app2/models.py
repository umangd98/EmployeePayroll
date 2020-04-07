from django.db import models

class MainDept(models.Model):
    DEPT_NO = models.IntegerField(default=None, blank=True,primary_key=True)
    DEPT_NAME = models.CharField(max_length=20,null=True, blank=True)
    SDEPT = models.CharField(max_length=10,null=True, blank=True)
    class Meta:
        db_table = "DEPARTMENT"

class SubDept(models.Model):
    SUBDEPT_NO = models.IntegerField(default=None, blank=True,primary_key=True)
    SUBDEPT_NAME = models.CharField(max_length=20,null=True, blank=True)
    SUBDEPT = models.CharField(max_length=10,null=True, blank=True)
    DEPT_NO = models.ForeignKey(MainDept,default=1,on_delete=models.CASCADE)
    class Meta:
        db_table = "SUBDEPT"

class MainDesignation(models.Model):
    DESIG_NAME = models.CharField(default=None,max_length=50,blank=True,primary_key=True)
    SDESIG = models.CharField(max_length=10,null=True, blank=True)
    def __str__(self):
        return self.DESIG_NAME

    class Meta:
        db_table = "DESIGNATION"

class SubDesignation(models.Model):
    SUBDESIG_NO = models.IntegerField(default=None, blank=True,primary_key=True)
    SUBDESIG_NAME = models.CharField(max_length=50,null=True, blank=True)
    SUBDESIG = models.CharField(max_length=8,null=True, blank=True)
    DESIG_NAME = models.ForeignKey(MainDesignation,default=1,on_delete=models.CASCADE)
    class Meta:
        db_table = "SUBDESIG"

class Scale(models.Model):
    SCALE_NO = models.IntegerField(default=None, blank=True,primary_key=True)
    B1 = models.IntegerField(default=None,null=True, blank=True)
    l1= models.IntegerField(default=None,null=True, blank=True)
    B2 = models.IntegerField(default=None,null=True, blank=True)
    l2 = models.IntegerField(default=None,null=True, blank=True)
    B3 = models.IntegerField(default=None,null=True, blank=True)
    l3 = models.IntegerField(default=None,null=True, blank=True)
    B4 = models.IntegerField(default=None,null=True, blank=True)
    l4 = models.IntegerField(default=None,null=True, blank=True)
    SCALE_NAME = models.CharField(max_length=100,null=True, blank=True)
    l5 = models.IntegerField(default=None,null=True, blank=True)
    DETAIL = models.CharField(max_length=200,null=True, blank=True)
    GRDPAY = models.IntegerField(default=None,null=True, blank=True)
    PAYBAND = models.CharField(max_length=60,null=True, blank=True)
    TA = models.IntegerField(default=None,null=True, blank=True)
    class Meta:
        db_table = "SCALE"

class Staff(models.Model):
    STAFF_NO = models.IntegerField(default=None,blank=True,primary_key=True)
    STAFF_NAME = models.CharField(max_length=40,null=True, blank=True)
    class Meta:
        db_table = "STAFF"


class Caste(models.Model):
    CASTE_NO = models.IntegerField(default=None, blank=True,primary_key=True)
    CASTE_NAME = models.CharField(max_length=20,null=True, blank=True)
    class Meta:
        db_table = "CASTE"

class Category(models.Model):
    CATEGORY_NO = models.IntegerField(default=None, blank=True,primary_key=True)
    CATEGORY_NAME = models.CharField(max_length=20,null=True, blank=True)
    class Meta:
        db_table = "CATEGORY"

class Religion(models.Model):
    RELIGION_NO = models.IntegerField(default=None, blank=True,primary_key=True)
    RELIGION_NAME = models.CharField(max_length=20,null=True, blank=True)
    class Meta:
        db_table = "RELIGION"


class Appointment(models.Model):
    APPOINT_NO = models.IntegerField(default=None, blank=True,primary_key=True)
    APPOINT_NAME = models.CharField(max_length=25,null=True, blank=True)
    l1 = models.IntegerField(default=None,null=True, blank=True)
    l2 = models.IntegerField(default=None,null=True, blank=True)
    l3 = models.IntegerField(default=None,null=True, blank=True)
    l4 = models.IntegerField(default=None,null=True, blank=True)
    l5 = models.IntegerField(default=None,null=True, blank=True)
    l6 = models.IntegerField(default=None,null=True, blank=True)
    l7 = models.IntegerField(default=None,null=True, blank=True)
    l8 = models.IntegerField(default=None,null=True, blank=True)
    l9 = models.IntegerField(default=None,null=True, blank=True)
    l10 = models.IntegerField(default=None,null=True, blank=True)
    l11 = models.IntegerField(default=None,null=True, blank=True)
    l12 = models.IntegerField(default=None,null=True, blank=True)
    l13 = models.IntegerField(default=None,null=True, blank=True)
    l14 = models.IntegerField(default=None,null=True, blank=True)
    l15 = models.IntegerField(default=None,null=True, blank=True)
    D1 = models.IntegerField(default=None,null=True, blank=True)
    D2 = models.IntegerField(default=None,null=True, blank=True)
    D3 = models.IntegerField(default=None,null=True, blank=True)
    D4 = models.IntegerField(default=None,null=True, blank=True)
    D5 = models.IntegerField(default=None,null=True, blank=True)
    D6 = models.IntegerField(default=None,null=True, blank=True)
    D7 = models.IntegerField(default=None,null=True, blank=True)
    D8 = models.IntegerField(default=None,null=True, blank=True)
    D9 = models.IntegerField(default=None,null=True, blank=True)
    D10 = models.IntegerField(default=None,null=True, blank=True)
    D11 = models.IntegerField(default=None,null=True, blank=True)
    D12 = models.IntegerField(default=None,null=True, blank=True)
    D13 = models.IntegerField(default=None,null=True, blank=True)
    D14 = models.IntegerField(default=None,null=True, blank=True)
    D15 = models.IntegerField(default=None,null=True, blank=True)
    D16 = models.IntegerField(default=None,null=True, blank=True)
    D17 = models.IntegerField(default=None,null=True, blank=True)
    D18 = models.IntegerField(default=None,null=True, blank=True)
    D19 = models.IntegerField(default=None,null=True, blank=True)
    D20 = models.IntegerField(default=None,null=True, blank=True)
    D21 = models.IntegerField(default=None,null=True, blank=True)
    D22 = models.IntegerField(default=None,null=True, blank=True)
    D23 = models.IntegerField(default=None,null=True, blank=True)
    D24 = models.IntegerField(default=None,null=True, blank=True)
    D25 = models.IntegerField(default=None,null=True, blank=True)
    D26 = models.IntegerField(default=None,null=True, blank=True)
    D27 = models.IntegerField(default=None,null=True, blank=True)
    D28 = models.IntegerField(default=None,null=True, blank=True)
    D29 = models.IntegerField(default=None,null=True, blank=True)
    D30 = models.IntegerField(default=None,null=True, blank=True)

    class Meta:
        db_table = "APPOINT"


class SuplHead(models.Model):
    SUPLNO = models.IntegerField(default=None, blank=True,primary_key=True)
    SUPLHEAD_NAME = models.CharField(max_length=30,null=True, blank=True)
    class Meta:
        db_table = "SUPLHEAD"

class Bank(models.Model):
    BNO = models.IntegerField(default=None, blank=True,primary_key=True)
    BSNAME = models.CharField(max_length=10,null=True, blank=True)
    BNAME = models.CharField(max_length=50,null=True, blank=True)
    LOCATION = models.CharField(max_length=35,null=True, blank=True)
    BANKNO = models.IntegerField(default=None,null=True, blank=True)

    class Meta:
        db_table = "BANK"

class City(models.Model):
    CITY_NO = models.IntegerField(default=None, blank=True,primary_key=True)
    CITY_NAME = models.CharField(max_length=25,null=True, blank=True)
    class Meta:
        db_table = "CITY"

class Title(models.Model):
    TITLE_NO = models.IntegerField(default=None, blank=True,primary_key=True)
    TITLE_NAME = models.CharField(max_length=20,null=True, blank=True)
    class Meta:
        db_table = "TITLE"

class TypeTran(models.Model):
    TYPETRAN_NO = models.IntegerField(default=None, blank=True,primary_key=True)
    TYPETRAN_NAME = models.CharField(max_length=20,null=True, blank=True)
    class Meta:
        db_table = "TYPETRAN"

# class NatureDesignation(models.Model):
    #CREATE NEW TABLE
class UnderCollege(models.Model):
    UNO = models.IntegerField(default=None, blank=True,primary_key=True)
    UGPG_NAME = models.CharField(max_length=20,null=True, blank=True)
    LUGPG = models.CharField(max_length=50,null=True, blank=True)

    class Meta:
        db_table = "UGPG"


# class Loan(models.Model):
#     #CREATE NEW TABLE

class StaffType(models.Model):
    STNO = models.IntegerField(default=None, blank=True,primary_key=True)
    STAFF_TYPE = models.CharField(max_length=20,null=True, blank=True)
    class Meta:
        db_table = "STAFFTYPE"

class InstallmentType(models.Model):
    INO = models.IntegerField(default=None, blank=True,primary_key=True)
    IDNO = models.IntegerField(default=None,null=True, blank=True)
    PAYHEAD = models.CharField(max_length=3,null=True, blank=True)
    MONAMT = models.IntegerField(default=None,null=True, blank=True)
    INSTALNO = models.IntegerField(default=None,null=True, blank=True)
    TOTAMT = models.IntegerField(default=None,null=True, blank=True)
    REM = models.CharField(max_length=200,null=True, blank=True)
    STOP = models.IntegerField(default=None,null=True, blank=True)
    EXPDT = models.DateTimeField(auto_now_add=True)
    PAIDNO = models.IntegerField(default=None,null=True, blank=True)
    MON = models.CharField(max_length=7,null=True, blank=True)
    NEW = models.IntegerField(default=None,null=True, blank=True)
    REF_NO = models.CharField(max_length=35,null=True, blank=True)
    DESP_NO = models.CharField(max_length=35,null=True, blank=True)
    DESP_DT  = models.DateTimeField(auto_now_add=True)
    START_DT = models.DateTimeField(auto_now_add=True)
    DEFA_AMT = models.IntegerField(default=None,null=True, blank=True)
    PRO_AMT = models.IntegerField(default=None,null=True, blank=True)
    CODE = models.CharField(max_length=20,null=True, blank=True)
    IBNO = models.IntegerField(default=None,null=True, blank=True)
    MONYEAR = models.CharField(max_length=30,null=True, blank=True)
    STOP1 = models.IntegerField(default=None,null=True, blank=True)
    BAL_AMT = models.IntegerField(default=None,null=True, blank=True)
    REGULAR = models.IntegerField(default=None,null=True, blank=True)
    LTNO = models.IntegerField(default=None,null=True, blank=True)

    class Meta:
        db_table = "INSTALLMENT"

class Designature(models.Model):
    DESIGNATURE_NO = models.IntegerField(default=None, blank=True,primary_key=True)
    DESIGNATURE_NAME = models.CharField(max_length=20,null=True, blank=True)
    class Meta:
        db_table = "DESIGNATURE"
