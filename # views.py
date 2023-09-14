# views.py

from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd

from .models import Employee, Company

def single_entry_update(request):
    if request.method == 'POST':
        update_type = request.POST.get('update_type')  # 'employee' or 'company'
        file_format = request.POST.get('file_format')  # 'csv', 'text', or 'excel'
        data = request.POST.get('data')  # JSON string containing the updated data
        
        # Extract the appropriate model based on the update type
        model = Employee if update_type == 'employee' else Company
        
        # Parse the data based on the file format
        if file_format == 'csv':
            df = pd.read_csv(pd.compat.StringIO(data))
        elif file_format == 'text':
            df = pd.read_csv(pd.compat.StringIO(data), delimiter='\t')
        elif file_format == 'excel':
            df = pd.read_excel(pd.compat.StringIO(data))
        else:
            return JsonResponse({'message': 'Invalid file format.'})
        
        # Iterate over the rows and update the corresponding records
        for _, row in df.iterrows():
            record_id = row['record_id']  # Unique identifier for the record
            record_data = row.to_dict()

            try:
                record = model.objects.get(pk=record_id)
                for field, value in record_data.items():
                    setattr(record, field, value)
                record.save()
            except model.DoesNotExist:
                pass  # Handle non-existent record IDs
        
        return JsonResponse({'message': 'Update completed successfully.'})
