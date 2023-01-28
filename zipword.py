import zipfile
import time

folderpath = input("\nPATH TO THE FILE => ")
zipf = zipfile.ZipFile(folderpath)

global result
result = 0
global tried
tried = 0
c = 0

if not zipf:
  print("\nZIPPED FILE/FOLDER NOT PASSWORD PROTECTED! YOU CAN SUCCESSFULLY OPEN IT!")
else:
  startTime = time.time()
  wordListFile = open("wordlist.txt", "r", errors="ignore")
  body = wordListFile.read().lower()
  words = body.split("\n")

  print("\n")
  for i in range(len(words)):
    word = words[i]
    password = word.encode("utf-8").strip()
    c+= 1
    print("TRYING TO DECODE PASSWORD BY: {}".format(word))

    try:
      with zipfile.ZipFile(folderpath, "r") as zf:
        zf.extractall(pwd=password)
        print("\nSUCCESS! THE PASSWORD IS: " + word)
        endtime = time.time()
        result = 1
      break
    except: pass

  if not result:
    print(f"\nPASSWORD NOT FOUND. PASSWORD IS NOT 4 CHARACTERS.")
  else:
    duration = endtime - startTime
    print(f"\nCONGRATULATIONS! PASSWORD FOUND AFTER TRYING {str(c)} COMBINATIONS IN {str(duration)} SECONDS.")