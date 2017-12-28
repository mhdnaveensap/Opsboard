from django.http import HttpResponseRedirect,HttpResponse,JsonResponse


class AjaxFormMixin(object):
    def form_invalid(self, form):
        response = super(AjaxFormMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxFormMixin, self).form_valid(form)
        if self.request.is_ajax():
            form = form.cleaned_data
            email = form['email']
            print(email)
            data = {
                'message': "Successfully submitted anveen form data."
            }
            return JsonResponse(data)
        else:
            return response
