# def add_user(request):
#     print("Here", request.user)
#     if hasattr(request, 'user'):
#         user = request.user
#         if not user.is_anonymous:
#             return {'user': request.user}
#     return {}
from mainapp.forms import DealForm


def add_deal_form(request):
    form = DealForm(prefix="add-deal")
    form.fields['name'].widget.attrs['placeholder'] = 'Name'
    form.fields['description'].widget.attrs['placeholder'] = 'Description'
    form.fields['total_price'].widget.attrs['placeholder'] = 'Total Price'
    form.fields['number_of_items'].widget.attrs['placeholder'] = 'Number of Items'
    form.fields['ending_date'].widget.attrs['placeholder'] = 'Valid Until...'
    form.fields['image'].widget.attrs['placeholder'] = 'Image'

    return {'add_deal_form': form}
