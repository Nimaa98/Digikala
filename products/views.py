from django.shortcuts import render , HttpResponse , get_object_or_404
from products.models import Category,Product
from django.template.loader import get_template , render_to_string
# Create your views here.


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()[:10]

    category_response = ''

    for c in categories:

        category_response += f'<li>{c.name}</li>'

    category_response = f'<ul>{category_response}</ul>'



    product_response = ''

    for p in products:

        product_response += f'<li><a href="/products/{p.id}">{p.name}</li>'

    product_response = f'<ul>{product_response}</ul>'



    return HttpResponse(f"""
    <html>
    <head><title>Digikala</title></head>
    <body>
    <h1 style = 'color:red'>the best seller site in iran</h1>
    {category_response}
    {product_response}
    </body>
    </html>
    """)




def product_view(request,product_id):

    p = get_object_or_404(Product,id = product_id)
    context = {'product': p}
    return render(
        template_name ='products/product.html',
        request=request,
        context=context
    )






