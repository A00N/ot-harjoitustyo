import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kassassa_rahaa = 100000
        self.edulliset = 0
        self.maukkaat = 0

        self.maksukortti = Maksukortti(10000)

    def test_kassassa_on_oikea_maara_rahaa(self):
        self.assertEqual(self.kassassa_rahaa, 100000)

    def test_myytyjen_edullisten_lounaiden_maara(self):
        self.assertEqual(self.edulliset, 0)

    def test_myytyjen_maukkaiden_lounaiden_maara(self):
        self.assertEqual(self.maukkaat, 0)

    def test_syo_edullisesti_kateisella_saldo(self):
        self.kassapaate.syo_edullisesti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100240)

    def test_edullisesti_syoty_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset,1)

    def test_syo_maukkaasti_kateisella_saldo(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100400)

    def test_maukkaasti_syoty_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_syo_edullisesti_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kortilla_ottaa_rahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_syo_maukkaasti_kortilla_ottaa_rahaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_syo_edullisesti_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukkaasti_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_edullisesti_kortilla_ei_muuta_kassaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_ei_muuta_kassaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassassa_rahaa, 100000)

    def test_syo_edullisesti_saldo_ei_muutu(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti),"saldo: 1.0")

    def test_syo_edullisesti_edulliset_maara_ei_muutu(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset,0)

    def test_syo_edullisesti_false_jos_ei_rahaa(self):
        self.maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)

    def test_syo_maukkaasti_maara_ei_muutu(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_maukkaasti_saldo_ei_muutu(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")

    def test_syo_maukkaasti_false_jos_ei_rahaa(self):
        self.maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)

    def test_lataa_rahaa_kassan_rahat_muuttuu(self):
        self.maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_lataa_rahaa_saldo_muuttuu(self):
        self.maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_lataa_negatiivista_saldoa(self):
        self.maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")