# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myproject.myapp.models import LogFile
from myproject.myapp.forms import LogFileForm

import json

import traceback


#file parse handler
from myproject.myapp.parser import lowparse

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = LogFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['docfile']
            newLog = LogFile(docfile=file)
            newLog.save()
            count_map = lowparse.handle_uploaded_file(file,lowparse.get_api_times_count)
            count_map_json = json.dumps(count_map)
            return render_to_response('statistic.html',{'count_map':count_map_json});

            # Redirect to the document list after POST
            # return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = LogFileForm()  # A empty, unbound form

    # Load documents for the list page
    documents = LogFile.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
