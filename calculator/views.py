from django.http import HttpResponse

# Create your views here.
from django.template import loader
from django.views import View


class CalculatorView (View):
    def get(self, request):
        return self.give_me_the_site(request, 0, 0, 0)

    def post(self, request):
        whatever1 = request.POST.get("num1")
        whatever2 = request.POST.get("num2")
        operator = request.POST.get("operator")
        result = cooler_calculator(whatever1, whatever2, operator)
        return self.give_me_the_site(request, whatever1, whatever2, operator, result)


    def give_me_the_site(self, request, whatever1, whatever2, operator, result):
        template = loader.get_template('calculator/index.html')
        context = {
            "num1": whatever1,
            "num2": whatever2,
            "operator": operator,
            "result": result,
            "whatever": "COOLER CALCULATOR",
        }
        return HttpResponse(template.render(context, request))


def cooler_calculator(num1, num2, operator):
    if operator == "+":
        return float(num1) + float(num2)

    elif operator == "-":
        return float(num1) - float(num2)

    elif operator == "*":
        return float(num1) * float(num2)

    else:
        return float(num1) / float(num2)






