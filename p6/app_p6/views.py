from django.shortcuts import render


# Create your views here.
def about(request):
    about_content = {
        "about": "Our promise: We put your ideas and your vision into practice - sustainably and always by your side.You know your company and your industry best, we contribute the technical possibilities. Let's combine the best of both worlds. Our task is your success."
    }
    return render(request, "about.html", about_content)
