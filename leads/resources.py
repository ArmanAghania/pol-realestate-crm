from import_export import resources
from .models import Lead


class LeadResource(resources.ModelResource):
    class Meta:
        model = Lead
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'feedback', 'date_added', 'date_modified')
