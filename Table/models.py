from django.db import models

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=254)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    # rel = models.ManyToManyField(FlowsFlow)

    class Meta:
        managed = False
        db_table = 'auth_user'


class FlowsFlowcategorycount(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_squashed = models.BooleanField()
    node_uuid = models.UUIDField()
    result_key = models.CharField(max_length=128)
    result_name = models.CharField(max_length=128)
    category_name = models.CharField(max_length=128)
    count = models.IntegerField()
    flow = models.ForeignKey('FlowsFlow', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'flows_flowcategorycount'


class FlowsRuleset(models.Model):
    uuid = models.CharField(unique=True, max_length=36)
    label = models.CharField(max_length=64, blank=True, null=True)
    operand = models.CharField(max_length=128, blank=True, null=True)
    webhook_url = models.CharField(max_length=255, blank=True, null=True)
    webhook_action = models.CharField(max_length=8, blank=True, null=True)
    rules = models.TextField()
    finished_key = models.CharField(max_length=1, blank=True, null=True)
    value_type = models.CharField(max_length=1)
    ruleset_type = models.CharField(max_length=16, blank=True, null=True)
    response_type = models.CharField(max_length=1)
    config = models.TextField(blank=True, null=True)
    x = models.IntegerField()
    y = models.IntegerField()
    created_on = models.DateTimeField()
    modified_on = models.DateTimeField()
    flow = models.ForeignKey('FlowsFlow', models.DO_NOTHING, blank=True, null=True)
    #models.ManyToManyField(FlowsFlowcategorycount)


    def __str__(self):
        return "%s (%s)" % (
            self.flow,
            ", ".join(FlowsFlowcategorycount.flow for FlowsFlowcategorycount in self.flow.all()),
        )

    class Meta:
        managed = False
        db_table = 'flows_ruleset'


class FlowsFlow(models.Model):
    is_active = models.BooleanField()
    created_on = models.DateTimeField()
    modified_on = models.DateTimeField()
    uuid = models.CharField(unique=True, max_length=36)
    name = models.CharField(max_length=64)
    entry_uuid = models.CharField(unique=True, max_length=36, blank=True, null=True)
    entry_type = models.CharField(max_length=1, blank=True, null=True)
    is_archived = models.BooleanField()
    flow_type = models.CharField(max_length=1)
    metadata = models.TextField(blank=True, null=True)
    expires_after_minutes = models.IntegerField()
    ignore_triggers = models.BooleanField()
    saved_on = models.DateTimeField()
    base_language = models.CharField(max_length=4, blank=True, null=True)
    version_number = models.CharField(max_length=8)
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING)

    # modified_by = models.ForeignKey('AuthUser', models.DO_NOTHING)
    # org = models.ForeignKey('OrgsOrg', models.DO_NOTHING)
    # saved_by = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'flows_flow'