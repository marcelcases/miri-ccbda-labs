import urllib.request
import os
import sys
import requests
import subprocess

user_input = input("Enter an flickr-link or type 'no' to use the default 'https://www.flickr.com/search/?text=desert' \n here please:\n")

if user_input == "no":
  fp = urllib.request.urlopen("https://www.flickr.com/search/?text=desert") #This is just for testing
  fp = urllib.request.urlopen("https://www.flickr.com/search/?text=barcelona") #This is just for testing
  print("Link to be used: {}".format("https://www.flickr.com/search/?text=desert"))
else:
  fp = urllib.request.urlopen(user_input)
  print("Link to be used: {}".format(user_input))
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

html_lines = mystr.split(" ")
# print(mystr)
count = 0
link_list = []
for elem in html_lines: # go over html line by line
    if ".jpg" in elem: # if jpg in line, split the link from the rest
      link_line = elem.split("\"")
      for line in link_line:
        if ".jpg" in line and "live" in line: # finally detect link in tokenized line
          #last char needs to be the 'g' of jpg
          while line[-1] != 'g':
            line = line[:-1]
          #first char needs to be the 'l' of live
          while line[0] != 'l':
            line = line[1:]
          count += 1
          # print("Sanitized link here::{}".format(line))
          link_list.append(line)
      # print("Here is an extracted image-link :: {}".format(image_link))


      #TODO implement google-hook here.
print("# of images :: {}".format(count))

old_link = ""
counter = 0
image_list = []
# downloads the last images found on the site
for e in range(count-35):  #first 10 images of the site are a bit buggy sometimes
  # if e == 3:
  #   continue
  cut_out_double_slashes = link_list[-e].replace("//","")
  https_link = "https://" + cut_out_double_slashes

  # bug here with \/, so remove this
  https_link = https_link.replace("\\", "")
  print("https-link:: {}".format(https_link))
  print("https-link-reduced:: {}".format(https_link[30:35]))

  #TODO this purges duplicates
  if https_link[30:35] == old_link:
    continue
  old_link = https_link[30:35]
  counter += 1
  response = requests.get(https_link)
  filename = "image_cache/" + str(counter) + ".jpg"
  file = open(filename, "wb")
  image_list.append(filename)
  file.write(response.content)
  file.close()
  #print("last 100 img :: {}".format(link_list[-e]))
print("found {} individual images".format(counter))

# invoke the label-script for each image
bashcmd1 = "python ../cloud-vision/label.py " # image_cache/1.jpg"
resultstring = ""
for elem in image_list: #dispatch cloudvision-call
  cmd = bashcmd1 + elem
  # cmd = [bashcmd1, elem]
  process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

  output, error = process.communicate() # record result
  resultstring = resultstring + " \n " + str(output) #aggregate result

#write result
text_file = open("google_cloud_results.txt", "w")
text_file.write(resultstring)
text_file.close()
