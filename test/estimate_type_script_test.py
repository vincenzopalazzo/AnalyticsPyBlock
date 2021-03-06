"""
Copyright (c) 2018-2019 Vincenzo Palazzo vicenzopalazzodev@gmail.com
Distributed under the Apache License Version 2.0 software license,
see https://www.apache.org/licenses/LICENSE-2.0.txt
"""
import unittest
from model.type_key_bitcoin import TypeKeyBitcoin
from model.type_script_value import TypescriptValue


class EstimateTypeScriptTest(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.type_key_bitcoin = TypeKeyBitcoin()

    def test_p2pk_one(self):
        script_pub_key = '4104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac'
        type_script = self.type_key_bitcoin.check_ty_script(script_pub_key)
        self.assertEqual(TypescriptValue.TYPE_P2PK, type_script)

    def test_p2pkh_one(self):
        script_pub_key_hash = '76a914ba507bae8f1643d2556000ca26b9301b9069dc6b88ac'
        type_script = self.type_key_bitcoin.check_ty_script(script_pub_key_hash)
        self.assertEqual(TypescriptValue.TYPE_P2PKH, type_script)

    def test_p2sh_one(self):
        script_hex = 'a9146e8ea702743a672edf2ee1d0c21737faf2b2aa8487'
        type_script = self.type_key_bitcoin.check_ty_script(script_hex)
        self.assertEqual(TypescriptValue.TYPE_P2SH, type_script)

    def test_p2wpkh_one(self):
        script_hex = '00149d57c57c3573b58db6b50c10651fc23e40eac0a1'
        type_script = self.type_key_bitcoin.check_ty_script(script_hex)
        self.assertEqual(TypescriptValue.TYPE_P2WPKH, type_script)

    def test_p2wpkh_two(self):
        script_hex = '00145b91adeca7e3e54bebb1b4c9d33a7eb696f190fe'
        type_script = self.type_key_bitcoin.check_ty_script(script_hex)
        self.assertEqual(TypescriptValue.TYPE_P2WPKH, type_script)

    def test_p2wpkh_three(self):
        script_hex = '0014827c5efa6940e99756750e08359f908b150cc68d'
        type_script = self.type_key_bitcoin.check_ty_script(script_hex)
        self.assertEqual(TypescriptValue.TYPE_P2WPKH, type_script)

    def test_p2wsh_one(self):
        script_hex = '0020204ef2ee585c9c9c9ee978a1ebf017c47f3d07f3ebf90f0a96e04e688a2586a9'
        type_script = self.type_key_bitcoin.check_ty_script(script_hex)
        self.assertEqual(TypescriptValue.TYPE_P2WSH, type_script)

    def test_p2wsh_two(self):
        script_hex = '0020701a8d401c84fb13e6baf169d59684e17abd9fa216c8cc5b9fc63d622ff8c58d'
        type_script = self.type_key_bitcoin.check_ty_script(script_hex)
        self.assertEqual(TypescriptValue.TYPE_P2WSH, type_script)


if __name__ == '__main__':
    unittest.main()
