from import_export import resources
from .models import ContestQuestion
 
class QuestionResource(resources.ModelResource):
    class Meta:
        model = ContestQuestion