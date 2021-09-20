import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='Warning: could not send message for past 8 hours',
    from_='MAILER-DAEMON@tppppp.com.au',
    to=('jennifer@sss.sssssss.net.au',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2008, 1, 17, 3, 40, 52, tzinfo=datetime.timezone(datetime.timedelta(0, 39600))),
    date_str='Thu, 17 Jan 2008 03:40:52 +1100',
    text='    **********************************************\r\n    **      THIS IS A WARNING MESSAGE ONLY      **\r\n    **  YOU DO NOT NEED TO RESEND YOUR MESSAGE  **\r\n    **********************************************\r\n\r\nThe original message was received at Wed, 16 Jan 2008 19:38:07 +1100\r\nfrom 60-0-0-61.static.tppppp.com.au [60.0.0.61]\r\n\r\nThis message was generated by mail11.tppppp.com.au\r\n\r\n   ----- Transcript of session follows -----\r\n.... while talking to mail.oooooooo.com.au.:\r\n>>> DATA\r\n<<< 452 4.2.2 <fraser@oooooooo.com.au>... Mailbox full\r\n<fraser@oooooooo.com.au>... Deferred: 452 4.2.2 <fraser@oooooooo.com.au>... Mailbox full\r\n<<< 503 5.0.0 Need RCPT (recipient)\r\nWarning: message still undelivered after 8 hours\r\nWill keep trying until message is 5 days old\r\n\r\n-- \r\nThis message has been scanned for viruses and\r\ndangerous content by MailScanner, and is\r\nbelieved to be clean.\r\n\r\n',
    html='',
    headers={'return-path': ('<mail_dump@ns1.sssssss.net.au>',), 'received': ('from acomputer ([unix socket])\r\n\t by imap01.sssssss.net (Cyrus) with LMTPA;\r\n\t Wed, 16 Jan 2008 13:51:42 -0800', 'from smtp.sssssss.org (unknown [198.0.0.92])\r\n\tby imap01.sssssss.net (Postfix) with ESMTP id BFE6477FAE\r\n\tfor <aaaa@sssssss.net>; Wed, 16 Jan 2008 13:51:40 -0800 (PST)', 'from ns1.sssssss.net.au (ns1.sssssss.net.au [202.0.0.246])\r\n\tby smtp.sssssss.org (Postfix) with ESMTP id 96E5C6C6830\r\n\tfor <aaaa@sssssss.net>; Wed, 16 Jan 2008 11:08:14 -0800 (PST)', 'from ns1.sssssss.net.au (unknown [127.0.0.1])\r\n\tby ns1.sssssss.net.au (Postfix) with ESMTP id E1BCEF227\r\n\tfor <aaaa@sssssss.net>; Thu, 17 Jan 2008 03:40:53 +1100 (EST)', 'from ns1.sssssss.net.au (ns1.sssssss.net.au [202.0.0.246])\r\n        by localhost (FormatMessage) with SMTP id ceaa681bbcb6c7f6\r\n        for <jennifer@sss.sssssss.net.au>; Thu, 17 Jan 2008 03:40:53 +1100 (EST)', 'from mail11.tppppp.com.au (unknown [203.0.0.161])\r\n\tby ns1.sssssss.net.au (Postfix) with ESMTP id 7F2D2F225\r\n\tfor <jennifer@sss.sssssss.net.au>; Thu, 17 Jan 2008 03:40:52 +1100 (EST)', 'from localhost (localhost)\r\n\tby mail11.tppppp.com.au (envelope-from MAILER-DAEMON) (8.14.2/8.14.2) id m0GFZ1c3009410;\r\n\tThu, 17 Jan 2008 03:40:52 +1100'), 'x-sieve': ('CMU Sieve 2.2',), 'date': ('Thu, 17 Jan 2008 03:40:52 +1100',), 'from': ('Mail Delivery Subsystem <MAILER-DAEMON@tppppp.com.au>',), 'message-id': ('<200801161640.m0GFZ1c3009410@mail11.ttttt.com.au>',), 'to': ('<jennifer@sss.sssssss.net.au>',), 'mime-version': ('1.0',), 'content-type': ('multipart/report; report-type=delivery-status;\r\n\tboundary="m0GFZ1c3009410.1200501652/mail11.ttttt.com.au"',), 'subject': ('Warning: could not send message for past 8 hours',), 'auto-submitted': ('auto-generated (warning-timeout)',), 'resent-date': ('Thu, 17 Jan 2008 03:40:53 +1100 (EST)',), 'resent-from': ('<mail_dump@ns1.sssssss.net.au>',), 'resent-to': ('<mikel@sssssss.net>',), 'resent-message-id': ('<ceaa681bbcb6c7f6.1200501653@sssssss.net.au>',), 'x-spam-status': ('No',)},
    attachments=[],
    from_values=EmailAddress('Mail Delivery Subsystem', 'MAILER-DAEMON@tppppp.com.au', 'Mail Delivery Subsystem <MAILER-DAEMON@tppppp.com.au>'),
    to_values=(EmailAddress('', 'jennifer@sss.sssssss.net.au', 'jennifer@sss.sssssss.net.au'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)