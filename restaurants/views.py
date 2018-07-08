from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        "my_list": [
            {
                "restaurant_name":"Nino",
                "food_type":"Italian",
            },
            {
                "restaurant_name":"Burger King",
                "food_type":"American",
            },
            {
                "restaurant_name":"Pizza Hut",
                "food_type":"Fast Food",
            },
        ],

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {'restaurant_name' : 'Lorenzo'

    }
    return render(request, 'detail.html', context)
