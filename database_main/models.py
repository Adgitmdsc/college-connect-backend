from utility.database_utility import *

class College(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    college_name = models.CharField(max_length=255, unique=True)
    college_identifier = models.CharField(max_length=10, unique=True)
    
    college_email = models.EmailField(max_length=255, null=True, blank=True)
    college_number = models.IntegerField(null=True, blank=True)
    college_address = models.ForeignKey(to="database_general.Address", on_delete=models.SET_NULL, null=True, blank=True, related_name="college_address")
    college_website = models.CharField(max_length=255, blank=True, null=True)

    college_description = models.TextField(blank=True, null=True)
    college_vision = models.TextField(blank=True, null=True)
    college_mission = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.college_name} | {self.college_identifier}"

class Society(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    society_name = models.CharField(max_length=255)
    society_college = models.ForeignKey(to="database_main.College", on_delete=models.CASCADE, related_name="society_college")
    society_identifier = models.CharField(max_length=255, unique=True)

    society_email = models.EmailField(max_length=255, null=True, blank=True)
    society_number = models.IntegerField(null=True, blank=True)
    society_website = models.CharField(max_length=255, blank=True, null=True)
    
    society_description = models.TextField(blank=True, null=True)
    society_category = models.ForeignKey(to="database_general.Tag", on_delete=models.SET_NULL, null=True, blank=True, related_name="society_category")
    society_tags = models.ManyToManyField(to="database_general.Tag", blank=True, related_name="society_tags")

    def __str__(self) -> str:
        return f"{self.society_name} - {self.society_identifier} | {self.society_college.__str__()}"

class Student(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    student_user = models.OneToOneField(to="database_user.User", on_delete=models.CASCADE, related_name="student_user")
    student_identifier = models.CharField(max_length=255, unique=True)

    student_societies = models.ManyToManyField(to="database_main.Society", blank=True, related_name="student_societies")

    def __str__(self) -> str:
        return f"{self.student_user.__str__()} | {self.student_user.identifier}-{self.student_identifier}"

class Faculty(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    faculty_user = models.OneToOneField(to="database_user.User", on_delete=models.CASCADE, related_name="faculty_user")
    faculty_identifier = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f"{self.faculty_user.__str__()} | {self.faculty_user.identifier}-{self.faculty_identifier}"