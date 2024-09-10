from django.shortcuts import render , HttpResponse , get_object_or_404
from products.models import Category,Product
from django.template.loader import get_template
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
    #try:
    #p = Product.objects.get(id = product_id)
    p = get_object_or_404(Product,id = product_id)
    template = get_template('products/product.html')
    return HttpResponse(template.render(context={"product": p} , request = request))

    #except Product.DoesNotExist:
        #return HttpResponse('404 Product not found')



