from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Advocate, Company,Usertype,Plan,Folder,Subscription,File


class CompanySerializer(ModelSerializer):
    employee_count = SerializerMethodField(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'

    def get_employee_count(self, obj):
        count = obj.advocate_set.count()
        return count


class AdvocateSerializer(ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Advocate
        # fields = '__all__'
        fields = ['username', 'bio', 'company']
        
class UsertypeSerializer(ModelSerializer):

    class Meta:
        model = Usertype
        fields = '__all__'
        
class PlanSerializer(ModelSerializer):

    class Meta:
        model = Plan
        fields = '__all__'
        
class FolderSerializer(ModelSerializer):

    class Meta:
        model = Folder
        fields = '__all__'
        
class SubscriptionSerializer(ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'
        
class FileSerializer(ModelSerializer):

    class Meta:
        model = File
        fields = '__all__'