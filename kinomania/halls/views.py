from django.shortcuts import render
from kinomania.halls.models import Halls
from django.http import HttpResponse
from django.views import generic as views
from django.urls import reverse_lazy
from kinomania.halls.forms import HallCreateForm
# Create your views here.


def index_hall(request):
    return HttpResponse("hall index")



class DisplayHallView(views.ListView):
    model = Halls
    template_name = "halls/halls-main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["halls"] = Halls.objects.all().order_by("-id")
        return context



class HallDetailsView(views.DetailView):
    template_name = 'halls/hall-details-page.html'
    model = Halls

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_seats'] = self.object.rows * self.object.seats_per_row
        context['rows'] = range(self.object.rows)
        context['seats'] = range(self.object.seats_per_row)
        return context



class CreateHallView(views.CreateView):
    template_name = "halls/hall-create-page.html"
    form_class = HallCreateForm

    def get_success_url(self):
        return  reverse_lazy("hall details", kwargs={"pk": self.object.pk, "slug": self.object.slug})



class EditHallView(views.UpdateView):
    # permission_required = "hall.change_hall"
    # login_url = "/profile/login/"
    template_name = "halls/hall-edit-page.html"
    model = Halls
    fields = "__all__"

    def get_success_url(self):
        reverse_lazy("hall details", kwargs = {"pk": self.object.pk, "slug": self.object.slug})



class DeleteHallView(views.DeleteView):
    # permission_required = "hall.delete_hall"
    template_name = "halls/hall-delete-page.html"
    model = Halls
    success_url = reverse_lazy("hall index")