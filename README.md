# Altcoins-to-Hash160
Altcoins to hash160 Supported coin types: BTC, LTC, DOGE, DASH, BCH, XRP, ZCASH t1, t3
</P>To brute force altcoin hash160's use Altcrack https://github.com/iceland2k14/AltCrack
  
Single address
python3 altconverter.py</br>
Supported coin types: BTC, LTC, DOGE, DASH, BCH, XRP, ZCASH t1, t3</br>
Enter the cryptocurrency address: t1K1yA7L7SKtF2chEUY7aWH2ehB5Dh58LdB</br>
Enter the coin type (e.g., BTC, LTC, DOGE, etc.): Zcash</br>
Hash160: <Hash160_value> b80c8d1c13f19481cd7dff61d95d4137b752dc117e</br>
<P>
Script run bulk</br>
$ python3 altconvert_bulk.py</br>
Enter the input file name: addresses.txt (or your file name)</br>
Enter the output file name: output.csv (or your file name)</br>
Enter the coin type (e.g., BTC, LTC, DOGE, etc.): DOGE</br>
Processing complete! Output written to output.csv  (or your file name)</br>
</br>
addresses.txt    Input bulk one type</br>
D8ZEVbgf4yPs3MK8dMJJ7PpSyBKsbd66TX</br>
DEgDVFa2DoW1533dxeDVdTxQFhMzs1pMke</br>
DDTtqnuZ5kfRT5qh2c7sNtqrJmV3iXYdGG</br>
</br>
output.csv</br>
Address, Coin Type, Hash160</br>
D8ZEVbgf4yPs3MK8dMJJ7PpSyBKsbd66TX, doge, 2579000e645c4eb1b1e7ec9bf515b313dbdfb6e8</br>
DEgDVFa2DoW1533dxeDVdTxQFhMzs1pMke, doge, 689bd3b0152163202d03f3504b1c6f890aa73bf7</br>
DDTtqnuZ5kfRT5qh2c7sNtqrJmV3iXYdGG, doge, 5b4f2511c94e4fcaa8f8835b2458f8cb6542ca76</br>
<p>
Script run bulk</br>
$ python3 altconvert_bulk1.py</br>
Enter the input file name: addresses.txt (or your file name)</br>
Enter the output file name: output.txt (or your file name)</br>
Enter the coin type (e.g., BTC, LTC, DOGE, etc.): DOGE</br>
Processing complete! Output written to output.csv (or your file name) <br>
<br>
addresses.txt    Input bulk one type<br>
D8ZEVbgf4yPs3MK8dMJJ7PpSyBKsbd66TX<br>
DEgDVFa2DoW1533dxeDVdTxQFhMzs1pMke<br>
DDTtqnuZ5kfRT5qh2c7sNtqrJmV3iXYdGG<br>
<br>
output.txt<br>
Hash160 (single column)<br>
2579000e645c4eb1b1e7ec9bf515b313dbdfb6e8<br>
689bd3b0152163202d03f3504b1c6f890aa73bf7<br>
5b4f2511c94e4fcaa8f8835b2458f8cb6542ca76<br>
<p>
Script run bulk mixed</br>
$ python3 altconvert_bulk_mixed.py</br>
Enter the input file name: addresses.txt (or your file name)</br>
Enter the output file name: output.csv (or your file name)</br>
Processing complete! Output written to output.csv (or your file name)</br>
<br>
addresses.txt    Input bulk mixed</br>
bc1qw4skpmcnns4xx8m5e8eumptxm7hdz2v70wv34y, BTC</br>
t1K1yA7L7SKtF2chEUY7aWH2ehB5Dh58LdB, Zcash</br>
D8ZEVbgf4yPs3MK8dMJJ7PpSyBKsbd66TX, DOGE</br>
<br>
Output bulk mixed </br>
Address, Coin Type, Hash160</br>
bc1qw4skpmcnns4xx8m5e8eumptxm7hdz2v70wv34y, BTC, f2c4c5796fa8c0fbb3b0f405a78cc3b0cfd9d967</br>
t1K1yA7L7SKtF2chEUY7aWH2ehB5Dh58LdB, Zcash, a5128be28b88e6f9edfdad86ed88170bff8488ac</br>
D8ZEVbgf4yPs3MK8dMJJ7PpSyBKsbd66TX, doge, 2579000e645c4eb1b1e7ec9bf515b313dbdfb6e8</br>
<br>
