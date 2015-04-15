# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusTiming',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bus_route', models.CharField(max_length=512)),
                ('from_time', models.TimeField()),
                ('bus_no', models.CharField(unique=True, max_length=10)),
                ('working_day', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.CharField(unique=True, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeVehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('employee_no', models.IntegerField()),
                ('department', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('block_number', models.CharField(max_length=5)),
                ('flat_number', models.CharField(max_length=5)),
                ('mobile_number', models.IntegerField()),
                ('user_photo', models.ImageField(upload_to=b'')),
                ('identity_card', models.FileField(null=True, upload_to=b'identity_card')),
                ('parking_slot_no', models.CharField(max_length=50)),
                ('vehicle_registration_number', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=32)),
                ('make_and_model', models.CharField(max_length=100)),
                ('chassis_number', models.CharField(max_length=100)),
                ('engine_number', models.CharField(max_length=100)),
                ('registered_in_the_name_of', models.CharField(max_length=100)),
                ('vehicle_insurance_no', models.CharField(unique=True, max_length=100)),
                ('insurance_valid_upto', models.DateField()),
                ('vehicle_registration_card', models.FileField(upload_to=b'vehicle_registration_card')),
                ('vehicle_insurance', models.FileField(null=True, upload_to=b'vehicle_insurance')),
                ('vehicle_photo', models.ImageField(null=True, upload_to=b'')),
                ('driving_license_number', models.CharField(max_length=15)),
                ('driving_license_issue_date', models.DateField()),
                ('driving_license_expiry_date', models.DateField()),
                ('driving_license', models.FileField(null=True, upload_to=b'driving_license')),
                ('declaration', models.TextField(default=b'By submitting this form, I hereby declare that I will be obliged to the following terms and conditions:\n\n1) I will abide by the rules of Traffic,\n2) I will not cause inconvenience to other road users.', null=True, blank=True)),
                ('date_of_application', models.DateTimeField(null=True, blank=True)),
                ('registered_with_security_section', models.BooleanField()),
                ('vehicle_pass_no', models.CharField(max_length=32, unique=True, null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gate_name', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Guard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guard_phone_number', models.IntegerField()),
                ('guard_user', models.OneToOneField(related_name='guard_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IITGUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_student', models.BooleanField(default=False, help_text='Designates whether the user is a student or a professor.', verbose_name='Is student')),
                ('user', models.OneToOneField(related_name='user', default=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OnDutyGuard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.CharField(max_length=100)),
                ('is_gate', models.BooleanField()),
                ('guard', models.OneToOneField(related_name='guard', to='vms.Guard')),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSlot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parking_area_name', models.CharField(unique=True, max_length=100)),
                ('total_slots', models.IntegerField(default=0, null=True, blank=True)),
                ('available_slots', models.IntegerField(default=0, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonPass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('old_card_reference', models.CharField(max_length=10)),
                ('pass_number', models.CharField(unique=True, max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('user_photo', models.ImageField(upload_to=b'')),
                ('age', models.IntegerField()),
                ('identified_by', models.CharField(max_length=255)),
                ('work_area', models.CharField(max_length=255)),
                ('working_time', models.CharField(max_length=255)),
                ('nature_of_work', models.CharField(max_length=255)),
                ('issue_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('is_blocked', models.BooleanField()),
                ('reason', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place_name', models.CharField(unique=True, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ResidentLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('registration_number', models.CharField(max_length=50)),
                ('vehicle_type', models.CharField(blank=True, max_length=50, null=True, choices=[(b'bicycle', b'bicycle'), (b'bike', b'bike'), (b'car', b'car'), (b'truck', b'truck'), (b'courier', b'courier'), (b'auto', b'auto'), (b'other', b'other')])),
                ('vehicle_model', models.CharField(max_length=100, null=True, blank=True)),
                ('is_entering', models.BooleanField(verbose_name=b'Is the vehicle entering?')),
                ('gate', models.ForeignKey(to='vms.Gate', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentCycle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cycle_company', models.CharField(max_length=32)),
                ('cycle_color', models.CharField(max_length=32)),
                ('cycle_pass_no', models.CharField(max_length=10)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentVehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('roll_number', models.IntegerField()),
                ('department', models.CharField(max_length=100)),
                ('programme', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('hostel_name', models.CharField(max_length=32)),
                ('room_number', models.CharField(max_length=5)),
                ('mobile_number', models.IntegerField()),
                ('user_photo', models.ImageField(upload_to=b'')),
                ('identity_card', models.FileField(null=True, upload_to=b'identity_card')),
                ('address_of_communication', models.TextField()),
                ('address_of_communication_district', models.CharField(max_length=100)),
                ('address_of_communication_state', models.CharField(max_length=100)),
                ('address_of_communication_pincode', models.IntegerField()),
                ('permanent_address', models.TextField()),
                ('permanent_address_district', models.CharField(max_length=100)),
                ('permanent_address_state', models.CharField(max_length=100)),
                ('permanent_address_pincode', models.IntegerField()),
                ('parents_contact_no', models.IntegerField()),
                ('parents_emailid', models.EmailField(max_length=75)),
                ('vehicle_registration_number', models.CharField(unique=True, max_length=100)),
                ('color', models.CharField(max_length=32)),
                ('make_and_model', models.CharField(max_length=100)),
                ('chassis_number', models.CharField(max_length=100)),
                ('engine_number', models.CharField(max_length=100)),
                ('registered_in_the_name_of', models.CharField(max_length=100)),
                ('relation_with_owner', models.CharField(max_length=32)),
                ('vehicle_insurance_no', models.CharField(unique=True, max_length=100)),
                ('insurance_valid_upto', models.DateField()),
                ('vehicle_registration_card', models.FileField(null=True, upload_to=b'vehicle_registration_card')),
                ('vehicle_insurance', models.FileField(null=True, upload_to=b'vehicle_insurance')),
                ('vehicle_photo', models.ImageField(upload_to=b'')),
                ('driving_license_number', models.CharField(max_length=15)),
                ('driving_license_issue_date', models.DateField()),
                ('driving_license_expiry_date', models.DateField()),
                ('driving_license', models.FileField(null=True, upload_to=b'driving_license')),
                ('declaration', models.TextField(default=b'By submitting this form, I hereby declare that I will be obliged to the following terms and conditions:\n\n1) I will abide by the rules of Traffic,\n2) I will not cause inconvenience to other road users.', null=True, blank=True)),
                ('date_of_application', models.DateTimeField(null=True, blank=True)),
                ('registered_with_security_section', models.BooleanField()),
                ('vehicle_pass_no', models.CharField(max_length=32, unique=True, null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SuspiciousVehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vehicle_number', models.CharField(unique=True, max_length=20)),
                ('vehicle_type', models.CharField(blank=True, max_length=50, null=True, choices=[(b'bicycle', b'bicycle'), (b'bike', b'bike'), (b'car', b'car'), (b'truck', b'truck'), (b'courier', b'courier'), (b'auto', b'auto'), (b'other', b'other')])),
                ('vehicle_model', models.CharField(max_length=100, null=True, blank=True)),
                ('vehicle_image', models.ImageField(null=True, upload_to=b'suspicious_image', blank=True)),
                ('remarks', models.TextField(max_length=1000, null=True, blank=True)),
                ('reporter', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TheftReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vehicle_pass_no', models.CharField(unique=True, max_length=50)),
                ('theft_time', models.DateTimeField(null=True)),
                ('theft_place', models.CharField(max_length=100, null=True)),
                ('remarks', models.TextField(max_length=1000, null=True, blank=True)),
                ('status', models.CharField(default=b'Submitted', max_length=100, choices=[(b'Submitted', b'Submitted'), (b'Received by Security Section', b'Received by Security Section'), (b'Search in Progress', b'Search in Progress'), (b'Vehicle Found', b'Vehicle Found'), (b'Case Closed (Vehicle Not Found)', b'Case Closed (Vehicle Not Found)'), (b'Vehicle Returned', b'Vehicle Returned')])),
                ('emp_vehicle', models.ForeignKey(blank=True, to='vms.EmployeeVehicle', null=True)),
                ('reporter', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('stud_vehicle', models.ForeignKey(blank=True, to='vms.StudentVehicle', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VisitorLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vehicle_number', models.CharField(max_length=20)),
                ('vehicle_type', models.CharField(blank=True, max_length=50, null=True, choices=[(b'bicycle', b'bicycle'), (b'bike', b'bike'), (b'car', b'car'), (b'truck', b'truck'), (b'courier', b'courier'), (b'auto', b'auto'), (b'other', b'other')])),
                ('vehicle_model', models.CharField(max_length=100, null=True, blank=True)),
                ('driver_name', models.CharField(max_length=255, null=True, blank=True)),
                ('license_number', models.CharField(max_length=20, null=True, blank=True)),
                ('place_to_visit', models.CharField(max_length=100, null=True, blank=True)),
                ('purpose_of_visit', models.TextField(max_length=1000, null=True, blank=True)),
                ('in_time', models.DateTimeField(null=True, blank=True)),
                ('out_time', models.DateTimeField(null=True, blank=True)),
                ('in_gate', models.ForeignKey(related_name='in_gate_log', to='vms.Gate', null=True)),
                ('out_gate', models.ForeignKey(related_name='out_gate_log', to='vms.Gate', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='bustiming',
            name='availability',
            field=models.ManyToManyField(to='vms.Day'),
        ),
        migrations.AddField(
            model_name='bustiming',
            name='ending_point',
            field=models.ForeignKey(related_name='ending_point', to='vms.Place'),
        ),
        migrations.AddField(
            model_name='bustiming',
            name='starting_point',
            field=models.ForeignKey(related_name='starting_point', to='vms.Place'),
        ),
    ]
