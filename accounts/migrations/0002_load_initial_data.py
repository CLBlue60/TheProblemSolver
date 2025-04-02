from django.db import migrations

def load_data(apps, schema_editor):
    """Load initial data for all models"""
    Role = apps.get_model('accounts', 'Role')
    Team = apps.get_model('accounts', 'Team')
    Status = apps.get_model('issues', 'Status')
    Priority = apps.get_model('issues', 'Priority')


    Role.objects.bulk_create([
        Role(name='Product Owner', description='Can create issues'),
        Role(name='Developer', description='Works on issues'),
        Role(name='QA', description='Tests issues'),
    ])


    Team.objects.bulk_create([
        Team(name='Frontend', description='Frontend team'),
        Team(name='Backend', description='Backend team'),
        Team(name='Design', description='Design team'),
    ])


    Status.objects.bulk_create([
        Status(name='To Do', description='Not started', order=1),
        Status(name='In Progress', description='Being worked on', order=2),
        Status(name='Done', description='Completed', order=3),
    ])


    Priority.objects.bulk_create([
        Priority(name='Low', level=1),
        Priority(name='Medium', level=2),
        Priority(name='High', level=3),
    ])

class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0001_initial'),
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data),
    ]
