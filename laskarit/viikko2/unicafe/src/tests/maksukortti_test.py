import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(2500)
        self.assertEqual(str(self.maksukortti), "saldo: 35.0")

    def test_kortilta_voi_ottaa_rahaa(self):
        self.maksukortti.ota_rahaa(900)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")

    def test_kortilta_ei_voi_ottaa_rahaa_jos_saldoa_ei_ole(self):
        self.maksukortti.ota_rahaa(11000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_palauta_true_jos_saldoa_voi_vahentaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100), True)