import unittest
from ..views import Amity
class Amitytest(unittest.TestCase):
    
    def setUp(self):
        self.amity = Amity()
        # self.fellow = fellow
        # self.staff = staff
        # self.livingspace = create_rooms
        # self.office = create_rooms
    
    def test_create_office(self):
        # amity = Amity()
        self.amity.create_rooms('office', 'Krypton')
        all_rooms = len(self.amity.All_rooms)+1
        self.assertEqual(len(self.amity.All_rooms), all_rooms, msg = "office added succesfully")

    def test_add_person(self):
        self.amity.add_person('dede','fellow')
        all_people = len(self.amity.All_people)+1
        self.assertEqual(len(self.amity.All_people), all_people, msg = "person added succesfully")
        
    def test_person_added_is_fellow(self):
        self.amity.add_person('dede', 'fellow')
        self.assertIn('dede', self.amity.All_fellows, msg = "dede added as fellow")
        self.assertFalse('dede', Staff)
        self.assertNotIn('dede', self.amity.All_staff, msg = "dede is not staff")
    
    def test_fellow_wants_accomodation(self):
        self.amity.add_person('dede', 'fellow', 'wants_accomodation = Y')
        self.assertTrue('dede' in self.amity.Accomodation_list)
        self.assertFalse('dede' in self.amity.No_accomodation_list)
        # self.amity.add_person('dede', 'fellow', 'wants_accomodation = Y')
        # self.assertRaises("Fellow already exists")

    def test_fellow_does_not_want_accomodation(self):
        self.amity.add_person('awesome', 'fellow', 'wants_accomodation')
        self.assertTrue('awesome' in self.amity.No_accomodation_list)
        self.assertFalse('awesome' in self.amity.Accomodation_list)
    
    def test_person_added_is_staff(self):
        self.amity.add_person('brian', 'staff')
        self.assertIn('brian', self.amity.All_staff, msg = "brian added as staff" )
        self.assertFalse('brian', Fellow)
        self.assertNotIn('brian', self.amity.All_fellows, msg = "brian is not staff")

    def test_Staff_gets_no_accomodation(self):
        self.amity.add_person('luke', 'staff', msg = 'wants_accomodation')
        self.assertTrue('dede' in self.amity.No_accomodation_list)

    def test_if_room_is_livingspace(self):
        self.amity.create_rooms('livingspace', 'ruby')
        all_rooms = len(self.amity.All_rooms)+1
        self.assertEqual(len(self.amity.All_rooms), all_rooms, msg = "livingroom added succesfully")

    def test_reallocate_person(self):
        pass

if __name__ == '__main__':
    unittest.main()

