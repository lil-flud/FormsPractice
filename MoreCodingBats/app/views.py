from django.shortcuts import render
from app.forms import (
    SumDoubleForm,
    Diff21Form,
    SleepInForm,
    CountHiForm,
    StringMatchForm,
    RoundSumForm,
)

# Create your views here.

choices = [
    "Warmup-1: Sum-Double",
    "Warmup-1: Diff21",
    "Warmup-1: Sleep-In",
    "String-2: Count-Hi",
    "Warmup-2: String-Match",
    "Logic-2: Round-Sum",
    # "String-1: Left2",
    # "String-1: Combo-String",
    # "String-1: First-Half",
]


def home(request):
    context = {"choices": choices}
    return render(request, "home.html", context)


def details(request, name):
    if name == "Warmup-1: Sum-Double":
        if request.method == "POST":
            form = SumDoubleForm(request.POST)
            if form.is_valid():
                a = form.cleaned_data["a"]
                b = form.cleaned_data["b"]
                if a != b:
                    answer = a + b
                else:
                    answer = (a + b) * 2
                context = {"answer": answer, "form": form, "name": name}
                return render(request, "details_page.html", context)
        else:
            form = SumDoubleForm()
            return render(request, "details_page.html", {"form": form, "name": name})
    elif name == "Warmup-1: Diff21":
        if request.method == "POST":
            form = Diff21Form(request.POST)
            if form.is_valid():
                n = form.cleaned_data["a"]
                if n <= 21:
                    answer = 21 - n
                elif n > 21:
                    answer = (n - 21) * 2
                context = {"answer": answer, "form": form, "name": name}
                return render(request, "details_page.html", context)
        else:
            form = Diff21Form()
            return render(request, "details_page.html", {"form": form, "name": name})
    elif name == "Warmup-1: Sleep-In":
        if request.method == "POST":
            form = SleepInForm(request.POST)
            if form.is_valid():
                w = form.cleaned_data["Weekday"]
                v = form.cleaned_data["Vacation"]
                if not w or v:
                    answer = "Feel free to sleep in!"
                else:
                    answer = "You've gotta be up early!"
                context = {"answer": answer, "form": form, "name": name}
                return render(request, "details_page.html", context)
        else:
            form = SleepInForm()
            return render(request, "details_page.html", {"form": form, "name": name})
    elif name == "String-2: Count-Hi":
        if request.method == "POST":
            form = CountHiForm(request.POST)
            if form.is_valid():
                string = form.cleaned_data["str"]
                count = 0
                for i in range(0, len(string) - 1, 1):
                    placeholder = string[i] + string[i + 1]
                    if placeholder == "hi":
                        count = count + 1
                context = {"form": form, "answer": count, "name": name}
                return render(request, "details_page.html", context)
        else:
            form = CountHiForm()
            return render(request, "details_page.html", {"form": form, "name": name})
    elif name == "Warmup-2: String-Match":
        if request.method == "POST":
            form = StringMatchForm(request.POST)
            if form.is_valid():
                a = form.cleaned_data["a"]
                b = form.cleaned_data["b"]
                count = 0
                shortest = min(len(a), len(b))

                for individual in range(shortest - 1):
                    amt_a = a[individual : individual + 2]
                    amt_b = b[individual : individual + 2]
                    if amt_a == amt_b:
                        count += 1
                context = {"form": form, "name": name, "answer": count}
                return render(request, "details_page.html", context)
        else:
            form = StringMatchForm()
            return render(request, "details_page.html", {"form": form, "name": name})
    elif name == "Logic-2: Round-Sum":
        if request.method == "POST":
            form = RoundSumForm(request.POST)
            if form.is_valid():
                a = form.cleaned_data["a"]
                b = form.cleaned_data["b"]
                c = form.cleaned_data["c"]
                answer = round10(a) + round10(b) + round10(c)
                context = {"form": form, "name": name, "answer": answer}
                return render(request, "details_page.html", context)
        else:
            form = RoundSumForm()
            return render(request, "details_page.html", {"form": form, "name": name})


def round10(num):
    if num % 10 >= 5:
        return num + 10 - (num % 10)
    return num - (num % 10)


# def details(request, name):
#     if name == "Warmup-1: Sum-Double":
#         context = sumdouble_view(request)
#     elif name == "Warmup-1: Diff21":
#         context = diff21_view(request)
#     elif name == "Warmup-1: Sleep-In":
#         context = sleepin_view(request)
#     elif name == "String-1: Left2":
#         context = left2_view_view(request)
#     elif name == "String-1: Combo-String":
#         context = combo_string_view(request)
#     elif name == "String-1: First-Half":
#         context = first_half_view(request)
#     context["name"] = name
#     return render(request, "details_page.html", context)


# def sumdouble(a, b):
#     if a != b:
#         answer = a + b
#     else:
#         answer = (a + b) * 2
#     return answer


# def sumdouble_view(request):
#     if name == "Warmup-1: Sum-Double":
#         if request.method == "POST":
#             form = SumDoubleForm(request.POST)
#             if form.is_valid():
#                 a = form.cleaned_data["a"]
#                 b = form.cleaned_data["b"]
#                 context = {"answer": sumdouble(a, b), "form": form}
#                 return context
#         else:
#             form = SumDoubleForm()
#             return {"form": form}
