# Prefixed to downloaded scripts
SCRIPT_PREFIX = "_scriptmanager."
# Notes with this tag will be touched by this addon
TAG_PREFIX = "managedscripts"
# Notes of these types will automatically have the TAG_PREFIX tag applied to them.
COMMON_VALID_NOTE_TYPES = ["Basic","Cloze","My Custom Type"]
# Adding scripts to this makes them available for updating and inserting into cards
SCRIPTS = {
    myjquery: { enabled: True, link: "http://code.jquery.com/jquery-latest.min.js", note_types = ["Basic"] },
    timestamp: { enabled: False, link: "https://gist.githubusercontent.com/seltzy/273b0cf6f78b870d0dda170773a498d4/raw/b86379b3d590422647e3d62e0b83e5090ec8f4e4/timestamp.js", note_types = ["Basic"]  },
}


# filepath = Editor._retrieveURL(self, url) seems to perform this
def Download(sid):
    # TODO
    return

def Delete(sid):
    # TODO
    return

def ReplaceOrInsert(note,sid):
    # TODO
    return

# Downloads latest versions of scripts, finds cards with scripts, and replaces/inserts the scripts on those cards
def UpdateScripts():
    # TODO
    return

def DisplayManagementInterface:
    # TODO
    return

def AddMenuButtons():
    # TODO
    return
