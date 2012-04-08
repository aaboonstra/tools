from django.core.paginator import InvalidPage
from tools.pagination import NamePaginator 


class NamedPaginatedViewMixin(object):
    paginate_on = None
    '''
    Mixing that uses a NamePaginator.
    Usage:
        in the view define a class variable 'per_page' to define
        the number of items the list will be paginated to. If not 
        defined the default of 25 will be used. 
    '''

    def get_context_data(self, *args, **kwargs):
        context = super(NamedPaginatedViewMixin, self).get_context_data(*args, **kwargs)
        if not self.paginate_on:
            raise AttributeError("paginate_on is undefined")
        try: 
            paginator = NamePaginator(self.object_list, on=self.paginate_on, per_page=self.per_page)
        except AttributeError:
            paginator = NamePaginator(self.object_list, on=self.paginate_on, per_page=25)

        try:
            page = int(self.request.GET.get('page', '1'))
        except ValueError:
            page = 1

        try:
            page = paginator.page(page)
        except InvalidPage:
            page = paginator.page(paginator.num_pages)
 
        context['page'] =  page
        return context
