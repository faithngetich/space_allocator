import unittest
from .context import Amity
from ..views import Amity
from ..models.rooms import Office
from ..models.rooms import LivingSpace

class Amitytest(unittest.TestCase):
    
    def setUp(self):
        self.amity = Amity()
    
    def test_create_room_adds_room_succesfully(self):
        self.amity.create_room('O', ['Krypton'])
        self.assertIn('KRYPTON', [room.room_name.upper() for room in self.amity.all_rooms])
        

    def test_add_person_adds_fellow_to_list(self):
        all_fellows = len(self.amity.all_fellows) + 1
        self.amity.add_person('dede','faith','F','N')
        self.assertEqual(len(self.amity.all_fellows), all_fellows, msg = "fellow not added")

    def test_add_person_adds_staff_to_list(self):
        all_staff = len(self.amity.all_staff) + 1
        self.amity.add_person('ded','fai','S','N')
        self.assertEqual(len(self.amity.all_staff), all_staff, msg = "staff not added")

    def test_office_is_created_successfully(self):
        """Tests offices are created"""
        self.amity.create_room('O', ['Krypto'])
        self.assertTrue('Krypto' in self.amity.office_allocations.key
        

if __name__ == '__main__':
    unittest.main()

