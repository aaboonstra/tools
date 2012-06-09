from django.views.generic import ListView, UpdateView, CreateView, DeleteView,\
    DetailView
from django.contrib.auth.decorators import permission_required

'''
Based on DjangoSnippet http://djangosnippets.org/snippets/2317/
Generic views that automaticly checks for permission
'''

class RestrictedListView(ListView):
    def dispatch(self, request, *args, **kwargs):
        @permission_required('%s.change_%s' % (self.model._meta.app_label, self.model._meta.module_name))
        def wrapper(request, *args, **kwargs):
            return super(RestrictedListView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)


class RestrictedUpdateView(UpdateView):
    def dispatch(self, request, *args, **kwargs):
        @permission_required('%s.change_%s' % (self.model._meta.app_label, self.model._meta.module_name))
        def wrapper(request, *args, **kwargs):
            return super(RestrictedUpdateView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)


class RestrictedCreateView(CreateView):
    def dispatch(self, request, *args, **kwargs):
        @permission_required('%s.create_%s' % (self.model._meta.app_label, self.model._meta.module_name))
        def wrapper(request, *args, **kwargs):
            return super(RestrictedCreateView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)


class RestrictedDeleteView(DeleteView):
    def dispatch(self, request, *args, **kwargs):
        @permission_required('%s.delete_%s' % (self.model._meta.app_label, self.model._meta.module_name))
        def wrapper(request, *args, **kwargs):
            return super(RestrictedDeleteView, self).dispatch(request, *args, **kwargs)
        return wrapper(request, *args, **kwargs)


''' 
TitleViewMixin can be used to make sure views have a title that can be used in templates.
get_title() can be overidden to be used for more adavanced titles.

for example ...

def get_title(self):
    return 'Details for %s' % self.object.title
'''
	
class TitleViewMixin(BaseTitleMixin):
    title = None

    def get_title(self):
	if not self.title:
            raise AttributeError('Title is undefined. Either set the variable or override get_title()')
        return self.title

    def get_context_data(self, **kwargs):
        context = super(TitleViewMixin, self).get_context_data(**kwargs)
        context.update({
            'title': self.get_title(),
        })
        return context
