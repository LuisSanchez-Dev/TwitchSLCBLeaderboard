import clr
import System
from System.Reflection import *
_ASM = [asm for asm in System.AppDomain.CurrentDomain.GetAssemblies() if "AnkhBotR2" in str(asm)][0]
clr.AddReference(_ASM)
import AnkhBotR2

def _get_datamanager_field_value(name):
    DataManager = _ASM.GetType("AnkhBotR2.Managers.DataManager") #.GetProperty("Instance").GetValue(None, None)
    fields = DataManager.GetFields(BindingFlags.Static | BindingFlags.NonPublic)
    dm = [f for f in fields if "instance" in f.Name.lower()][0].GetValue(DataManager)
    fields = DataManager.GetFields(BindingFlags.Instance | BindingFlags.NonPublic)
    output = [f for f in fields if name.lower() in f.Name.lower()][0].GetValue(dm)
    return output

class Data:
    """
    Attributes:
        DeathCounterSettings (DeathCounterSettings): AnkhBotR2.Helpers.Data.Settings.DeathCounterSettings
        SongRequestSettings (SongRequestSettings): AnkhBotR2.Helpers.Data.Settings.SongRequestSettings
        Locker (Object): System.Object
        playList (ObservableCollection`1): System.Collections.ObjectModel.ObservableCollection`1[AnkhBotR2.Helpers.Com.YoutubeVideo]
        songQueue (ObservableCollection`1): System.Collections.ObjectModel.ObservableCollection`1[AnkhBotR2.Helpers.Com.YoutubeVideo]
        ActiveServiceData (StreamingServiceData): AnkhBotR2.Helpers.Data.Structures.Users.StreamingServiceData
        Settings (Settings): AnkhBotR2.Data.Settings
        StyleSettings (UIStyleSettingV2): AnkhBotR2.Data.UIStyleSettingV2
        CloudSettings (CloudSettings): AnkhBotR2.Data.CloudSettings
        WhisperSettings (WhisperSettings): AnkhBotR2.Helpers.Data.Settings.WhisperSettings
        HotkeySettings (HotkeySetting): AnkhBotR2.Helpers.Data.Settings.HotkeySetting
        MacroSettings (MacroSetting): AnkhBotR2.Helpers.Data.Settings.MacroSetting
        DiscordSettings (DiscordSetting): AnkhBotR2.Helpers.Data.Settings.DiscordSetting
        ArenaSettings (ArenaSetting): AnkhBotR2.Helpers.Data.Settings.ArenaSetting
        ChatSettings (ChatSetting): AnkhBotR2.Helpers.Data.Settings.ChatSetting
        RaidAssistSettings (RaidAssistSetting): AnkhBotR2.Helpers.Data.Settings.RaidAssistSetting
        CommandSettings (CommandSetting): AnkhBotR2.Helpers.Data.Settings.CommandSetting
        ExtraLifeNotifySettings (ExtraLifeNotifySetting): AnkhBotR2.Helpers.Data.Settings.ExtraLifeNotifySetting
        YT_SubscriberNotifySettings (YT_SubscriberNotifySettings): AnkhBotR2.Helpers.Data.Settings.Notifications.YT_SubscriberNotifySettings
        YT_SuperChatNotifySettings (YT_SuperChatNotifySettings): AnkhBotR2.Helpers.Data.Settings.Notifications.YT_SuperChatNotifySettings
        YT_SponsorNotifySettings (YT_SponsorNotifySettings): AnkhBotR2.Helpers.Data.Settings.Notifications.YT_SponsorNotifySettings
        MX_SubscriberNotifySettings (SubscriberNotifySetting): AnkhBotR2.Helpers.Data.Settings.SubscriberNotifySetting
        MX_FollowNotifySettings (FollowerNotifySetting): AnkhBotR2.Helpers.Data.Settings.FollowerNotifySetting
        MX_HostNotifySettings (HostNotifierSetting): AnkhBotR2.Helpers.Data.Settings.HostNotifierSetting
        BotCredentials (BotCredentials): AnkhBotR2.Data.BotCredentials
        StreamerCredentials (StreamerCredentials): AnkhBotR2.Data.StreamerCredentials
        MixerBotCredentials (MixerCredentials): AnkhBotR2.Data.MixerCredentials
        MixerStreamerCredentials (MixerCredentials): AnkhBotR2.Data.MixerCredentials
        DiscordCredentials (DiscordCredentials): AnkhBotR2.Data.Discord.DiscordCredentials
        GameWispCredentials (GameWispCredentials): AnkhBotR2.Data.Discord.GameWispCredentials
        SpotifyCredentials (SpotifyCredentials): AnkhBotR2.Helpers.Data.Spotify.SpotifyCredentials
        StreamlabCredentials (StreamlabsCredentials): AnkhBotR2.Data.Discord.StreamlabsCredentials
        OBSCredentials (OBSCredentials): AnkhBotR2.Data.OBSCredentials
        ExtraLifeCredentials (ExtraLifeCredentials): AnkhBotR2.Helpers.Data.Credentials.ExtraLifeCredentials
        StreamlabsPageSettings (StreamlabsPageSettings): AnkhBotR2.Helpers.Data.Streamlabs.StreamlabsPageSettings
        ChatBotDatabase (ChatBotDatabase): AnkhBotR2.Datamodels.ChatBotDatabase
        Localization (Localization): AnkhBotR2.Helpers.Data.Localization.Localization
    """
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

class DeathCounterSettings(AnkhBotR2.Helpers.Data.Settings.DeathCounterSettings):
        """
        Attributes:
            Command (String): System.String
        Template (String): System.String
        StartAmount (Int32): System.Int32
        FontSize (Int32): System.Int32
        Font (Int32): System.Int32
        Style (Int32): System.Int32
        Weight (Int32): System.Int32
        TextColor (String): System.String
        BgColor (String): System.String
        """
        pass
            
class SongRequestSettings(AnkhBotR2.Helpers.Data.Settings.SongRequestSettings):
        """
        Attributes:
            EnableSongRequests (Boolean): System.Boolean
        Volume (Int32): System.Int32
        RequestPermission (String): System.String
        RequestInfo (String): System.String
        MaxSongDuration (Int32): System.Int32
        SkipPermission (String): System.String
        SkipInfo (String): System.String
        VetoPermission (String): System.String
        VetoInfo (String): System.String
        ViewerCost (Int32): System.Int32
        RegularCost (Int32): System.Int32
        SubCost (Int32): System.Int32
        ModCost (Int32): System.Int32
        SkipCost (Int32): System.Int32
        VetoCost (Int32): System.Int32
        ViewerMaxSongs (Int32): System.Int32
        RegularMaxSongs (Int32): System.Int32
        SubMaxSongs (Int32): System.Int32
        ModMaxSongs (Int32): System.Int32
        MinSkipVotes (Int32): System.Int32
        MaxQueueSize (Int32): System.Int32
        LastPlayListLocation (String): System.String
        GameWispCost (Int32): System.Int32
        GameWispMaxSongs (Int32): System.Int32
        Youtube (Boolean): System.Boolean
        Spotify (Boolean): System.Boolean
        ShowVideo (Boolean): System.Boolean
        Quality (String): System.String
        LikedVideosOnly (Boolean): System.Boolean
        LimitToMusic (Boolean): System.Boolean
        LimitToPlaylist (Boolean): System.Boolean
        RepeatPlaylist (Boolean): System.Boolean
        """
        pass
            
class StreamingServiceData(AnkhBotR2.Helpers.Data.Structures.Users.StreamingServiceData):
        """
        Attributes:
            ClientIdTwitch (String): System.String
        ClientIdYoutube (String): System.String
        ClientIdMixer (String): System.String
        ActiveService (StreamingServiceType): AnkhBotR2.Data.Enums.StreamingServiceType
        """
        pass
            
class Settings(AnkhBotR2.Data.Settings):
        """
        Attributes:
            TimerSettings (TimerSetting): AnkhBotR2.Data.TimerSetting
        QuoteSettings (QuoteSetting): AnkhBotR2.Data.QuoteSetting
        GiveAwaySettings (GiveAwaySetting): AnkhBotR2.Data.GiveAwaySetting
        SFXSettings (SFXSetting): AnkhBotR2.Data.SFXSetting
        CurrencySettings (CurrencySetting): AnkhBotR2.Data.CurrencySetting
        DashboardSettings (DashboardSetting): AnkhBotR2.Data.DashboardSetting
        GroupMinigameSettings (GroupMinigameSetting): AnkhBotR2.Helpers.Data.Settings.GroupMinigameSetting
        BasicSettings (BasicSetting): AnkhBotR2.Helpers.Data.Settings.BasicSetting
        CapsSettings (CapsProtectionSetting): AnkhBotR2.Helpers.Data.Settings.CapsProtectionSetting
        SymbolSettings (SymbolProtectionSetting): AnkhBotR2.Helpers.Data.Settings.SymbolProtectionSetting
        HostNotifierSettings (HostNotifierSetting): AnkhBotR2.Helpers.Data.Settings.HostNotifierSetting
        LinkSettings (LinkProtectionSetting): AnkhBotR2.Helpers.Data.Settings.LinkProtectionSetting
        RaiderSettings (RaiderSetting): AnkhBotR2.Helpers.Data.Settings.RaiderSetting
        SubSettings (SubscriberNotifySetting): AnkhBotR2.Helpers.Data.Settings.SubscriberNotifySetting
        WordSettings (WordProtectionSetting): AnkhBotR2.Helpers.Data.Settings.WordProtectionSetting
        FollowNotifySettings (FollowerNotifySetting): AnkhBotR2.Helpers.Data.Settings.FollowerNotifySetting
        ExtraQuoteSettings (ExtraQuoteSetting): AnkhBotR2.Data.ExtraQuoteSetting
        BlackListSettings (BlackListSettings): AnkhBotR2.Helpers.Data.Settings.BlackListSettings
        QueueSettings (QueueSettings): AnkhBotR2.Helpers.Data.Settings.QueueSettings
        CheerSettings (CheerNotifySetting): AnkhBotR2.Helpers.Data.Settings.CheerNotifySetting
        GameWispSubSettings (GameWispSubscriberNotifySetting): AnkhBotR2.Helpers.Data.Settings.GameWispSubscriberNotifySetting
        StreamlabsNotifySettings (StreamlabsNotifySetting): AnkhBotR2.Helpers.Data.Settings.StreamlabsNotifySetting
        """
        pass
            
class UIStyleSettingV2(AnkhBotR2.Data.UIStyleSettingV2):
        """
        Attributes:
            ActiveStyle (String): System.String
        ChatScale (Double): System.Double
        ItemHeight (Double): System.Double
        """
        pass
            
class CloudSettings(AnkhBotR2.Data.CloudSettings):
        """
        Attributes:
            GoogleDrivePath (String): System.String
        AutoBackup (Boolean): System.Boolean
        Days (Int32): System.Int32
        LastBackup (DateTime): System.DateTime
        """
        pass
            
class WhisperSettings(AnkhBotR2.Helpers.Data.Settings.WhisperSettings):
        """
        Attributes:
            Mode (String): System.String
        Status (String): System.String
        Game (String): System.String
        StartHost (String): System.String
        StopHost (String): System.String
        ComAdd (String): System.String
        ComRemove (String): System.String
        ComEdit (String): System.String
        ComCount (String): System.String
        Enable (String): System.String
        ComCooldown (String): System.String
        ComUserCooldown (String): System.String
        ComUsage (String): System.String
        TimAdd (String): System.String
        TimRemove (String): System.String
        TimEdit (String): System.String
        Activate (String): System.String
        QuotAdd (String): System.String
        QuotRemove (String): System.String
        QuotEdit (String): System.String
        Quote (String): System.String
        Raffle (String): System.String
        GiveStart (String): System.String
        GiveClose (String): System.String
        GiveWinner (String): System.String
        SFX (String): System.String
        Points (String): System.String
        PointAdd (String): System.String
        PointRemove (String): System.String
        PointAddAll (String): System.String
        PointRemoveAll (String): System.String
        PointsTransfer (String): System.String
        Bet (String): System.String
        BetStart (String): System.String
        BetStop (String): System.String
        BetAbort (String): System.String
        BetWinner (String): System.String
        Vote (String): System.String
        PollStart (String): System.String
        PollStop (String): System.String
        Heist (String): System.String
        Events (String): System.String
        Songrequest (String): System.String
        Skip (String): System.String
        Veto (String): System.String
        SongblAdd (String): System.String
        SongblRemove (String): System.String
        Volume (String): System.String
        WrongSong (String): System.String
        Join (String): System.String
        QueOpen (String): System.String
        QueClose (String): System.String
        QueClear (String): System.String
        QueueLeave (String): System.String
        QueuePick (String): System.String
        RegAdd (String): System.String
        RegRemove (String): System.String
        Permit (String): System.String
        Raider (String): System.String
        BlackAdd (String): System.String
        BlackRemove (String): System.String
        Death (String): System.String
        DeathP (String): System.String
        DeathM (String): System.String
        DeathN (String): System.String
        GifAdd (String): System.String
        GifRemove (String): System.String
        GifEdit (String): System.String
        Gif (String): System.String
        ArenaOneVOne (String): System.String
        ArenaFFA (String): System.String
        ArenaBoss (String): System.String
        """
        pass
            
class HotkeySetting(AnkhBotR2.Helpers.Data.Settings.HotkeySetting):
        """
        Attributes:
            UseHotkeysInAnkhBot (Boolean): System.Boolean
        SongPlayPause (String): System.String
        SongSteal (String): System.String
        SongBlacklist (String): System.String
        SongSkip (String): System.String
        SongVolUp (String): System.String
        SongVolDown (String): System.String
        DeathIncrease (String): System.String
        DeathDecrease (String): System.String
        Commercial1 (String): System.String
        Commercial2 (String): System.String
        Commercial3 (String): System.String
        Commercial4 (String): System.String
        Commercial5 (String): System.String
        Commercial6 (String): System.String
        Macro1 (String): System.String
        Macro2 (String): System.String
        Macro3 (String): System.String
        Macro4 (String): System.String
        Macro5 (String): System.String
        Macro6 (String): System.String
        Macro7 (String): System.String
        HostToggle (String): System.String
        SkipAlert (String): System.String
        ToggleAlertVolume (String): System.String
        ToggleAlertQueue (String): System.String
        RollCredits (String): System.String
        EmptyJar (String): System.String
        MuteBot (String): System.String
        SpinWheel (String): System.String
        """
        pass
            
class MacroSetting(AnkhBotR2.Helpers.Data.Settings.MacroSetting):
        """
        Attributes:
            Macro1 (String): System.String
        Macro2 (String): System.String
        Macro3 (String): System.String
        Macro4 (String): System.String
        Macro5 (String): System.String
        Macro6 (String): System.String
        Macro7 (String): System.String
        Macro1Name (String): System.String
        Macro2Name (String): System.String
        Macro3Name (String): System.String
        Macro4Name (String): System.String
        Macro5Name (String): System.String
        Macro6Name (String): System.String
        Macro7Name (String): System.String
        """
        pass
            
class DiscordSetting(AnkhBotR2.Helpers.Data.Settings.DiscordSetting):
        """
        Attributes:
            AnnounceStreamLive (Boolean): System.Boolean
        AnnounceMessage (String): System.String
        AnnounceChannel (String): System.String
        PostTimersInDiscord (Boolean): System.Boolean
        PostTimersChannel (String): System.String
        PostInterval (Int32): System.Int32
        PostMinChatLines (Int32): System.Int32
        AutoAssignRole (Boolean): System.Boolean
        CustomEmbed (Boolean): System.Boolean
        RoleName (String): System.String
        """
        pass
            
class ArenaSetting(AnkhBotR2.Helpers.Data.Settings.ArenaSetting):
        """
        Attributes:
            ArenaOneVOne (ArenaOneVOne): AnkhBotR2.Helpers.Data.Settings.ArenaOneVOne
        ArenaFreeForAll (ArenaFreeForAll): AnkhBotR2.Helpers.Data.Settings.ArenaFreeForAll
        ArenaBossBattle (ArenaBossBattle): AnkhBotR2.Helpers.Data.Settings.ArenaBossBattle
        ViewerStats (ArenaStats): AnkhBotR2.Data.ArenaStats
        RegularStats (ArenaStats): AnkhBotR2.Data.ArenaStats
        ModStats (ArenaStats): AnkhBotR2.Data.ArenaStats
        SubStats (ArenaStats): AnkhBotR2.Data.ArenaStats
        GwSubStats (ArenaStats): AnkhBotR2.Data.ArenaStats
        """
        pass
            
class ChatSetting(AnkhBotR2.Helpers.Data.Settings.ChatSetting):
        """
        Attributes:
            UseEmotes (Boolean): System.Boolean
        UseGifEmotes (Boolean): System.Boolean
        HighlightMentions (String): System.String
        HideBotMessages (Boolean): System.Boolean
        UseSplitChat (Boolean): System.Boolean
        CreateCache (Boolean): System.Boolean
        UseOldChat (Boolean): System.Boolean
        SubBadge (String): System.String
        ReplyMixerCostream (Boolean): System.Boolean
        """
        pass
            
class RaidAssistSetting(AnkhBotR2.Helpers.Data.Settings.RaidAssistSetting):
        """
        Attributes:
            Enabled (Boolean): System.Boolean
        Command (String): System.String
        LinkTimes (Int32): System.Int32
        Reward (Int64): System.Int64
        UseRewardTimer (Boolean): System.Boolean
        RewardTimer (Int32): System.Int32
        UseLinkPostTimer (Boolean): System.Boolean
        LinkTimer (Int32): System.Int32
        Instructions (String): System.String
        WaitForStreamer (Boolean): System.Boolean
        StreamerStartMessage (String): System.String
        RaidCall (String): System.String
        ViewerWorm (String): System.String
        UseSubWorm (Boolean): System.Boolean
        SubWorm (String): System.String
        CeaseRewardOnMessage (Boolean): System.Boolean
        CeaseMessage (String): System.String
        PostResults (Boolean): System.Boolean
        ResultsMessage (String): System.String
        """
        pass
            
class CommandSetting(AnkhBotR2.Helpers.Data.Settings.CommandSetting):
        """
        Attributes:
            DisplayCooldownMessages (Boolean): System.Boolean
        CooldownMessageTemplate (String): System.String
        DisplayCostMessages (Boolean): System.Boolean
        CostMessageTemplate (String): System.String
        DisplayPermissionMessages (Boolean): System.Boolean
        PermissionMessageTemplate (String): System.String
        """
        pass
            
class ExtraLifeNotifySetting(AnkhBotR2.Helpers.Data.Settings.ExtraLifeNotifySetting):
        """
        Attributes:
            PlaySFX (Boolean): System.Boolean
        ShowRealName (Boolean): System.Boolean
        SFXPath (String): System.String
        Enabled (Boolean): System.Boolean
        StandardReply (String): System.String
        AnonReply (String): System.String
        """
        pass
            
class YT_SubscriberNotifySettings(AnkhBotR2.Helpers.Data.Settings.Notifications.YT_SubscriberNotifySettings):
        """
        Attributes:
            PlaySFX (Boolean): System.Boolean
        SFXPath (String): System.String
        Enabled (Boolean): System.Boolean
        CustomReply (String): System.String
        """
        pass
            
class YT_SuperChatNotifySettings(AnkhBotR2.Helpers.Data.Settings.Notifications.YT_SuperChatNotifySettings):
        """
        Attributes:
            PlaySFX (Boolean): System.Boolean
        SFXPath (String): System.String
        Enabled (Boolean): System.Boolean
        CustomReply (String): System.String
        """
        pass
            
class YT_SponsorNotifySettings(AnkhBotR2.Helpers.Data.Settings.Notifications.YT_SponsorNotifySettings):
        """
        Attributes:
            PlaySFX (Boolean): System.Boolean
        SFXPath (String): System.String
        Enabled (Boolean): System.Boolean
        CustomReply (String): System.String
        """
        pass
            
class SubscriberNotifySetting(AnkhBotR2.Helpers.Data.Settings.SubscriberNotifySetting):
        """
        Attributes:
            PlaySFX (Boolean): System.Boolean
        SFXPath (String): System.String
        Enabled (Boolean): System.Boolean
        CustomReply (String): System.String
        CustomResubReply (String): System.String
        CustomPrimeReply (String): System.String
        CustomGiftReply (String): System.String
        MysterySubGiftReply (String): System.String
        """
        pass
            
class FollowerNotifySetting(AnkhBotR2.Helpers.Data.Settings.FollowerNotifySetting):
        """
        Attributes:
            PlaySFX (Boolean): System.Boolean
        SFXPath (String): System.String
        Enabled (Boolean): System.Boolean
        CustomMessage (String): System.String
        PollTwitch (Int32): System.Int32
        WelcomeDelay (Int32): System.Int32
        """
        pass
            
class HostNotifierSetting(AnkhBotR2.Helpers.Data.Settings.HostNotifierSetting):
        """
        Attributes:
            PlaySFX (Boolean): System.Boolean
        SFXPath (String): System.String
        Enabled (Boolean): System.Boolean
        CustomReply (String): System.String
        MinViewers (Int32): System.Int32
        NotifyAutoHost (Boolean): System.Boolean
        """
        pass
            
class BotCredentials(AnkhBotR2.Data.BotCredentials):
        """
        Attributes:
            Username (String): System.String
        Channel (String): System.String
        Token (String): System.String
        ChannelID (String): System.String
        BotChannelId (String): System.String
        Server (String): System.String
        IsNew (Boolean): System.Boolean
        IsVerified (Boolean): System.Boolean
        """
        pass
            
class StreamerCredentials(AnkhBotR2.Data.StreamerCredentials):
        """
        Attributes:
            Username (String): System.String
        Token (String): System.String
        IsPartnered (Boolean): System.Boolean
        ChannelID (String): System.String
        Validated (Boolean): System.Boolean
        IsAffiliate (Boolean): System.Boolean
        NotifiedServer (Boolean): System.Boolean
        """
        pass
            
class MixerCredentials(AnkhBotR2.Data.MixerCredentials):
        """
        Attributes:
            Name (String): System.String
        UserId (String): System.String
        ChannelId (String): System.String
        AccessToken (String): System.String
        TokenType (String): System.String
        ExpiresIn (Int64): System.Int64
        RefreshToken (String): System.String
        CreatedAt (DateTime): System.DateTime
        """
        pass
            
class DiscordCredentials(AnkhBotR2.Data.Discord.DiscordCredentials):
        """
        Attributes:
            ClientId (String): System.String
        Token (String): System.String
        BotChannel (String): System.String
        LiveChannel (String): System.String
        SubscriberRole (String): System.String
        """
        pass
            
class GameWispCredentials(AnkhBotR2.Data.Discord.GameWispCredentials):
        """
        Attributes:
            TempToken (String): System.String
        Oauth (String): System.String
        ExpiryDate (DateTime): System.DateTime
        RefreshToken (String): System.String
        AllowSubCommands (Boolean): System.Boolean
        """
        pass
            
class SpotifyCredentials(AnkhBotR2.Helpers.Data.Spotify.SpotifyCredentials):
        """
        Attributes:
            AccessToken (String): System.String
        RefreshToken (String): System.String
        TokenType (String): System.String
        CreatedAt (DateTime): System.DateTime
        """
        pass
            
class StreamlabsCredentials(AnkhBotR2.Data.Discord.StreamlabsCredentials):
        """
        Attributes:
            UserId (String): System.String
        Oauth (String): System.String
        SocketToken (String): System.String
        LegacyToken (String): System.String
        SpecialToken (String): System.String
        CurrencyCode (String): System.String
        CreatedAt (DateTime): System.DateTime
        """
        pass
            
class OBSCredentials(AnkhBotR2.Data.OBSCredentials):
        """
        Attributes:
            IP (String): System.String
        Port (String): System.String
        Password (String): System.String
        """
        pass
            
class ExtraLifeCredentials(AnkhBotR2.Helpers.Data.Credentials.ExtraLifeCredentials):
        """
        Attributes:
            ParticipantId (String): System.String
        TeamId (String): System.String
        """
        pass
            
class StreamlabsPageSettings(AnkhBotR2.Helpers.Data.Streamlabs.StreamlabsPageSettings):
        """
        Attributes:
            Enabled (Boolean): System.Boolean
        ShowCommands (Boolean): System.Boolean
        ShowSonglist (Boolean): System.Boolean
        ShowPlaylist (Boolean): System.Boolean
        ShowQueue (Boolean): System.Boolean
        ShowQuotes (Boolean): System.Boolean
        PrimaryAccount (String): System.String
        """
        pass
            
class ChatBotDatabase(AnkhBotR2.Datamodels.ChatBotDatabase):
        """
        Attributes:
            Scripts (ITable`1): LinqToDB.ITable`1[AnkhBotR2.Datamodels.Script]
        BlacklistedSongs (ITable`1): LinqToDB.ITable`1[AnkhBotR2.Datamodels.BlacklistedSong]
        BlacklistedWords (ITable`1): LinqToDB.ITable`1[AnkhBotR2.Datamodels.BlacklistedWord]
        Bosses (ITable`1): LinqToDB.ITable`1[AnkhBotR2.Datamodels.Boss]
        Commands (ITable`1): LinqToDB.ITable`1[AnkhBotR2.Datamodels.Command]
        Currencies (ITable`1): LinqToDB.ITable`1[AnkhBotR2.Datamodels.Currency]
        Events (ITable`1): LinqToDB.ITable`1[AnkhBotR2.Datamodels.Event]
        GameWispSubscribers (ITable`1): LinqToDB.ITable`1[AnkhBotR2.Datamodels.GameWispSubscriber]
        Giveaways (ITable`1): LinqToDB.ITable`1[AnkhBotR2.Datamodels.Giveaway]
        Queues (ITable`1): LinqToDB.ITable`1[AnkhBotR2.Datamodels.Queue]
        Quotes (ITable`1): LinqToDB.ITable`1[AnkhBotR2.Datamodels.Quote]
        ExtraQuotes (ITable`1): LinqToDB.ITable`1[AnkhBotR2.Datamodels.ExtraQuote]
        Ranks (ITable`1): LinqToDB.ITable`1[AnkhBotR2.Datamodels.Rank]
        SoundFiles (ITable`1): LinqToDB.ITable`1[AnkhBotR2.Datamodels.SoundFile]
        StreamEvents (ITable`1): LinqToDB.ITable`1[AnkhBotR2.Datamodels.StreamEvent]
        Timers (ITable`1): LinqToDB.ITable`1[AnkhBotR2.Datamodels.Timer]
        TwitchFollowers (ITable`1): LinqToDB.ITable`1[AnkhBotR2.Datamodels.TwitchFollower]
        TwitchSubscribers (ITable`1): LinqToDB.ITable`1[AnkhBotR2.Datamodels.TwitchSubscriber]
        Users (ITable`1): LinqToDB.ITable`1[AnkhBotR2.Datamodels.User]
        WhitelistedLinks (ITable`1): LinqToDB.ITable`1[AnkhBotR2.Datamodels.WhitelistedLink]
        HostTargets (ITable`1): LinqToDB.ITable`1[AnkhBotR2.Datamodels.HostTarget]
        ConfigurationString (String): System.String
        DataProvider (IDataProvider): LinqToDB.DataProvider.IDataProvider
        ConnectionString (String): System.String
        ID (Int32): System.Int32
        IsMarsEnabled (Boolean): System.Boolean
        OnTraceConnection (Action`1): System.Action`1[LinqToDB.Data.TraceInfo]
        Connection (IDbConnection): System.Data.IDbConnection
        CommandTimeout (Int32): System.Int32
        Command (IDbCommand): System.Data.IDbCommand
        Transaction (IDbTransaction): System.Data.IDbTransaction
        MappingSchema (MappingSchema): LinqToDB.Mapping.MappingSchema
        InlineParameters (Boolean): System.Boolean
        QueryHints (List`1): System.Collections.Generic.List`1[System.String]
        NextQueryHints (List`1): System.Collections.Generic.List`1[System.String]
        """
        pass
            
class Localization(AnkhBotR2.Helpers.Data.Localization.Localization):
        """
        Attributes:
            CommandLoc (LocCommand): AnkhBotR2.Helpers.Data.Localization.LocCommand
        TimerLoc (LocTimer): AnkhBotR2.Helpers.Data.Localization.LocTimer
        HostLoc (LocHost): AnkhBotR2.Helpers.Data.Localization.LocHost
        QuoteLoc (LocQuote): AnkhBotR2.Helpers.Data.Localization.LocQuote
        CurrencyLoc (LocCurrency): AnkhBotR2.Helpers.Data.Localization.LocCurrency
        GiveAwayLoc (LocGiveAway): AnkhBotR2.Helpers.Data.Localization.LocGiveAway
        BettingLoc (LocBet): AnkhBotR2.Helpers.Data.Localization.LocBet
        PollLoc (LocPoll): AnkhBotR2.Helpers.Data.Localization.LocPoll
        SongLoc (LocSong): AnkhBotR2.Helpers.Data.Localization.LocSong
        DeathLoc (LocDeath): AnkhBotR2.Helpers.Data.Localization.LocDeath
        QueueLoc (LocQueue): AnkhBotR2.Helpers.Data.Localization.LocQueue
        DiscordLoc (LocDiscord): AnkhBotR2.Helpers.Data.Localization.LocDiscord
        """
        pass
            
    