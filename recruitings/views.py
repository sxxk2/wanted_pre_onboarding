import json

from django.http      import JsonResponse
from django.views     import View

from recruitings.models import Recruiting


class RecruitingView(View):
    # 1. 채용공고를 등록합니다.
    def post(self, request):
        try:
            data = json.loads(request.body)

            company    = request.company
            position   = data['position']
            reward     = data['reward']
            content    = data['content']
            tech_stack = data['tech_stack']

            Recruiting.objects.create(
                company_id = company.id,
                position   = position,
                reward     = reward,
                content    = content,
                tech_stack = tech_stack
            )
            return JsonResponse({'message' : '채용공고가 등록되었습니다.'}, status=201)
        except KeyError:
            return JsonResponse({'message': 'KEY ERROR'}, status=400)
