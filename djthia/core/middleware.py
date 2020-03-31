class StudentEligibilityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.eligible = False

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        response.context_data['eligibility'] = self.eligible
        return response
