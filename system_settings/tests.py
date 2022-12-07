from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import UserManager
from django.contrib.auth import get_user_model
from system_settings.models import Unit, Location, Airport

User = get_user_model()


class CreateUnitViewTests(TestCase):

    def test_not_logged_in(self):
        """
        If user is not logged in, redirect to login page.
        """
        response = self.client.get(reverse('system_settings:unit_add'))
        self.assertRedirects(response, '/accounts/login/?next=/system_settings/unit/add/')

    def test_form_view(self):
        """
        If user is logged in, page should render a form for creating a new unit.
        """
        self.user = User.objects.create_user(username='name', password='tokenpass')
        login = self.client.login(username='name', password='tokenpass')
        response = self.client.get('/system_settings/unit/add/')
        self.assertTemplateUsed(response, template_name='system_settings/unit_form.html')
        self.assertContains(response, '<form action="/system_settings/unit/add/" method="post">')

    def test_form_post(self):
        """
        If the user inputs valid information:
            a new unit is added to database
            user is redirected to system_settings:unit_add
            a success message shows up
        """
        self.user = User.objects.create_user(username='name', password='tokenpass')
        login = self.client.login(username='name', password='tokenpass')
        response = self.client.post('/system_settings/unit/add/', {'name': 'unit', 'unit': 'U'}, follow=True)
        self.assertTemplateUsed(response, template_name='system_settings/unit_form.html')
        self.assertContains(response, 'Unit successfully added.')
        self.assertTrue(Unit.objects.filter(name='unit').exists())

    def test_form_rejected(self):
        """
        If the user inputs invalid information:
            no unit is added
            user is redirected to system_settings:unit_add
            error messages in the form show up
        """
        self.user = User.objects.create_user(username='name', password='tokenpass')
        login = self.client.login(username='name', password='tokenpass')
        response = self.client.post('/system_settings/unit/add/',
                                    {'name': 'unit', 'unit': 'very long unit to make it invalid'}, follow=True)
        self.assertTemplateUsed(response, template_name='system_settings/unit_form.html')
        self.assertContains(response, 'Ensure this value has at most 10 characters')
        self.assertFalse(Unit.objects.filter(name='unit').exists())


class CreateLocationViewTests(TestCase):

    def test_not_logged_in(self):
        """
        If user is not logged in, redirect to login page.
        """
        response = self.client.get(reverse('system_settings:location_add'))
        self.assertRedirects(response, '/accounts/login/?next=/system_settings/location/add/')

    def test_form_view(self):
        """
        If user is logged in, page should render a form for creating a new location.
        """
        self.user = User.objects.create_user(username='name', password='tokenpass')
        login = self.client.login(username='name', password='tokenpass')
        response = self.client.get('/system_settings/location/add/')
        self.assertTemplateUsed(response, template_name='system_settings/location_form.html')
        self.assertContains(response, '<form action="/system_settings/location/add/" method="post">')

    def test_form_post(self):
        """
        If the user inputs valid information:
            a new location is added to database
            user is redirected to system_settings:location_add
            a success message shows up
        """
        self.user = User.objects.create_user(username='name', password='tokenpass')
        login = self.client.login(username='name', password='tokenpass')
        response = self.client.post('/system_settings/location/add/',
                                    {'name': 'location', 'alias': 'alias', 'address': 'address of the location'},
                                    follow=True)
        self.assertTemplateUsed(response, template_name='system_settings/location_form.html')
        self.assertContains(response, 'Location successfully added.')
        self.assertTrue(Location.objects.filter(name='location').exists())

    def test_form_rejected(self):
        """
        If the user inputs invalid information:
            no location is added
            user is redirected to system_settings:location_add
            error messages in the form show up
        """
        self.user = User.objects.create_user(username='name', password='tokenpass')
        login = self.client.login(username='name', password='tokenpass')
        same_alias = Location.objects.create(name='name', alias='alias', address='address')
        response = self.client.post('/system_settings/location/add/',
                                    {'name': 'location', 'alias': 'alias', 'address': 'address of the location'},
                                    follow=True)
        self.assertTemplateUsed(response, template_name='system_settings/location_form.html')
        self.assertContains(response, 'Location with this Alias already exists.')
        self.assertFalse(Unit.objects.filter(name='location').exists())


class CreateAirportViewTests(TestCase):

    def test_not_logged_in(self):
        """
        If user is not logged in, redirect to login page.
        """
        response = self.client.get(reverse('system_settings:airport_add'))
        self.assertRedirects(response, '/accounts/login/?next=/system_settings/airport/add/')

    def test_form_view(self):
        """
        If user is logged in, page should render a form for creating a new airport.
        """
        self.user = User.objects.create_user(username='name', password='tokenpass')
        login = self.client.login(username='name', password='tokenpass')
        response = self.client.get('/system_settings/airport/add/')
        self.assertTemplateUsed(response, template_name='system_settings/airport_form.html')
        self.assertContains(response, '<form action="/system_settings/airport/add/" method="post">')

    def test_form_post(self):
        """
        If the user inputs valid information:
            a new airport is added to database
            user is redirected to system_settings:airport_add
            a success message shows up
        """
        self.user = User.objects.create_user(username='name', password='tokenpass')
        login = self.client.login(username='name', password='tokenpass')
        response = self.client.post('/system_settings/airport/add/',
                                    {'name': 'location', 'alias': 'alias',
                                     'address': 'address of the location', 'IATA_code': 'LOC'},
                                    follow=True)
        self.assertTemplateUsed(response, template_name='system_settings/airport_form.html')
        self.assertContains(response, 'Airport successfully added.')
        self.assertTrue(Airport.objects.filter(name='location').exists())

    def test_form_rejected(self):
        """
        If the user inputs invalid information:
            no location is added
            user is redirected to system_settings:location_add
            error messages in the form show up
        """
        self.user = User.objects.create_user(username='name', password='tokenpass')
        login = self.client.login(username='name', password='tokenpass')
        same_code = Airport.objects.create(name='name', alias='alias', address='address', IATA_code='LOC')
        response = self.client.post('/system_settings/airport/add/',
                                    {'name': 'location', 'alias': 'alias2',
                                     'address': 'address of the location', 'IATA_code': 'LOC'},
                                    follow=True)
        self.assertTemplateUsed(response, template_name='system_settings/airport_form.html')
        self.assertContains(response, 'Airport with this IATA code already exists.')
        self.assertFalse(Airport.objects.filter(name='location').exists())


class ListLocationViewTests(TestCase):

    def test_not_logged_in(self):
        """
        If user is not logged in, redirect to login page.
        """
        response = self.client.get(reverse('system_settings:location_list'))
        self.assertRedirects(response, '/accounts/login/?next=/system_settings/location/list/')

    def test_locations(self):
        """
        If user is logged in, the view shows all locations (airports included).
        """
        self.user = User.objects.create_user(username='name', password='tokenpass')
        login = self.client.login(username='name', password='tokenpass')
        loc1 = Location.objects.create(name='name', alias='alias', address='address')
        loc2 = Airport.objects.create(name='eman', alias='airport', address='address')
        response = self.client.get(reverse('system_settings:location_list'))
        self.assertContains(response, 'airport')
        self.assertContains(response, 'alias')
