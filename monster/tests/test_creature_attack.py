__author__ = "Andrea Flack"

import unittest

#Import the class where the fuction lices that you are testing
from creature import Creature, Weapon 

#make a new TestCase, CreatureAttackTest, which inherit's from unittest.#TestCase
class CreatureAttackTest(unittest.TestCase):

	#make the things and so the setUp that every test in the test case needs 
	def setUp (self):
		"""Creature an instance of the creature class that we can leverage its functin in our test 
		"""
		self.creature = Creature()
	#undoes everhting that your setup function did.
	def tearDown(self):
		"""Delete the creature
		"""
		del self.creature

	def test_attack_return_int(self):
		"""Ensure that when attack is called, an int is returned.
		"""
		#call the attack function of our creature, and catch what it returns 
		#in value
		value = self.creature.attack()

		self.assertIsInstance(value, int, "Returned atk value is not an int")

	def test_no_weapon_return_base_damage(self):
		"""Ensure that with no weapon equiped, the creature does its base damage
		"""
		#manually set the base damge to 3 
		self.creature.attack_points = 2 

		#get the creatures attack value 
		value = self.creature.attack()

		self.assertEqual(value, 2, "Excepted based attack value")

	def test_with_weapon_return_damage(self):
		"""Ensure that with a weapon, the creature does base damage = weapon damage
		"""

		#make a weapon and give to creature
		weapon = Weapon(3)

		#give the weapon to the creature
		self.creature.weapon = weapon

		#set creature's base attack value 
		self.creature.attack_points =2

		#get the creature's total attack value 
		value = self.creature.attack()
		#Assert the attack value is the base + weapon damage 
		self.assertEqual (value,5, "computed attack value is not correct")








