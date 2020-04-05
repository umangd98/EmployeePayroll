from django.db import models
from django.core.validators import RegexValidator

class MainDept(models.Model):   #field of table main dept
    DEPT_NO = models.IntegerField(default=None,null=True, blank=True)   #dept no
    DEPT_NAME = models.CharField(max_length=20,null=True, blank=True)   #dept name
    SDEPT = models.CharField(max_length=10,null=True, blank=True)   #sub dept
    class Meta:
        db_table = "DEPARTMENT"

class SubDept(models.Model):    #field of table sub dept
    SUBDEPT_NO = models.IntegerField(default=None,null=True, blank=True)    #sub dept no
    SUBDEPT_NAME = models.CharField(max_length=20,null=True, blank=True)    #sub dept name
    SUBDEPT = models.CharField(max_length=10,null=True, blank=True) #sub dept
    DEPT_NO = models.IntegerField(default=None,null=True, blank=True)   # dept no
    class Meta:
        db_table = "SUBDEPT"

class MainDesignation(models.Model):     #field of table main design
    DESIG_NO = models.IntegerField(default=None,null=True, blank=True)  #design no
    DESIG_NAME = models.CharField(max_length=50,null=True, blank=True)  #design name
    SDESIG = models.CharField(max_length=10,null=True, blank=True)  #sub design
    class Meta:
        db_table = "DESIGNATION"

class SubDesignation(models.Model):  #field of table  sub design
    SUBDESIG_NO = models.IntegerField(default=None,null=True, blank=True)   #no
    SUBDESIG_NAME = models.CharField(max_length=50,null=True, blank=True)   #name
    SUBDESIG = models.CharField(max_length=8,null=True, blank=True) #sub design
    DESIG_NO = models.IntegerField(default=None,null=True, blank=True)  #design no
    class Meta:
        db_table = "SUBDESIG"

class Scale(models.Model):  # #field of table scale
    SCALE_NO = models.IntegerField(default=None,null=True, blank=True)
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

class Staff(models.Model):  #fields of table scale
    STAFF_NO = models.IntegerField(default=None,null=True, blank=True)
    STAFF_NAME = models.CharField(max_length=40,null=True, blank=True)
    class Meta:
        db_table = "STAFF"


class Caste(models.Model):  #fields of table caste
    CASTE_NO = models.IntegerField(default=None,null=True, blank=True)  #no
    CASTE_NAME = models.CharField(max_length=20,null=True, blank=True)  #name
    class Meta:
        db_table = "CASTE"

class Category(models.Model):   #fields of table category
    CATEGORY_NO = models.IntegerField(default=None,null=True, blank=True)   #no
    CATEGORY_NAME = models.CharField(max_length=20,null=True, blank=True)   #name
    class Meta:
        db_table = "CATEGORY"

class Religion(models.Model):   #fields of table religion
    RELIGION_NO = models.IntegerField(default=None,null=True, blank=True)   #no
    RELIGION_NAME = models.CharField(max_length=20,null=True, blank=True)   #name
    class Meta:
        db_table = "RELIGION"


class Appointment(models.Model):    #fields of table appointment
    APPOINT_NO = models.IntegerField(default=None,null=True, blank=True)
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


class SuplHead(models.Model):   #fields of table suppl head
    SUPLNO = models.IntegerField(default=None,null=True, blank=True)    #no
    SUPLHEAD_NAME = models.CharField(max_length=30,null=True, blank=True)   #name
    class Meta:
        db_table = "SUPLHEAD"

class Bank: #fields of table bank   
    BNO = models.IntegerField(default=None,null=True, blank=True)   #no
    BSNAME = models.CharField(max_length=10,null=True, blank=True)  #name
    BNAME = models.CharField(max_length=50,null=True, blank=True)
    LOCATION = models.CharField(max_length=35,null=True, blank=True)
    BANKNO = models.IntegerField(default=None,null=True, blank=True)

    class Meta:
        db_table = "BANK"

class City: # fields of table city
    CITY_NO = models.IntegerField(default=None,null=True, blank=True)   #no
    CITY_NAME = models.CharField(max_length=25,null=True, blank=True)   #name
    class Meta:
        db_table = "CITY"

class Title(models.Model):   # fields of table title
    TITLE_NO = models.IntegerField(default=None,null=True, blank=True)  #no
    TITLE_NAME = models.CharField(max_length=20,null=True, blank=True)  #name
    class Meta:
        db_table = "TITLE"

class TypeTran(models.Model):    # fields of table typetran
    TYPETRAN_NO = models.IntegerField(default=None,null=True, blank=True)   #no
    TYPETRAN_NAME = models.CharField(max_length=20,null=True, blank=True)       #name
    class Meta:
        db_table = "TYPETRAN"

# class NatureDesignation(models.Model):
    #CREATE NEW TABLE
class UnderCollege(models.Model):    # fields of table under college
    UNO = models.IntegerField(default=None,null=True, blank=True)
    UGPG_NAME = models.CharField(max_length=20,null=True, blank=True)
    LUGPG = models.CharField(max_length=50,null=True, blank=True)

    class Meta:
        db_table = "UGPG"


# class Loan(models.Model):
#     #CREATE NEW TABLE

class StaffType(models.Model):  #fields of table stafftype
    STNO = models.IntegerField(default=None,null=True, blank=True)  #no
    STAFF_TYPE = models.CharField(max_length=20,null=True, blank=True)  #staff type
    class Meta:
        db_table = "STAFFTYPE"

class InstallmentType(models.Model):    #fields of table installmenttype
    INO = models.IntegerField(default=None,null=True, blank=True)
    IDNO = models.IntegerField(default=None,null=True, blank=True)
    PAYHEAD = models.CharField(max_length=3,null=True, blank=True)
    MONAMT = models.IntegerField(default=None,null=True, blank=True)
    INSTALNO = models.IntegerField(default=None,null=True, blank=True)
    TOTAMT = models.IntegerField(default=None,null=True, blank=True)
    REM = models.CharField(max_length=200,null=True, blank=True)
    STOP = models.IntegerField(default=None,null=True, blank=True)
    # EXPDT = #Date
    PAIDNO = models.IntegerField(default=None,null=True, blank=True)
    MON = models.CharField(max_length=7,null=True, blank=True)
    NEW = models.IntegerField(default=None,null=True, blank=True)
    REF_NO = models.CharField(max_length=35,null=True, blank=True)
    DESP_NO = models.CharField(max_length=35,null=True, blank=True)
    # DESP_DT = #Date
    # START_DT = #Date
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

class Designature(models.Model):    # fields of table designature
    DESIGNATURE_NO = models.IntegerField(default=None,null=True, blank=True)    #no
    DESIGNATURE_NAME = models.CharField(max_length=20,null=True, blank=True)    #name
    class Meta:
        db_table = "DESIGNATURE"
    # PER = models.IntegerField(default=None,null=True, blank=True)
    # FIXAMT = models.IntegerField(default=None,null=True, blank=True)
    # T_RANGE = models.IntegerField(default=None,null=True, blank=True)
    # F_RANGE = models.IntegerField(default=None,null=True, blank=True)
    # ITNO = models.IntegerField(default=None,null=True, blank=True)
    # LTNO = models.IntegerField(default=None,null=True, blank=True)
    # REGULAR = models.IntegerField(default=None,null=True, blank=True)
    # BAL_AMT = models.IntegerField(default=None,null=True, blank=True)
    # STOP1 = models.IntegerField(default=None,null=True, blank=True)
    # IBNO = models.IntegerField(default=None,null=True, blank=True)
    # PRO_AMT = models.IntegerField(default=None,null=True, blank=True)
    # PRO_AMT = models.IntegerField(default=None,null=True, blank=True)
    # DEFA_AMT = models.IntegerField(default=None,null=True, blank=True)
    # NEW = models.IntegerField(default=None,null=True, blank=True)
    # PAID_NO = models.IntegerField(default=None,null=True, blank=True)
    # STOP = models.IntegerField(default=None,null=True, blank=True)
    # NEW = models.IntegerField(default=None,null=True, blank=True)
    # TOTALAMT = models.IntegerField(default=None,null=True, blank=True)
    # INSTAL_NO = models.IntegerField(default=None,null=True, blank=True)
    # MONAMT = models.IntegerField(default=None,null=True, blank=True)

    # USER_PASS = models.CharField(max_length=3,null=True, blank=True)
    # USER_NAME = models.CharField(max_length=3,null=True, blank=True)
    # IPADDRESS = models.CharField(max_length=3,null=True, blank=True)
    # MONYEAR = models.CharField(max_length=3,null=True, blank=True)
    # CODE = models.CharField(max_length=3,null=True, blank=True)
    # DESP_NO = models.CharField(max_length=3,null=True, blank=True)

    # PAYHEAD = models.CharField(max_length=3,null=True, blank=True)










#crud operations : vaibhav
#do not edit



class Designation_Nature(models.Model):  # fields of table design nature
    NAME = models.CharField(max_length=20,null=True, blank=True, unique=True)
    class Meta:
        db_table = "DESIGNATION_NATURE"
    def __str__(self):
        return self.NAME

class Under(models.Model):   # fields of table under
    NAME = models.CharField(max_length=20,null=True, blank=True, unique=True)
    class Meta:
        db_table = "UNDER"
    def __str__(self):
        return self.NAME

'''
class Designation(models.Model):
    NAME = models.CharField(max_length=20,null=True, blank=True, unique=True)
    class Meta:
        db_table = "DESIGNATION1"
    def __str__(self):
        return self.NAME

class Department(models.Model):
    NAME = models.CharField(max_length=20,null=True, blank=True, unique=True)
    class Meta:
        db_table = "DEPARTMENT1"
    def __str__(self):
        return self.NAME


class Staff_Type(models.Model):
    NAME = models.CharField(max_length=20,null=True, blank=True, unique=True)
    class Meta:
        db_table = "STAFF_TYPE"
    def __str__(self):
        return self.NAME

class Appointment(models.Model):
    NAME = models.CharField(max_length=20,null=True, blank=True, unique=True)
    class Meta:
        db_table = "APPOINTMENT"
    def __str__(self):
        return self.NAME
'''
class Vacational(models.Model): # fields of table vacational
    NAME = models.CharField(max_length=20,null=True, blank=True, unique=True)
    class Meta:
        db_table = "VACATIONAL"
    def __str__(self):
        return self.NAME

class Bank_Name(models.Model):   # fields of table bank name
    NAME = models.CharField(max_length=20,null=True, blank=True, unique=True)
    class Meta:
        db_table = "BANK_NAME"
    def __str__(self):
        return self.NAME

class Level(models.Model):   # fields of table rule
    NAME = models.CharField(max_length=20,null=True, blank=True, unique=True)
    class Meta:
        db_table = "LEVEL"
    def __str__(self):
        return self.NAME

class Rule(models.Model):    # fields of table rule
    NAME = models.CharField(max_length=20,null=True, blank=True, unique=True)
    class Meta:
        db_table = "RULE"
    def __str__(self):
        return self.NAME


class Gender(models.Model): # fields of table gender
    NAME = models.CharField(max_length=20,null=True, blank=True, unique=True)
    class Meta:
        db_table = "GENDER"
    def __str__(self):
        return self.NAME

class EmployeeInformation(models.Model):     # fields of table employee information

    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))


    id_number_regex = RegexValidator(regex=r'^\d{5}$', message="INVALID ID NUMBER")
    ID_NUMBER = models.CharField(max_length=50,null=True, blank=True, unique=True)

    sequnce_number_regex = RegexValidator(regex=r'^\d{10}$', message="INVALID SEQUENCE NUMBER")
    SEQUENCE_NUMBER = models.CharField(max_length=50,null=True, blank=True)


    TITLE = models.CharField(max_length=50,null=True, blank=True)
    FIRST_NAME = models.CharField(max_length=50,null=True, blank=True)
    MIDDLE_NAME = models.CharField(max_length=50,null=True, blank=True)
    LAST_NAME = models.CharField(max_length=50,null=True, blank=True)
    FATHER_NAME = models.CharField(max_length=50,null=True, blank=True)

    INCREMENT_DATE = models.DateField()
    DATE_OF_BIRTH = models.DateField()
    DATE_OF_JOINING = models.DateField()
    DATE_OF_RETIREMENT = models.DateField()
    DESIGNATION_NAME = models.CharField(max_length=50,null=True, blank=True)

    GENDER= models.CharField(max_length=50,null=True, blank=True)
    TA = models.BooleanField(null=True, blank=True, default=False, choices=BOOL_CHOICES)
    PT = models.BooleanField(max_length=10,null=True, blank=True, default=True, choices=BOOL_CHOICES)
    QUARTER = models.BooleanField(null=True, blank=True, default=True, choices=BOOL_CHOICES)
    RENT_FREE = models.BooleanField(null=True, blank=True, default=True, choices=BOOL_CHOICES)
    QUARTER_ADDRESS = models.CharField(max_length=50,null=True, blank=True)
    HANDICAP = models.BooleanField(null=True, blank=True, default=True, choices=BOOL_CHOICES)
    SENIOR_CITIZEN = models.BooleanField(null=True, blank=True, default=True, choices=BOOL_CHOICES)
    
    
    DESIGNATION = models.CharField(max_length=50,null=True, blank=True)
    DEPARTMENT = models.CharField(max_length=50,null=True, blank=True)
    STAFF_TYPE = models.CharField(max_length=50,null=True, blank=True)
    APPOINTMENT = models.CharField(max_length=50,null=True, blank=True)
    VACATIONAL = models.CharField(max_length=50,null=True, blank=True)
    BANK_NAME = models.CharField(max_length=50,null=True, blank=True)

    account_number_regex = RegexValidator(regex=r'^\d{9,18}$', message="INVALID ACCOUNT NUMBER")
    BANK_ACCOUNT_NUMBER= models.CharField(validators=[account_number_regex], max_length=50, blank=True)
    pf_regex = RegexValidator(regex=r'^[A-Z]{2}/[A-Z]{3}/\d{5}/\d{3}/\d{7}$', message="INVALID PF NUMBER")
    PF_NUMBER = models.CharField(validators=[pf_regex], max_length=50, blank=True, unique=True)
    pran_regex = RegexValidator(regex=r'^\d{12,12}$', message="INVALID PF NUMBER")
    PRAN_NUMBER = models.CharField(validators=[pran_regex], max_length=50, blank=True, unique=True)
    pan_regex = RegexValidator(regex=r'^([a-zA-Z]){5}([0-9]){4}([a-zA-Z]){1}?$', message="INVALID PAN NUMBER")
    PAN_NUMBER = models.CharField(validators=[pan_regex], max_length=50,blank=True, unique=True)
    UNDER = models.CharField(max_length=50,null=True, blank=True)


    LEVEL = models.CharField(max_length=50,null=True, blank=True)
    BASIC = models.IntegerField()
    PAY_STATUS = models.BooleanField(null=True, blank=True, default=False, choices=BOOL_CHOICES)
    RULE = models.CharField(max_length=50,null=True, blank=True)


    REMARK = models.CharField(max_length=50,null=True, blank=True)

    class Meta:
        db_table = "EmployeeInformation"