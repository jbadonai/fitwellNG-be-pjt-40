# Generated by Django 3.2.4 on 2021-07-08 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitwellNG_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('routine_name', models.CharField(help_text='squats, Jumping-Jack, etc', max_length=200)),
                ('description', models.TextField(help_text='How is it being done?')),
                ('repetition_no', models.IntegerField(help_text='Expected number of repetition daily')),
                ('repetition_achieved_today', models.IntegerField(null=True)),
                ('repetition_achieved_total', models.IntegerField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='mealplanslist',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mealplanslist',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.CreateModel(
            name='WorkoutPlanList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(help_text='Beginners, Intermediate, Expert...', max_length=200)),
                ('duration', models.IntegerField(help_text='weeks')),
                ('daily_duration', models.IntegerField(help_text='Time in Mins to spend daily')),
                ('time_spent_today', models.IntegerField(help_text='In Minutes', null=True)),
                ('time_spent_total', models.IntegerField(help_text='In Minutes', null=True)),
                ('routines', models.ManyToManyField(to='fitwellNG_app.Routine')),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutPlan',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fitwellNG_app.user')),
                ('workout_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitwellNG_app.workoutplanlist')),
            ],
        ),
    ]