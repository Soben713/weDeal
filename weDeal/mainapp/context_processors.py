# def add_user(request):
#     print("Here", request.user)
#     if hasattr(request, 'user'):
#         user = request.user
#         if not user.is_anonymous:
#             return {'user': request.user}
#     return {}
