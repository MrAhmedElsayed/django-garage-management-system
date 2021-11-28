from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Ticket


@login_required
def home(request):
    context = dict()
    context["tickets"] = Ticket.objects.all().order_by('created')
    return render(request, template_name='garage_app/index.html', context=context)

# todo: if you prefer using forms !!
# def create_ticket_view(request):
#     form = TicketForm()
#     if request.method == 'POST':
#         form = TicketForm(request.POST)
#
#         if form.is_valid():
#             print('Valid form')
#             form_instance = TicketForm(request.POST).save(commit=False)
#             form_instance.employee = request.user
#             form_instance.ticket_total_price = float(form_instance.reservation_time_per_day) * float(
#                 form_instance.parking_price_per_day)
#             form_instance.save()
#             return redirect('/')
#
#     return render(request, template_name='garage_app/index.html', context={
#         'form': form
#     })
