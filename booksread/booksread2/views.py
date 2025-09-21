from django.shortcuts import render

books = []

def book_list(request):
    if request.method == "POST":
        title = request.POST.get("book_title")
        if title:  
            books.append(title)
    return render(request, "books.html", {"books": books})
