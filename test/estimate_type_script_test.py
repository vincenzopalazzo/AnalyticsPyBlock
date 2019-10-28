"""
Copyright (c) 2018-2019 Vincenzo Palazzo vicenzopalazzodev@gmail.com
Distributed under the Apache License Version 2.0 software license,
see https://www.apache.org/licenses/LICENSE-2.0.txt
"""
import unittest
from model.type_key_bitcoin import TypeKeyBitcoin


class EstimateTypeScriptTest(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.type_key_bitcoin = TypeKeyBitcoin()

    def test_p2pk_one(self):
        script_pub_key = '4104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac'
        type_script = self.type_key_bitcoin.check_ty_script(script_pub_key)
        self.assertEqual(self.type_key_bitcoin.TYPE_P2PK, type_script)

    def test_p2pkh_one(self):
        script_pub_key_hash = '76a914ba507bae8f1643d2556000ca26b9301b9069dc6b88ac'
        type_script = self.type_key_bitcoin.check_ty_script(script_pub_key_hash)
        self.assertEqual(self.type_key_bitcoin.TYPE_P2PKH, type_script)

    def test_p2sh_one(self):
        script_hex = 'a9146e8ea702743a672edf2ee1d0c21737faf2b2aa8487'
        type_script = self.type_key_bitcoin.check_ty_script(script_hex)
        self.assertEqual(self.type_key_bitcoin.TYPE_P2SH, type_script)

    def test_p2wpkh_one(self):
        script_hex = '00149d57c57c3573b58db6b50c10651fc23e40eac0a1'
        type_script = self.type_key_bitcoin.check_ty_script(script_hex)
        self.assertEqual(self.type_key_bitcoin.TYPE_P2WPKH, type_script)


if __name__ == '__main__':
    unittest.main()
