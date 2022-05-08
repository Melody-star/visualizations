from django.db import models

class PersonNum(models.Model):
    StudentNum = models.IntegerField()
    TeacherNum = models.IntegerField()
    WorkerNum = models.IntegerField()
    Freshman = models.IntegerField()
    Sophomore = models.IntegerField()
    Junior = models.IntegerField()
    Senior = models.IntegerField()

# PersonNum.objects.create(StudentNum="13871", TeacherNum="915", WorkerNum="405",Freshman="3455", Sophomore="3562", Junior="3452", Senior="3402")


class Classroom(models.Model):
    name = models.CharField(max_length=16)
    total = models.IntegerField()
    use = models.IntegerField()

# Classroom.objects.create(name="科技楼", total="80", use="64")
# Classroom.objects.create(name="生科楼", total="90", use="56")
# Classroom.objects.create(name="化材楼", total="85", use="43")
# Classroom.objects.create(name="三元区", total="256", use="198")
# Classroom.objects.create(name="同大综合楼", total="75", use="65")
# Classroom.objects.create(name="教一", total="80", use="64")
# Classroom.objects.create(name="天工楼", total="85", use="79")
# Classroom.objects.create(name="天成楼", total="95", use="90")
# Classroom.objects.create(name="计科楼", total="110", use="96")
# Classroom.objects.create(name="美术楼", total="245", use="126")


class News(models.Model):
    title = models.CharField(max_length=64)
    time = models.CharField(max_length=64)
    place = models.CharField(max_length=64)


# News.objects.create(title="发现体温异常人员", place="同大北门", time="2022-3-31 20:22:30")
# News.objects.create(title="物联设备异常", place="三里8栋", time="2022-3-31 12:23:30")
# News.objects.create(title="车辆超速", place="鄂K·88888", time="2022-3-31 21:32:30")
# News.objects.create(title="发现体温异常人员", place="西二门", time="2022-3-31 09:16:30")
# News.objects.create(title="发现体温异常人员", place="南大门", time="2022-3-31 09:16:30")


class IotEquipment(models.Model):
    num = models.IntegerField()
    name = models.CharField(max_length=64)


# IotEquipment.objects.create(name="教学楼", num="540")
# IotEquipment.objects.create(name="西区", num="1186")
# IotEquipment.objects.create(name="三里", num="1200")
# IotEquipment.objects.create(name="东区", num="780")
# IotEquipment.objects.create(name="同大", num="1820")

class ControlPass(models.Model):
    place = models.CharField(max_length=32)
    person = models.IntegerField()
    unusual = models.IntegerField()

# ControlPass.objects.create(place="同大北门", person="234", unusual="0")
# ControlPass.objects.create(place="同大南门", person="543", unusual="1")
# ControlPass.objects.create(place="三园区", person="345", unusual="0")
# ControlPass.objects.create(place="西二门", person="643", unusual="2")
# ControlPass.objects.create(place="南大门", person="453", unusual="0")
# ControlPass.objects.create(place="东区", person="154", unusual="1")

class CarSystem(models.Model):
    place = models.CharField(max_length=32)
    amount = models.IntegerField()

# CarSystem.objects.create(place="东区", amount="242")
# CarSystem.objects.create(place="三里", amount="320")
# CarSystem.objects.create(place="西区", amount="142")
# CarSystem.objects.create(place="三园区", amount="220")
# CarSystem.objects.create(place="同大南区", amount="292")
# CarSystem.objects.create(place="同大北区", amount="372")