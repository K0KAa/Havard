from typing import List
from django.shortcuts import redirect, render
from django.views.generic import ListView,CreateView,DetailView
from .models import Listing,Bid
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class index(LoginRequiredMixin,ListView):
    model = Listing
    template_name = "auctions/index.html"
    context_object_name = 'listings'


class AddListing(LoginRequiredMixin,CreateView):
    model =Listing
    fields = ["title","description","start_bid","image_url"]
    template_name ="auctions/add_listing.html"
    success_url= "/"

    def form_valid(self,form):
        form.instance.user =self.request.user
        return super().form_valid(form)

def DetailListing(request,pk):
    if request.method == "POST":
        bidval = request.POST["bid"]
        listing = Listing.objects.get(id=pk)
        Bid.objects.create(bid_amount= bidval, user=request.user, listing=listing)
        return redirect("/")

    else:
        listing = Listing.objects.get(id=pk)
        return render(request,'auctions/detail.html',{"listing":listing})

       

