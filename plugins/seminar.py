# coding: utf-8

from slackbot.bot import listen_to
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pydrive.files import ApiRequestError

DOMAIN = 'hamadalab.com'

# hamadalab限定のファイルであればTrueを返す
def is_file_for_domain_members(drive_id):
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile('credentials.json')

    drive = GoogleDrive(gauth)
    file = drive.CreateFile({'id': drive_id})

    try:
        file.FetchMetadata(fields='permissions')
    except ApiRequestError:
        # ファイルが存在しない or アクセス権限がない or IDがディレクトリを指している
        return False

    # hamadalab内のファイルであればTrue
    return any(
        'domain' in p and
        p['domain'] == DOMAIN
        for p in file['permissions'])

@listen_to(r'https://drive\.google\.com/?(open\?id=|drive/folders/|file/d/)([0-9a-zA-Z_\-]+)')
def drive_helper(message, filetype, drive_id):

    if is_file_for_domain_members(drive_id):
        good_url = f'https://drive.google.com/a/{DOMAIN}/'+ filetype + drive_id
    else:
        return False
    message.reply(good_url, in_thread=True)

#https://drive.google.com/open?id=13a_J9c8oKKR3bgx4WTe8Rh2-a3CvGfjS
#https://drive.google.com/drive/folders/1G8H2TqsW32WhCgvyLambhAFIR-gwY9sy
