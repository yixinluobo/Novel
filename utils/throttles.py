from rest_framework.throttling import SimpleRateThrottle


class SMSRateThrottle(SimpleRateThrottle):
    scope = 'sms'

    # 对访问ip进行限制
    def get_cache_key(self, request, view):
        ip = request.META.get('REMOTE_ADDR')

        # 返回可以根据ip动态变化，且不易重复的字符串
        return 'throttle_%(scope)s_%(ident)s' % {'scope': self.scope, 'ident': ip}

