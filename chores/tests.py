from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.test import TestCase

from .models import Household, Member


class HouseholdModelTests(TestCase):
    def test_string_representation_is_household_name(self):
        household = Household.objects.create(name="The Smiths")

        self.assertEqual(str(household), "The Smiths")


class MemberModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="alex",
            password="test-password",
        )
        self.household = Household.objects.create(name="The Smiths")

    def test_member_links_user_and_household_and_defaults_to_member_role(self):
        member = Member.objects.create(
            user=self.user,
            household=self.household,
        )

        self.assertEqual(member.user, self.user)
        self.assertEqual(member.household, self.household)
        self.assertEqual(member.role, Member.Role.MEMBER)
        self.assertEqual(self.household.members.get(), member)
        self.assertEqual(self.user.household_memberships.get(), member)

    def test_admin_and_member_roles_are_valid(self):
        for role in (Member.Role.ADMIN, Member.Role.MEMBER):
            member = Member(
                user=self.user,
                household=self.household,
                role=role,
            )
            member.full_clean()

    def test_invalid_role_fails_validation(self):
        member = Member(
            user=self.user,
            household=self.household,
            role="owner",
        )

        with self.assertRaises(ValidationError):
            member.full_clean()

    def test_user_can_belong_to_multiple_households(self):
        second_household = Household.objects.create(name="The Joneses")

        first_membership = Member.objects.create(
            user=self.user,
            household=self.household,
        )
        second_membership = Member.objects.create(
            user=self.user,
            household=second_household,
        )

        self.assertNotEqual(first_membership.pk, second_membership.pk)

    def test_user_cannot_have_duplicate_membership_in_same_household(self):
        Member.objects.create(user=self.user, household=self.household)

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Member.objects.create(user=self.user, household=self.household)
