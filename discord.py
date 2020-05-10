class Member():
    __units__ = ["name", "roles"]

    def __init__(self, name):
        self.name = name
        self.roles = []


class Role():
    __units__ = ["name", "perms"]

    def __init__(self, name):
        self.name = name
        self.perms = 0


class Permission():
    __units__ = ["value", "name", "desc"]

    def __init__(self, *, value, name, desc):
        self.value = value
        self.name = name
        self.desc = desc


members = [
    Member("Natalie"),
    Member("Solace"),
    Member("Kane"),
    Member("Friend"),
    Member("Stranger")
]

roles = [
    Role("Overseer"),
    Role("Inquisitor"),
    Role("Court Wizard"),
    Role("Denizen")
]

permissions = [
    Permission(value=0x00000008, name="ADMINISTRATOR", desc="Administrator"),
    Permission(value=0x00000080, name="VIEW_AUDIT_LOG", desc="View Audit Log"),
    Permission(value=0x00000020, name="MANAGE_GUILD", desc="Manage Server"),
    Permission(value=0x10000000, name="MANAGE_ROLES", desc="Manage Roles"),
    Permission(value=0x00000010, name="MANAGE_CHANNELS", desc="Manage Channels"),
    Permission(value=0x00000002, name="KICK_MEMBERS", desc="Kick Members"),
    Permission(value=0x00000004, name="BAN_MEMBERS", desc="Ban Members"),
    Permission(value=0x00000001, name="CREATE_INSTANT_INVITE", desc="Create Invite"),
    Permission(value=0x04000000, name="CHANGE_NICKNAME", desc="Change Nickname"),
    Permission(value=0x08000000, name="MANAGE_NICKNAMES", desc="Manage Nicknames"),
    Permission(value=0x40000000, name="MANAGE_EMOJIS", desc="Manage Emojis"),
    Permission(value=0x20000000, name="MANAGE_WEBHOOKS", desc="Manage Webhooks"),
    Permission(value=0x00000400, name="VIEW_CHANNEL", desc="Read Text Channels & See Voice Channels"),
    Permission(value=0x00000800, name="SEND_MESSAGES", desc="Send Messages"),
    Permission(value=0x00001000, name="SEND_TTS_MESSAGES", desc="Send TTS Messages"),
    Permission(value=0x00002000, name="MANAGE_MESSAGES", desc="Manage Messages"),
    Permission(value=0x00004000, name="EMBED_LINKS", desc="Embed Links"),
    Permission(value=0x00008000, name="ATTACH_FILES", desc="Attach Files"),
    Permission(value=0x00010000, name="READ_MESSAGE_HISTORY", desc="Read Message History"),
    Permission(value=0x00020000, name="MENTION_EVERYONE", desc="Mention @everyone, @here, and All Roles"),
    Permission(value=0x00040000, name="USE_EXTERNAL_EMOJIS", desc="Use External Emojis"),
    Permission(value=0x00000040, name="ADD_REACTIONS", desc="Add Reactions"),
    Permission(value=0x00100000, name="CONNECT", desc="Connect"),
    Permission(value=0x00200000, name="SPEAK", desc="Speak"),
    Permission(value=0x00000200, name="STREAM", desc="Video"),
    Permission(value=0x00400000, name="MUTE_MEMBERS", desc="Mute Members"),
    Permission(value=0x00800000, name="DEAFEN_MEMBERS", desc="Deafen Members"),
    Permission(value=0x01000000, name="MOVE_MEMBERS", desc="Move Members"),
    Permission(value=0x02000000, name="USE_VAD", desc="Use Voice Activity"),
    Permission(value=0x00000100, name="PRIORITY_SPEAKER", desc="Priority Speaker")
]
