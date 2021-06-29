# Copyright (c) 2021 Luis Sanchez. All Rights Reserved.

# -*- coding: utf-8 -*-
import os
import re
import sys
import clr
import time
import json
import codecs
import System

# Import the chatbot
clr.AddReference([asm for asm in System.AppDomain.CurrentDomain.GetAssemblies() if "AnkhBotR2" in str(asm)][0])
import AnkhBotR2

# Script Information
ScriptName = "Twitch SLCB Leaderboard"
Description = "Show the top 5 viewers with the most chatbot currency"
Creator = "LuisSanchezDev"
Version = "1.0.1"
Website = "https://luissanchezdev.com/"

# Define Global Variables
global PATH, SETTINGS, CONFIG_FILE
PATH = os.path.dirname(os.path.realpath(__file__))
SETTINGS = {}
CACHE_FILE = os.path.join(PATH, "cache.json")

global last_check
last_check = time.time()

# Initialize Data (Only called on load)
def Init():
    push_new_leaderboard()

def Execute(data):
    pass

def Tick():
    global last_check
    if Parent.GetStreamingService() != "Twitch":
        return

    elapsed_time = time.time() - last_check
    if elapsed_time >= 30:
        if has_leaderboard_updated():
            last_check = time.time()
            push_new_leaderboard()

def Unload():
    push_new_leaderboard()

def get_leaderboard():
    parsed = BuiltInParse("$toppoints(5)", "", "").replace(",", "")
    # #1 tecno_diana (10000569) - #2 BitsBearer (3000) - #3 dumb_ted (500) - #4 patriciaefackler (430) - #5 bongtheripper (112)
    pattern = r'#\d\s(\S+)\s\((\d+)\)'
    match = re.findall(pattern, parsed)
    if match:
        users = []
        for row in match:
            users.append({
                "name": row[0],
                "points": float(row[1])
            })
        return {
            "currency": Parent.GetCurrencyName(),
            "users": users
        }
    return []

def BuiltInParse(msg, userId, userName, count = 0):
    asm = [asm for asm in System.AppDomain.CurrentDomain.GetAssemblies() if "AnkhBotR2" in str(asm)][0]
    ParameterExtension = asm.GetType("AnkhBotR2.Helpers.Extensions.ParameterExtension")
    ReplaceParameters = ParameterExtension.GetMethods()[1]
    return ReplaceParameters.Invoke(msg, System.Array[System.Object]([msg, userId, userName, "", count]))

def has_leaderboard_updated():
    global CACHE_FILE
    try:
        with codecs.open(CACHE_FILE, encoding="utf-8-sig", mode='r') as file:
            leaderboard = get_leaderboard()
            cached_leaderboard = json.load(file, encoding="utf-8-sig")
            if leaderboard["currency"] != cached_leaderboard["currency"]:
                return True
            if len(leaderboard["users"]) != len(cached_leaderboard["users"]):
                return True
            for i in range(5):
                if leaderboard["users"][i]["name"] != cached_leaderboard["users"][i]["name"]:
                    return True
                if leaderboard["users"][i]["points"] != cached_leaderboard["users"][i]["points"]:
                    return True
            return False
    except Exception as e:
        Parent.Log(ScriptName, "Error comparing cached file to curent leaderboard\n\t" + str(e))
        return True

def push_new_leaderboard():
    global CACHE_FILE
    if Parent.GetStreamingService() != "Twitch":
        return
    leaderboard = get_leaderboard()
    headers = {
        "Authorization": get_oauth()
    }
    request_response = Parent.PostRequest("https://extensions.luissanchezdev.com/slcb/leaderboard", headers, leaderboard, True)
    response = json.loads(request_response)

    if response["status"] == 200:
        try:
            with codecs.open(CACHE_FILE, encoding="utf-8-sig", mode='w') as file:
                file.write(json.dumps(leaderboard))
        except Exception as e:
            Parent.Log(ScriptName, "Error saving cache file\n\t" + str(e))

def get_oauth():
    vmloc = AnkhBotR2.Managers.GlobalManager.Instance.VMLocator
    return vmloc.StreamerLogin.Token

# UI Buttons
def open_contact_me():
    os.startfile("https://www.fiverr.com/luissanchezdev")




######################
#    DATA
######################
# import clr
# import System
from System.Reflection import *
_ASM = [asm for asm in System.AppDomain.CurrentDomain.GetAssemblies() if "AnkhBotR2" in str(asm)][0]
# clr.AddReference(_ASM)
# import AnkhBotR2

def _get_datamanager_field_value(name):
    DataManager = _ASM.GetType("AnkhBotR2.Managers.DataManager") #.GetProperty("Instance").GetValue(None, None)
    fields = DataManager.GetFields(BindingFlags.Static | BindingFlags.NonPublic)
    dm = [f for f in fields if "instance" in f.Name.lower()][0].GetValue(DataManager)
    fields = DataManager.GetFields(BindingFlags.Instance | BindingFlags.NonPublic)
    output = [f for f in fields if name.lower() in f.Name.lower()][0].GetValue(dm)
    return output

class Data:
    def __init__(self):
        self.DeathCounterSettings = _get_datamanager_field_value("m_DeathCounterSettings")
        self.SongRequestSettings = _get_datamanager_field_value("m_SongRequestSettings")
        self.Locker = _get_datamanager_field_value("m_Locker")
        self.playList = _get_datamanager_field_value("m_playList")
        self.songQueue = _get_datamanager_field_value("m_songQueue")
        self.ActiveServiceData = _get_datamanager_field_value("m_ActiveServiceData")
        self.Settings = _get_datamanager_field_value("<Settings>k__BackingField")
        self.StyleSettings = _get_datamanager_field_value("<StyleSettings>k__BackingField")
        self.CloudSettings = _get_datamanager_field_value("<CloudSettings>k__BackingField")
        self.WhisperSettings = _get_datamanager_field_value("<WhisperSettings>k__BackingField")
        self.HotkeySettings = _get_datamanager_field_value("<HotkeySettings>k__BackingField")
        self.MacroSettings = _get_datamanager_field_value("<MacroSettings>k__BackingField")
        self.DiscordSettings = _get_datamanager_field_value("<DiscordSettings>k__BackingField")
        self.ArenaSettings = _get_datamanager_field_value("<ArenaSettings>k__BackingField")
        self.ChatSettings = _get_datamanager_field_value("<ChatSettings>k__BackingField")
        self.RaidAssistSettings = _get_datamanager_field_value("<RaidAssistSettings>k__BackingField")
        self.CommandSettings = _get_datamanager_field_value("<CommandSettings>k__BackingField")
        self.ExtraLifeNotifySettings = _get_datamanager_field_value("<ExtraLifeNotifySettings>k__BackingField")
        self.YT_SubscriberNotifySettings = _get_datamanager_field_value("<YT_SubscriberNotifySettings>k__BackingField")
        self.YT_SuperChatNotifySettings = _get_datamanager_field_value("<YT_SuperChatNotifySettings>k__BackingField")
        self.YT_SponsorNotifySettings = _get_datamanager_field_value("<YT_SponsorNotifySettings>k__BackingField")
        self.MX_SubscriberNotifySettings = _get_datamanager_field_value("<MX_SubscriberNotifySettings>k__BackingField")
        self.MX_FollowNotifySettings = _get_datamanager_field_value("<MX_FollowNotifySettings>k__BackingField")
        self.MX_HostNotifySettings = _get_datamanager_field_value("<MX_HostNotifySettings>k__BackingField")
        self.BotCredentials = _get_datamanager_field_value("<BotCredentials>k__BackingField")
        self.StreamerCredentials = _get_datamanager_field_value("<StreamerCredentials>k__BackingField")
        self.MixerBotCredentials = _get_datamanager_field_value("<MixerBotCredentials>k__BackingField")
        self.MixerStreamerCredentials = _get_datamanager_field_value("<MixerStreamerCredentials>k__BackingField")
        self.DiscordCredentials = _get_datamanager_field_value("<DiscordCredentials>k__BackingField")
        self.GameWispCredentials = _get_datamanager_field_value("<GameWispCredentials>k__BackingField")
        self.SpotifyCredentials = _get_datamanager_field_value("<SpotifyCredentials>k__BackingField")
        self.StreamlabCredentials = _get_datamanager_field_value("<StreamlabCredentials>k__BackingField")
        self.OBSCredentials = _get_datamanager_field_value("<OBSCredentials>k__BackingField")
        self.ExtraLifeCredentials = _get_datamanager_field_value("<ExtraLifeCredentials>k__BackingField")
        self.StreamlabsPageSettings = _get_datamanager_field_value("<StreamlabsPageSettings>k__BackingField")
        self.ChatBotDatabase = _get_datamanager_field_value("<ChatBotDatabase>k__BackingField")
        self.Localization = _get_datamanager_field_value("<Localization>k__BackingField")
