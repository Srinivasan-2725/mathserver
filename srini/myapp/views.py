from django.shortcuts import render

def power(request):
    context = {'power': "0", 'I': "0", 'R': "0"}  

    if request.method == 'POST':
        try:
            # Must match input names from your HTML form (Intensity, Resistance)
            I = float(request.POST.get('Intensity', '0'))
            R = float(request.POST.get('Resistance', '0'))

            Formula
            p = (I ** 2) * R

            # Store in context for template
            context['power'] = p
            context['I'] = I
            context['R'] = R

            print("POST method is used")
            print("Intensity =", I)
            print("Resistance =", R)
            print("Power =", p)

        except ValueError:
            context['power'] = "Invalid input"

    return render(request, 'myapp/math.html', context)