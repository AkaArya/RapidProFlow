from django.contrib import admin
from Table.models import AuthUser
from Table.models import FlowsRuleset
from Table.models import FlowsFlowcategorycount
from Table.models import FlowsFlow

admin.site.register(AuthUser)
admin.site.register(FlowsRuleset)
admin.site.register(FlowsFlowcategorycount)
admin.site.register(FlowsFlow)

