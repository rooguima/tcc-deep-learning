from rest_framework.response import Response
from rest_framework import viewsets, status
from distutils import util

from profanity_filter import ProfanityFilter

class FilterViewSet(viewsets.ViewSet):

    def list(self, request):
        if all (k in request.query_params for k in ('comment', 'deep_flag', 'lang')):
            comment   = request.query_params['comment']
            deep_flag = util.strtobool(request.query_params['deep_flag'])
            lang      = request.query_params['lang']

            pf  = ProfanityFilter(censor_whole_words=False,
                                  deep_analysis=deep_flag,
                                  languages=[lang])
            return Response({
                'comment':  pf.censor(comment),
                'approved': pf.is_clean(comment)
            })
        else:
            return Response({'error_message': 'All params are required'},
                            status=status.HTTP_400_BAD_REQUEST)
