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
TitleViews, can hold a title context variable which can be used in the template
'''

class ListView(ListView):
    title = None
    
    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context.update({
            'title': self.get_title(),
        })
        return context


class CreateView(CreateView):
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context.update({
            'title': self.get_title(),
        })
        return context


class UpdateView(UpdateView):
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context.update({
            'title': self.get_title(),
        })
        return context


class DetailView(DetailView):
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context.update({
            'title': self.get_title(),
        })
        return context


class DeleteView(DeleteView):
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context.update({
            'title': self.get_title(),
        })
        return context
