from datetime import date
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from .models import ClasaPrincipala
from .models import Workout


# 1) LOGIN:
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.user.username == "Administrator":
            return reverse_lazy('paginaPrincipala')
        else:
            return reverse_lazy('paginaPrincipalaUser')


# 2) REGISTER:
class CustomRegisterView(FormView):
    template_name = "base/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('paginaPrincipala')

    def form_valid(self, form):
        user = form.save()

        if user is not None:
            login(self.request, user)

        return super(CustomRegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('paginaPrincipala')

        return super(CustomRegisterView, self).get(*args, **kwargs)


# 3) LISTA:
class PaginaPrincipalaView(LoginRequiredMixin, ListView):
    model = ClasaPrincipala
    context_object_name = "ListaPrincipala"
    template_name = 'base/paginaPrincipala.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''

        if search_input:
            context['ListaPrincipala'] = context['ListaPrincipala'].filter(oraInceput__icontains=search_input)

        context['search_input'] = search_input
        return context

    def get(self, *args, **kwargs):
        if self.request.user.username != "Administrator":
            return redirect('paginaPrincipalaUser')
        return super(PaginaPrincipalaView, self).get(*args, **kwargs)


# 4) DETAIL: NU IL FOLOSIM.
class CustomDetailView1(LoginRequiredMixin, DetailView):
    model = ClasaPrincipala
    context_object_name = "ListaPrincipala"
    template_name = "base/afisare.html"


# 5) CREATE:
class CustomCreateView1(LoginRequiredMixin, CreateView):
    model = ClasaPrincipala
    template_name = "base/create_update.html"
    fields = '__all__'
    success_url = reverse_lazy('paginaPrincipala')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CustomCreateView1, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.username != "Administrator":
            return redirect('paginaPrincipalaUser')

        return super(CustomCreateView1, self).get(*args, **kwargs)


# 6) UPDATE:
class CustomUpdateView1(LoginRequiredMixin, UpdateView):
    model = ClasaPrincipala
    template_name = "base/create_update.html"
    fields = '__all__'
    success_url = reverse_lazy('paginaPrincipala')

    def get(self, *args, **kwargs):
        if self.request.user.username != "Administrator":
            return redirect('paginaPrincipalaUser')

        return super(CustomUpdateView1, self).get(*args, **kwargs)


# 7) DELETE:
class CustomDeleteView1(LoginRequiredMixin, DeleteView):
    model = ClasaPrincipala
    template_name = "base/delete.html"

    context_object_name = 'DeleteItem'
    success_url = reverse_lazy('paginaPrincipala')

    def get(self, *args, **kwargs):
        if self.request.user.username != "Administrator":
            return redirect('paginaPrincipalaUser')

        return super(CustomDeleteView1, self).get(*args, **kwargs)


# 8) LISTA PENTRU WORKOUT:
class PaginaWorkoutView(LoginRequiredMixin, ListView):
    model = Workout
    context_object_name = "ListaWorkout"
    template_name = 'base/workoutPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''

        if search_input:
            context['ListaWorkout'] = context['ListaWorkout'].filter(date__icontains=search_input)

        context['search_input'] = search_input
        return context

    def get(self, *args, **kwargs):
        if self.request.user.username != "Administrator":
            return redirect('paginaPrincipalaUser')

        return super(PaginaWorkoutView, self).get(*args, **kwargs)


# 9) CREATE PENTRU WORKOUT:
class CustomCreateView2(LoginRequiredMixin, CreateView):
    model = Workout
    template_name = "base/create_updateWorkout.html"
    fields = '__all__'
    success_url = reverse_lazy('workoutPage')

    def get(self, *args, **kwargs):
        if self.request.user.username != "Administrator":
            return redirect('paginaPrincipalaUser')

        return super(CustomCreateView2, self).get(*args, **kwargs)


# 10) UPDATE PENTRU WORKOUT:
class CustomUpdateView2(LoginRequiredMixin, UpdateView):
    model = Workout
    template_name = "base/create_updateWorkout.html"
    fields = '__all__'
    success_url = reverse_lazy('workoutPage')

    def get(self, *args, **kwargs):
        if self.request.user.username != "Administrator":
            return redirect('paginaPrincipalaUser')

        return super(CustomUpdateView2, self).get(*args, **kwargs)


# 11) DELETE PENTRU WORKOUT:
class CustomDeleteView2(LoginRequiredMixin, DeleteView):
    model = Workout
    template_name = "base/deleteWorkout.html"
    context_object_name = 'DeleteItem'
    success_url = reverse_lazy('workoutPage')

    def get(self, *args, **kwargs):
        if self.request.user.username != "Administrator":
            return redirect('paginaPrincipalaUser')

        return super(CustomDeleteView2, self).get(*args, **kwargs)


# 12) LISTA PENTRU USER:
class PaginaUserView(LoginRequiredMixin, ListView):
    model = ClasaPrincipala
    context_object_name = "ListaPrincipala"
    template_name = 'base/paginaPrincipalaUser.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['ListaPrincipala'] = context['ListaPrincipala'].filter(workout__date=date.today())
        context['dataActuala'] = date.today()
        search_input = self.request.GET.get('search-area') or ''

        if search_input:
            context['ListaPrincipala'] = context['ListaPrincipala'].filter(oraInceput__icontains=search_input)

        context['claseRezervate'] = context['ListaPrincipala'].filter(listaParticipanti__icontains=
                                                                      self.request.user.username + " ;")

        try:
            context['clasaRezervata'] = context['claseRezervate'][0]
        except:
            context['clasaRezervata'] = None

        context['search_input'] = search_input
        return context

    def get(self, *args, **kwargs):
        if self.request.user.username == "Administrator":
            return redirect('paginaPrincipala')

        return super(PaginaUserView, self).get(*args, **kwargs)


# 13) DETAIL PENTRU USER:
class CustomWorkoutView(LoginRequiredMixin, DetailView):
    model = ClasaPrincipala
    context_object_name = "ListaPrincipala"
    template_name = "base/viewWorkout.html"
    success_url = reverse_lazy('paginaPrincipalaUser')

    def reserveSpot(request, block_id):
        objectModel = ClasaPrincipala.objects.get(pk=block_id)
        listaClase = ClasaPrincipala.objects.filter(workout__date=date.today())

        for clasa in listaClase:
            if clasa.listaParticipanti is not None:
                if (request.user.username + " ;") in clasa.listaParticipanti:
                    return redirect("paginaPrincipalaUser")

        if objectModel.complete is False:
            if objectModel.listaParticipanti is None:
                objectModel.listaParticipanti = request.user.username + " ;"
            else:
                if (request.user.username + " ;") not in objectModel.listaParticipanti:
                    objectModel.listaParticipanti += request.user.username + " ;"
                else:
                    return redirect("paginaPrincipalaUser")

            if objectModel.counterParticipanti is None:
                objectModel.counterParticipanti = 1
            else:
                objectModel.counterParticipanti += 1

        if objectModel.counterParticipanti == 5:
            objectModel.complete = True

        objectModel.save()
        return redirect("paginaPrincipalaUser")

    def cancelReservation(request, block_id):
        objectModel = ClasaPrincipala.objects.get(pk=block_id)

        if objectModel.listaParticipanti is None:
            return redirect("paginaPrincipalaUser")
        else:
            if (request.user.username + " ;") in objectModel.listaParticipanti:
                if objectModel.counterParticipanti == 1:
                    objectModel.listaParticipanti = None
                    objectModel.counterParticipanti = None
                else:
                    objectModel.listaParticipanti = objectModel.listaParticipanti.replace(request.user.username + " ;",
                                                                                          "")
                    objectModel.counterParticipanti -= 1
                objectModel.complete = False
            else:
                return redirect("paginaPrincipalaUser")

        objectModel.save()
        return redirect("paginaPrincipalaUser")

    def get(self, *args, **kwargs):
        if self.request.user.username == "Administrator":
            return redirect('paginaPrincipala')

        return super(CustomWorkoutView, self).get(*args, **kwargs)


# 14) VIEW ATTENDANCE LIST PENTRU USER.
class CustomAttendanceListView(LoginRequiredMixin, ListView):
    model = ClasaPrincipala
    context_object_name = "ListaClasa"
    template_name = "base/viewClassAttendanceList.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ListaClasa'] = context['ListaClasa'].filter(listaParticipanti__icontains=self.request.user.username
                                                                                          +" ;")
        search_input1 = self.request.GET.get('Search-Area1') or ''
        if search_input1:
            context['ListaClasa'] = context['ListaClasa']. \
                filter(workout__date__icontains=search_input1)
        context['search_inputHtml1'] = search_input1

        search_input2 = self.request.GET.get('Search-Area2') or ''
        if search_input2:
            context['ListaClasa'] = context['ListaClasa']. \
                filter(workout__title__icontains=search_input2)
        context['search_inputHtml2'] = search_input2

        search_input3 = self.request.GET.get('Search-Area3') or ''
        if search_input3:
            context['ListaClasa'] = context['ListaClasa']. \
                filter(title__icontains=search_input3)
        context['search_inputHtml3'] = search_input3

        return context

    def get(self, *args, **kwargs):
        if self.request.user.username == "Administrator":
            return redirect('paginaPrincipala')

        return super(CustomAttendanceListView, self).get(*args, **kwargs)
