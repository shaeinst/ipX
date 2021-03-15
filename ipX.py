#! /usr/bin/python3

"""
Author: Ali Shahid
Github: https://github.com/shaeinst/ipX
website: https://shaeinst.github.io/

API provided by: https://ipapi.co/
"""




# ----------------------------------------------------------------------------
# import important module
import argparse             # to handle argument
from requests import get    # to get data from online


# ----------------------------------------------------------------------------
#       setup argument
# ----------------------------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument( "-i","--ip", default=1,
                    help="ip address you want to track")
parser.add_argument("-I","--myip", "--self", action="store_true",
                    help="get details of your own IP")
parser.add_argument("-o", "--output", default="result.json",
                    help="save details of tracked IP, example result.json. valid formats are json, jsonp, xml, csv, yaml")
parser.add_argument("-no","--nooutput", action="store_true",
                    help="save details of IP without showing result")

args = parser.parse_args()

# if no flag is given print help messege:
if args.ip == 1 and not args.myip:
    print("to get help:\npython ipX.py --help")

# IP address which we want to track
ip_address = args.ip

# our own IP address
my_ip = args.myip

# file name for saving tracked IP
file_name = args.output

#file extension
file_name_ext = file_name.split(".")[-1]
if len(file_name.split(".")) < 2:
    file_name_ext = "json"

nooutput = args.nooutput
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# import module only if required
if file_name_ext == "json":
    import json
# ----------------------------------------------------------------------------
#



# ----------------------------------------------------------------------------
# get own ip address
def getMyIP(ext):
    url = "https://ipapi.co/"+ext
    tracked_ip = get(url)
    if ext == "json":
        return tracked_ip.json()
    return tracked_ip.text


# get target ip
def getTargetIP(ip, ext):
    url = "https://ipapi.co/"+ip+"/"+ext
    tracked_ip = get(url)
    if ext == "json":
        return tracked_ip.json()
    return tracked_ip.text


# write result (tracked ip)
def saveIP(dataTosave, SaveAs):
    # save as json if file is json
    if file_name_ext == "json":
        with open(SaveAs, 'w') as fil:
            json.dump(dataTosave, fil, indent=4, sort_keys=True)
    else:
        with open(SaveAs, 'w') as fil:
            fil.writelines(dataTosave)


# print output result
def printResult():

    # making function to print each types of file is little time consuming
    # and increase the line of code(loc). so we are going to print json only
    # if user has specify filename with other extension, then we are goign to
    # re request ip in json format.
    # --------------this block give us json result---------------------
    if my_ip:
        ipdata = myip
    if ip_address != 1:
        ipdata = target_ip
    if file_name_ext != "json":
        if my_ip:
            ipdata = getMyIP("json")
        if ip_address != 1:
            ipdata = getTargetIP(ip_address, "json")
    # -----------------------------------------------------------------

    # printing json file in human understandable form
    ls = []
    count = 0
    for key, value in ipdata.items():
        ls.insert(count, [key, value])
        count += 1
    from tabulate import tabulate
    print (tabulate(ls))

# ----------------------------------------------------------------------------




# ----------------------------------------------------------------------------
# getting details of own and target IP address at once make no sence.
if my_ip and ip_address != 1:
    print(""" common, this make no sence.
    either get your ip or other ip\nnot both""")
    exit()


if my_ip:
    # we are going to use json for tracking own IP
    if len(file_name.split(".")) < 2:
        file_name = file_name+".json"

    # get our own ip
    myip = getMyIP(file_name_ext)

    # save result if option nooutput or output is selected
    if nooutput or file_name != "result.json":
        saveIP(myip, file_name)

    # show result only if nooutput option is not selected
    if not nooutput:
        printResult()


if ip_address != 1:
    # we are going to use json if extension is not mentioned
    if len(file_name.split(".")) < 2:
        file_name = file_name+".json"

    # get ip details
    target_ip = getTargetIP(ip_address, file_name_ext)

    # save result if option nooutput or output is selected
    if nooutput or file_name != "result.json":
        saveIP(target_ip, file_name)

    # show result only if nooutput option is not selected
    if not nooutput:
        printResult()

# ----------------------------------------------------------------------------

