import unittest
from ..views import Amity
class Amitytest(unittest.TestCase):
    
    def setUp(self):
        self.amity = Amity()
    
    def test_create_room_adds_room_succesfully(self):
        self.amity.create_room('office', 'Krypton')
        self.assertIn('Krypton', self.amity.offices)

    # def test_add_person_adds_fellow_to_list(self):
    #     self.amity.add_person('dede','fellow')
    #     all_fellows = len(self.amity.all_fellows) + 1
    #     self.assertEqual(len(self.amity.all_fellows), all_fellows, msg = "fellow not added")

    # def test_person_added_is_fellow(self):
    #     self.amity.add_person('dede', 'fellow')
    #     self.assertIn('dede', self.amity.all_fellows, msg = "person not  added as fellow")
    #     self.assertFalse('dede', 'Staff')
    #     self.assertNotIn('dede', self.amity.all_staff, msg = "dede is not staff")

    # def test_person_added_is_staff(self):
    #     self.amity.add_person('dede', 'staff')
    #     self.assertIn('dede', self.amity.all_fellows, msg = "person not  added as fellow")
    #     self.assertFalse('dede', 'Staff')
    #     self.assertNotIn('dede', self.amity.all_staff, msg = "dede is not staff")
    
    # def test_fellow_wants_accomodation(self):
    #     self.amity.add_person('dede', 'fellow', 'wants_accomodation = Y')
    #     self.assertTrue('dede' in self.amity.accomodation_list, msg = 'fellow not in accomodation list')
    #     self.assertFalse('dede' not in self.amity.accomodation_list, msg = 'fellow should be in the accomodation list')
    #     self.amity.add_person('dede', 'fellow', 'wants_accomodation = Y')
    #     self.assertRaises("Fellow already exists")

    # def test_fellow_does_not_want_accomodation(self):
    #     self.amity.add_person('dede', 'fellow', 'wants_accomodation = N')
    #     self.assertTrue('dede' in self.amity.accomodation_list)
    #     self.assertFalse('awesome' in self.amity.accomodation_list, msg = 'fellow does not want accomodation')

    # def test_Staff_gets_no_accomodation(self):
    #     self.amity.add_person('luke', 'staff', 'wants_accomodation')
    #     self.assertFalse('luke' in self.amity.accomodation_list)
    
    # def test_person_added_is_staff(self):
    #     self.amity.add_person('brian', 'staff')
    #     self.assertIn('brian', self.amity.all_staff, msg = "brian added as staff" )
    #     self.assertFalse('brian', 'fellow')
    #     self.assertNotIn('brian', self.amity.all_fellows, msg = "brian is not staff")

    # def test_if_room_is_livingspace(self):
    #     self.amity.create_room('livingspace', 'ruby')
    #     living_spaces = len(self.amity.living_spaces) + 1
    #     #self.assertEqual(ruby.room_capacity, 4)
    #     self.assertEqual(len(self.amity.living_spaces), living_spaces, msg = "livingroom is not added succesfully")

    # def test_if_room_is_office(self):
    #     self.amity.create_room('office', 'hogwarts')
    #     #self.assertEqual(hogwarts.room_capacity, 6)
    #     offices1 = len(self.amity.offices) + 1
    #     self.assertEqual(len(self.amity.offices), offices1, msg = "livingroom is not added succesfully")

    # def test_reallocate_person(self):
    #     self.amity.create_room('office', 'oculus')
    #     self.amity.add_person('dede', 'staff', 'N')
    #     self.amity.create_room('office', 'valhalla')
    #     self.amity.reallocate_person('dede', 'valhalla')
    #     self.assertIn('dede', self.amity.allocated_rooms['valhalla'])

    # def test_print_allocations_returns_all_allocated_names(self):
    #     self.amity.add_person('dede', 'fellow')
    #     allocated_names = len(self.amity.allocated_rooms) + 1
    #     self.assertEqual(len(self.amity.allocated_rooms), allocated_names, msg = "allocated person is missing")
        
    # def test_print_unallocated_returns_all_not_in_accomodation_list(self):
    #     self.amity.print_unallocated('dede')
    #     self.assertFalse('dede' in self.amity.accomodation_list, msg = "person not in accomodation list")

    # def test_print_rooms_returns_names(self):
    #     self.amity.create_room('office', 'kikwete')
    #     self.amity.add_person('collins', 'staff', 'N')
    #     self.amity.reallocate_person('collins','kikwete')
    #     self.assertIn('collins', self.amity.print_room('kikwete'))
        

if __name__ == '__main__':
    unittest.main()

