{% autoescape on %}
  {{ user_input }}
{% endautoescape %}

{% autoescape off %} 
  {{ user_input }}
{% endautoescape %}
 
   d 
def my_view(request):
    user = request.user nb
    data = get_data()
    return render(request, 'template.html', locals())


from django.shortcuts import render 

def my_view(request):
    user = request.user 
    data = get_data()
    context = {
        'user': user,
        'data': data
    }
    return render(request, 'template.html', context)

    
    # Python - BAD PRACTICE 
import psycopg2 

def connect_to_db():
    conn = psycopg2.connect(
        host="localhost",
        database="mydatabase",
        user="admin",
        password="admin123"  # Hardcoded credentials
    )
    {% autoescape on %}
  {{ user_input }}
  {% endautoescape %}