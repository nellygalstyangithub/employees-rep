from tastypie.authentication import ApiKeyAuthentication

class CustomAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
      if request.method == "Get":
         return True
      
      return super().is_authenticated(request, **kwargs)

      