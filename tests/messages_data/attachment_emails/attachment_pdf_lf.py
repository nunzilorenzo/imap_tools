import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Another PDF with 🎉 Unicode chars in it 🍿',
    from_='xxxx@xxxx.com',
    to=('xxxx@xxxx.com', 'xxxx@xxxx.com'),
    cc=(),
    bcc=(),
    reply_to=('xxxx@xxxx.com',),
    date=datetime.datetime(2005, 5, 10, 11, 26, 39, tzinfo=datetime.timezone(datetime.timedelta(-1, 64800))),
    date_str='Tue, 10 May 2005 11:26:39 -0600',
    text='Just attaching another PDF, here, to see what the message looks like,\nand to see if I can figure out what is going wrong here.\n',
    html='',
    headers={'return-path': ('<xxxx@xxxx.com>',), 'x-original-to': ('xxxx@xxxx.com',), 'delivered-to': ('xxxx@xxxx.com',), 'received': ('from localhost (localhost [127.0.0.1])\n\tby xxx.xxxxx.com (Postfix) with ESMTP id 50FD3A96F\n\tfor <xxxx@xxxx.com>; Tue, 10 May 2005 17:26:50 +0000 (GMT)', 'from xxx.xxxxx.com ([127.0.0.1])\n by localhost (xxx.xxxxx.com [127.0.0.1]) (amavisd-new, port 10024)\n with LMTP id 70060-03 for <xxxx@xxxx.com>;\n Tue, 10 May 2005 17:26:49 +0000 (GMT)', 'from xxx.xxxxx.com (xxx.xxxxx.com [69.36.39.150])\n\tby xxx.xxxxx.com (Postfix) with ESMTP id 8B957A94B\n\tfor <xxxx@xxxx.com>; Tue, 10 May 2005 17:26:48 +0000 (GMT)', 'from xxx.xxxxx.com (xxx.xxxxx.com [64.233.184.203])\n\tby xxx.xxxxx.com (Postfix) with ESMTP id 9972514824C\n\tfor <xxxx@xxxx.com>; Tue, 10 May 2005 12:26:40 -0500 (CDT)', 'by xxx.xxxxx.com with SMTP id 68so1694448wri\n        for <xxxx@xxxx.com>; Tue, 10 May 2005 10:26:40 -0700 (PDT)', 'by 10.54.96.19 with SMTP id t19mr621017wrb;\n        Tue, 10 May 2005 10:26:39 -0700 (PDT)', 'by 10.54.110.5 with HTTP; Tue, 10 May 2005 10:26:39 -0700 (PDT)'), 'domainkey-signature': ('a=rsa-sha1; q=dns; c=nofws;\n        s=beta; d=xxxxx.com;\n        h=received:message-id:date:from:reply-to:to:subject:mime-version:content-type;\n        b=g8ZO5ttS6GPEMAz9WxrRk9+9IXBUfQIYsZLL6T88+ECbsXqGIgfGtzJJFn6o9CE3/HMrrIGkN5AisxVFTGXWxWci5YA/7PTVWwPOhJff5BRYQDVNgRKqMl/SMttNrrRElsGJjnD1UyQ/5kQmcBxq2PuZI5Zc47u6CILcuoBcM+A=',), 'message-id': ('<xxxx@xxxx.com>',), 'date': ('Tue, 10 May 2005 11:26:39 -0600',), 'from': ('Test Tester <xxxx@xxxx.com>',), 'reply-to': ('Test Tester <xxxx@xxxx.com>',), 'to': ('xxxx@xxxx.com, xxxx@xxxx.com',), 'subject': ('Another PDF with \udcf0\udc9f\udc8e\udc89 Unicode chars in it \udcf0\udc9f\udc8d\udcbf',), 'mime-version': ('1.0',), 'content-type': ('multipart/mixed; \n\tboundary="----=_Part_2192_32400445.1115745999735"',), 'x-virus-scanned': ('amavisd-new at textdrive.com',)},
    attachments=[
        dict(
            filename='broken.pdf',
            content_id='',
            content_disposition='attachment',
            content_type='application/pdf',
            payload=b'%PDF-1.4\r\n%\xe4\xf6\xdc\xdf\r\n1 0 obj\r\n<< /Length 2 0 R\r\n   /Filter /FlateDecode\r\n>>\r\nstream\r\nx\x9c\xbdZ\xdd\x8a%\xb9\r\xbeo\xe8w\xa8\xeb\x85\x9cX\x96\x7faXHv\xa7\xef\x07\x06\xf2\x02\xc9&\x84\xc9\xc2\xeeM^?\xd6\'\xc9\xf6\xa9\xea\xd3\xd3iH\x18\xa6\xbb\xbe\xb2-K\xb2\xfe\xac\xeap\xfc\xfb\xf9\xe9\xb7#\x1c\x7f\x087:\n\xc5\xf1\xb3v\xf9\xf9\xfb\xdf\x8e\xbf\xfcp\xfc\xfa\xfc\x14n\xad\xb7\xc0\xc7\xf9\xf7\xef\x7f\x7f~\xe2r\x94\x9en\xe5\xf8\xd7\xf3S\xae\x0e\xbe\x1dx\xae\x01\xcf|\xffh3\xfe\xf1\xfc\xf4\xcb\x0f \xd0\xe7\xea\xeeKk\xd4\xc9\xfe\xbbo+\xbe\x1c\xbf\x8dW\x83A&\xbe\xf5\x83J\x1c\xff\xe9\xc6;\xc35\xf5@\xc7\xf9\xb70\\\xf9\xe0XoM\xb6\xacy\xacb\x0e\x83v-\xe3\x153\x0f\xb2\x03\xb4[\x1d \x83\xcf\x16ni\x80v\x13V\x1a\xcb\xb4\x14\xc7\xcfo\xcfO\xad\xc8P\xca2P\x07+\x9c\xaa.i\xe3\x17\xe78F1"@\x85\x1e+\x06\xe5\\\xc7\xbe\x02\xc6c7Ry\xc8d\x0b\xe41\xe9\x0cy,\xba\xb3<\xd6\xb1z<\xa6\x9b\x80\xae\xb3\x01\xaa\xc8\x0f2"Q\x8d\xb7\xac\x9b\r\xf6*+\x00O5\xe9\xa2.\xea[ \x01\xd4\x05\xb2\xe8a\x90s\x94\x16\x05c\xa7a\xa32\xa4\x9e\xc0\x84\xd75\r\xbb\x8e\xb3\x1eji \xd6\xb3\xc8\xde"\xd6\x1b`\x88i A\xf9]v\xe3\x96\x15D\x80\x86m\xbaX(w6Q!C\x97\xa34\xf5\xa7\x10U\x06!\x97\x02+\x90\x13K!+\xd7\x84iE\xd7\x08\xb9\x14p\xb0\xc3\x16d\xa0cI\x95W\x89\x08K*(\x0f\xb7`\x05y\x00\xc6\xfa*G\x9a\xa8BP\x98R\x8aAO\x13\xd6\x94b\xda(D\xd5\x8e\x02\x0e\xba\xa8`QWb2I9\xabl\xcb;\x88\xf1"%\xcaK\xb1)3"mb\xbc\x1fS\xe0\x12\xfa\x98\x82\xce\x06\x99\x04\xab\x122@jX\x06\x8a\xb2!\x8aO\xa9\xe1\x94\r\xf4M\xc4LS\xc0\x1cM[\xf2\x9au\x97\xfd\x11sX%}\x0b4\x00\x15\xaf\xca\x86Y\xcdO\x15\x9c\xf5\xf0UW\x0e\xf4\x11,\xca1\th\xee\x9e\x06\x86Q\xc8\xa1\xa5\xac\xaa\x18\xa0\xec\xa0\x03\xc0F#807tP\xd7\x9a.\x8a\x01\xb9\x89\xd6P\x7f\x1d\x94\xe06\xf6\n\xa8\x8b;E\x87\x01\x9a2\x94h\x82\x02\xa8g\x88\xd4#\x164\x0fJI\xa3\xc1\xf3S\x81\x0e\x8c\xd4\x88~yj7\xeb\x01f\x8c\x8cC%\x98\x86P\x18\x96\xb0\x0c\x91\xc5}\xc4zA\x8e\x8b9\x06#\xde\x8e\x97\xdc\xd5e0"\xbe)\x14F\x14l\x1e\x1d\x84\xdc\x98V2\x94\x93d)\xe7\xa2z\xcb\x84\xc0\xa8v\n\xcdr\n8\xbb"T%\xce\xaa\x9d[,\x9e\xb1\x9d\xd4\xfbk\xd1\x8c"\xb0#\x98\xc8\x86\xd4\xc1X\xd5\xe3\x10T4\xb6\xe0\xb9#\xb6`{\xa3\xa2p\x0c&C\x1dH\x8e\xdb#\x0fu\x02J\xb6\x01ILQa\x85L\xc0\x0ejh\xd4:\xf6P\x0b\x12$cjB\xa4\xc1h\xfc\x8c\x0buR\xc7\xb3\xa9\xddw\x04\xd1\xae\n\x15n\xf2\xd4\xf5\xe0t\x1b\x81\x0c\x9d\xd5tL\xda1\x1d\xbbw$\x15\xb0+\xa8a\xbfx\x87|;E\xca\x89\x01\xdfM\x88\xa4@S\x9db\x02u\xee.a\xcf\xf5\x92\x10\xdbH\x89\x10\xa2\x93\xba\x95\xca\x9a\x98`n\xd4\xe4\x84\xdc\xdeH=+\x19_M\x02\x91!\xd1\x8a,\xb1\xe8t\x08J\x1b\x12\x1d%M\xb3\x07U\xb1\xa3\x94H\x05\xaa\xf5\xa6!\x0e\xd1\x83j\x81\xb9kyA\x1aF-\xfeQe\x04[uR\xaa\xd8\x9f5mR\x95\x10\x9c\xb8\x99z\x8b\x8a\x81\xfdJ\x85\x10U\x89\x14d\x13\x17\xa9$,\xd3\xc0I\x85\r\xa9HE\xb2\xc4\x1a\xdc4\x81\xfaDH\xeaH\x00_\xcd\x9e\x93\xf3qP\x86\xf3\xab4\x83`\xeeK\'x\xd6\xe8M\x19\xb1 i*\xd6\x11s\x91\x12\xb6\xf0',
        ),
        ],
    from_values=EmailAddress('Test Tester', 'xxxx@xxxx.com', 'Test Tester <xxxx@xxxx.com>'),
    to_values=(EmailAddress('', 'xxxx@xxxx.com', 'xxxx@xxxx.com'), EmailAddress('', 'xxxx@xxxx.com', 'xxxx@xxxx.com')),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(EmailAddress('Test Tester', 'xxxx@xxxx.com', 'Test Tester <xxxx@xxxx.com>'),),
)