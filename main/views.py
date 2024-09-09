from django.shortcuts import render

def show_main(request):
    context = {
        'brand' : 'Wearwise',
        'myname': 'Gilbert Kristian',
        'kelas': 'PBP D',
        'name' : 'Wearwise Black T-Shirt',
        'price': 'Rp150.000',
        'description': 'Baju hitam ini adalah pilihan sempurna untuk gaya yang sederhana namun elegan. Terbuat dari bahan berkualitas tinggi, baju ini memberikan kenyamanan maksimal sepanjang hari. Dengan desain yang klasik dan potongan yang pas, baju ini cocok untuk berbagai kesempatan, baik formal maupun santai.',
        'quantity' : 300
    }

    return render(request, "main.html", context)