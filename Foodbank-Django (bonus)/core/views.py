
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum

from .models import Family, FoodStock, Distribution


def get_stock():
    stock, _ = FoodStock.objects.get_or_create(id=1)
    return stock


def index(request):
    # Display the report on the homepage without changing the URL.
    return report(request)


def register(request):
    if request.method == 'POST':
        fid = request.POST.get('family_id', '').strip()
        name = request.POST.get('name', '').strip()

        try:
            members = int(request.POST.get('members', 0))
        except ValueError:
            messages.error(request, 'Members must be a number.')
            return render(request, 'core/register.html')

        if not fid or not name:
            messages.error(request, 'ID and name are required.')
            return render(request, 'core/register.html')

        if members <= 0:
            messages.error(request, 'Member count must be positive.')
            return render(request, 'core/register.html')

        if Family.objects.filter(family_id=fid).exists():
            messages.error(request, f'Family ID {fid} already exists.')
            return render(request, 'core/register.html')

        Family.objects.create(
            family_id=fid,
            name=name,
            members=members
        )

        messages.success(request, f'Family {fid} registered.')
        return redirect('register')

    return render(request, 'core/register.html')


def add_food(request):
    stock = get_stock()

    if request.method == 'POST':
        try:
            packs = int(request.POST.get('packs', 0))
        except ValueError:
            messages.error(request, 'Enter a valid number.')
            return render(
                request,
                'core/add_food.html',
                {'stock': stock.packs}
            )

        if packs <= 0:
            messages.error(request, 'Must add a positive number of packs.')
            return render(
                request,
                'core/add_food.html',
                {'stock': stock.packs}
            )

        stock.packs += packs
        stock.save()

        messages.success(
            request,
            f'Added {packs} packs. Stock is now {stock.packs}.'
        )

        return redirect('add_food')

    return render(
        request,
        'core/add_food.html',
        {'stock': stock.packs}
    )


def distribute(request):
    stock = get_stock()
    families = Family.objects.all()

    if request.method == 'POST':
        fid = request.POST.get('family_id', '').strip()

        try:
            packs = int(request.POST.get('packs', 0))
        except ValueError:
            messages.error(request, 'Enter a valid number.')
            return render(
                request,
                'core/distribute.html',
                {'stock': stock.packs, 'families': families}
            )

        try:
            family = Family.objects.get(family_id=fid)
        except Family.DoesNotExist:
            messages.error(request, f'Family {fid} not found.')
            return render(
                request,
                'core/distribute.html',
                {'stock': stock.packs, 'families': families}
            )

        if packs <= 0:
            messages.error(request, 'Packs must be positive.')
            return render(
                request,
                'core/distribute.html',
                {'stock': stock.packs, 'families': families}
            )

        if packs > stock.packs:
            messages.error(
                request,
                f'Not enough stock. Available: {stock.packs}.'
            )
            return render(
                request,
                'core/distribute.html',
                {'stock': stock.packs, 'families': families}
            )

        stock.packs -= packs
        stock.save()

        Distribution.objects.create(
            family=family,
            packs=packs
        )

        messages.success(
            request,
            f'Distributed {packs} packs to {family.name}. '
            f'Remaining: {stock.packs}.'
        )

        return redirect('distribute')

    return render(
        request,
        'core/distribute.html',
        {'stock': stock.packs, 'families': families}
    )


def report(request):
    stock = get_stock()
    families = Family.objects.all()

    history = Distribution.objects.select_related(
        'family'
    ).order_by('-distributed_at')

    total = Distribution.objects.aggregate(
        t=Sum('packs')
    )['t'] or 0

    return render(request, 'core/report.html', {
        'stock': stock.packs,
        'families': families,
        'history': history,
        'total': total,
    })
