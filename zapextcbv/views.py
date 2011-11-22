'''
@author Aleksandr Aibulatov
@email zap.aibulaotv@gmail.com

Extended generic views
'''
from django.views import generic as cbv


class FilterListView(cbv.ListView):
    '''
    Extension  for ListView. Adding filter for query_set
    '''
    
    def get_filter(self):
        '''
            Return filter options.
            Should be implemented on concrete site
        '''
        return {}
    
    def get_queryset(self):
        '''
            Rewrited queryset
        '''
        return self.model.objects.filter(self.get_filter())


