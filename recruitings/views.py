import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

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
    # 4-1,2. 채용공고를 불러오고 검색합니다.
    def get(self, request):
        try:
            search = request.GET.get('search', None)

            q = Q()

            if search:
                q &= Q(company__name__icontains=search)
                q &= Q(position__icontains=search)
                q &= Q(content__icontains=search)
                q &= Q(tech_stack__icontains=search)

            results = [{
                'id'         : recruiting.id,
                'company'    : recruiting.company.name,
                'country'    :recruiting.company.country,
                'region'     :recruiting.company.region,
                'reward'     : recruiting.reward,
                'content'    : recruiting.content,
                'tech_stack' : recruiting.tech_stack,
            } for recruiting in Recruiting.objects.filter(q).distinct()]
            return JsonResponse({"results" : results}, status = 200)
        except KeyError:
            return JsonResponse({"message" : "KEY ERROR"}, status=400)

class RecruitingDetailView(View):
    # 5. 채용 상세페이지를 가져옵니다.
    def get(self, request, recruiting_id):
        if not Recruiting.objects.filter(id=recruiting_id).exists():
            return JsonResponse({'message' : '채용공고가 없습니다.'}, status=404)

        recruiting = Recruiting.objects.get(id=recruiting_id)

        result = {
            'recruiting_id' : recruiting.id,
            'company'       : recruiting.company.name,
            'position'      : recruiting.position,
            'reward'        : recruiting.reward,
            'content'       : recruiting.content,
            'tech_stack'    : recruiting.tech_stack
        }
        return JsonResponse({'result' : result}, status=200)
    # 2. 채용공고를 수정합니다.
    def put(self, request, recruiting_id):
        try:
            data = json.loads(request.body)

            position = data['position']
            reward     = data['reward']
            content    = data['content']
            tech_stack = data['tech_stack']

            recruiting = Recruiting.objects.get(id=recruiting_id)

            recruiting.position   = position
            recruiting.reward     = reward
            recruiting.content    = content
            recruiting.tech_stack = tech_stack

            recruiting.save()

            return JsonResponse({'message': 채용공고가 수정되었습니다.}, status=201)
        except Recruiting.DoesNotExist:
            return JsonResponse({'message' : '없는 채용공고입니다.'}, status=401)
    # 3. 채용공고를 삭제합니다.
    def delete(self, request, recruiting_id):
        if not Recruiting.objects.filter(id=recruiting_id).exists():
            return JsonResponse({'message' : '채용공고가 없습니다.'}, status=404)
        recruiting = Recruiting.objects.get(id=recruiting_id)
        recruiting.delete()

        return JsonResponse({'message' : '채용공고가 삭제되었습니다.'}, status=200)
