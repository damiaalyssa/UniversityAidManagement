# Generated by Django 5.1.2 on 2025-02-10 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0007_alter_systemlog_action_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemlog',
            name='action_type',
            field=models.CharField(choices=[('profile_update', 'Profile Update'), ('feedback_submission', 'Feedback Submission'), ('notification_sent', 'Notification Sent'), ('user_registration', 'User Registration'), ('user_login', 'User Login'), ('chat_message', 'Chat Message'), ('profile_deletion', 'Profile Deleted'), ('aid_programs', 'Aid Program'), ('other', 'Other')], max_length=20),
        ),
    ]
