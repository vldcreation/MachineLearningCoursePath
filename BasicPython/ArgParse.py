import argparse
import datetime
# Argument Parser
# GetOpt => https://docs.python.org/3.8/library/getopt.html
# ArgParser => https://docs.python.org/3.8/library/argparse.html

 
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")
parser.add_argument('-t', '--tanggallahir', required=True,type=datetime.date.fromisoformat, help="Masukkan Tanggal Lahir  Anda(DD-MM-YYYY)")
args = parser.parse_args()
 
print("Terima kasih telah menggunakan panggildicoding.py, "+args.nama+"\nTangagl Lahir Anda "+str(args.tanggallahir))