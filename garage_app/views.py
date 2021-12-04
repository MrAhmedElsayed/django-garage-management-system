from io import BytesIO

import qrcode
import qrcode.image.svg
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from .models import Ticket


@login_required
def home(request):
    return render(request, template_name='garage_app/home.html')


@login_required
def ticket_management(request):
    context = dict()
    context["tickets"] = Ticket.objects.all().order_by('created')
    return render(request, template_name='garage_app/ticket_list.html', context=context)


def qr_generator(request):
    """
    https://medium.com/geekculture/how-to-generate-a-qr-code-in-django-e32179d7fdf2
    """
    if request.method == "POST" and request.is_ajax() and request.POST.get("operation") == "generate_qr":
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("qr_text", ""), image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        svg = stream.getvalue().decode()
        return JsonResponse({"svg": svg, }, status=200)
    return JsonResponse({"success": False}, status=400)


def generate_pdf():
    # https://github.com/fdemmer/django-weasyprint
    # https://doc.courtbouillon.org/weasyprint/stable/first_steps.html
    # HELP: https://www.codegrepper.com/code-examples/whatever/Weasyprint+save+pdf
    pass

# https://medium.com/geekculture/how-to-generate-a-qr-code-in-django-e32179d7fdf2
# @login_required
# def qr_generator(request):
#     context = dict()
#     context["tickets"] = Ticket.objects.all().order_by('created')
#     return render(request, template_name='garage_app/ticket_list.html', context=context)
