from django.test import TestCase
from habits.models import Habit
from users.models import User


class HabitModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='test_user')

    def test_creation_of_habit(self):
        habit = Habit.objects.create(
            owner=self.user,
            action='Тренировка',
            period=Habit.PERIODS.index(('day', 'Ежедневно')),
            is_nice_habit=True,
            is_public=False
        )

        self.assertEqual(habit.owner, self.user)
        self.assertEqual(habit.action, 'Тренировка')
        self.assertEqual(habit.period, 0)
        self.assertTrue(habit.is_nice_habit)
        self.assertFalse(habit.is_public)

    def test_period_choices(self):
        habit = Habit(period='week')  # Еженедельная привычка
        self.assertEqual(habit.get_period_display(), 'Еженедельно')
