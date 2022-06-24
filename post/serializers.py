from rest_framework import serializers
from post.models import SkillSet as SkillSetModel
from post.models import JobPostSkillSet as JobPostSkillSetModel
from post.models import JobType as JobTypeModel
from post.models import JobPost as JobPostModel
from post.models import Company as CompanyModel
from post.models import CompanyBusinessArea as CompanyBusinessAreaModel
from post.models import BusinessArea as BusinessAreaModel

class SkillSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillSetModel
        fields = ["name", "job_posts"]
        
class JobPostSkillSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostSkillSetModel
        fields = ["Skill_set", "job_post"]

class JobType(serializers.ModelSerializer):
    class Meta:
        model = JobTypeModel
        fields = ["job_type"]
        
class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostModel
        fields = ["job_type", "company", "job_deescription", "salary"]

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = ["company_name", "business_area"]

class CompanyBusinessAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBusinessAreaModel
        fields = ["company", "business_area"]
        
class BusinessAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessAreaModel
        fields = ["area"]