import datetime
from imap_tools import EmailAddress

DATA = dict(
    subject='test',
    from_='samgentlemankaka@foxmail.com',
    to=('qmebi@mfk.app',),
    cc=(),
    bcc=(),
    reply_to=(),
    date=datetime.datetime(2020, 10, 21, 11, 34, 9, tzinfo=datetime.timezone(datetime.timedelta(0, 28800))),
    date_str='Wed, 21 Oct 2020 11:34:09 +0800',
    text='',
    html='<meta http-equiv="Content-Type" content="text/html; charset=GB18030"><div><img src="cid:F76361FC@E3C5215F.31AC8F5F.png" style="" id="img_insert_160325124624005018289219499459"><br><br></div>',
    headers={'return-path': ('<samgentlemankaka@foxmail.com>',), 'x-original-to': ('qmebi@mfk.app',), 'delivered-to': ('qmebi@mfk.app',), 'received': ('from qq.com (unknown [113.96.223.80])\r\n\tby mail.mfk.app (Postfix) with ESMTP id DD4B62140DD4\r\n\tfor <qmebi@mfk.app>; Wed, 21 Oct 2020 03:34:11 +0000 (UTC)', 'from qq.com (unknown [127.0.0.1])\r\n\tby smtp.qq.com (ESMTP) with SMTP\r\n\tid ; Wed, 21 Oct 2020 11:34:10 +0800 (CST)'), 'dkim-signature': ('v=1; a=rsa-sha256; c=relaxed/relaxed; d=foxmail.com;\r\n\ts=s201512; t=1603251251;\r\n\tbh=bZSz/mtqfdz94kmtGaFYXC+YAQiOxaGFSWBJgZKsdU4=;\r\n\th=From:To:Subject:Mime-Version:Date:Message-ID;\r\n\tb=bHrL4mJuop2NculsqdAgtZBTFjvA8VK2WqfJwn4MqmVpNUvfUQ/OyCzC7WAG2DjDq\r\n\t NhaAt5+61RCFDBKuv2NVx7xyH7xPTI0xVrCbUZinXDQQ53r6vBwP08jwx4GaP+b4k6\r\n\t WYypqGbGKA2pDDUKmsABkHWdG2QbANM0YDCLnlBM=',), 'x-qq-feat': ('AU3gs7VM8fUm1shbPQ2y/acBleNQwil+zNLsynIgszFw26Mnhh/EwwA+B+R36\r\n\tyfTKfZtupqkoghvYDKTdaoIJHPvl3hwvMYCK5O0pgoIgbwuFYw2V5fn3Gldt7UXsU6U7tyH\r\n\twqWfCV4fZ445hfnnbUWSDNVElNzvEyQ+KXbeWoY8wscD6YadaE8uZDImlxSshpPqQ6QZ+Hv\r\n\tLAH0CFTPcbU0pVX7JZWe+yehkkfGa8pNbg2udDcM+l2It8FiRxZE1Dd/e+eLR6ZeHxrSdcF\r\n\tzsYA==',), 'x-qq-ssf': ('00000000000000F100000000000000J',), 'x-qq-xmailinfo': ('MKhv4vGKTxZzZwBiOOWzJjOs1CMM2urx0EOWlCdHAK4tftFk+6UX7CdZHFmrau\r\n\t guT9pUXQHsD4SoKYAbJJgAkezWTcclYEtZ5xC4nTjAObSp7hATM9Wz70KG1uocKqaXQT7MJP0sc9c\r\n\t bpSK6QNPNd3+j7/BptWtYSJjEQSs7BFqvSDf3T7b1gPmf14cCPF4OGaIV332nu7Yfv6UeJDuMtM8E\r\n\t V8WKUfbWqjedOX7j/4mx94I9GBJK7MwebhIqqVST1wrdrAckfU+wzSRmn+GsvqRnYuog5vBEtUjMW\r\n\t dHVOpXPD3GtA0tqfs3mbYyV45ix3wR5P3AQQoVgyyFiIMVWW2Ro/pCCxW4t8IGJLDWtm7SE1x+n5l\r\n\t ovf0oGXFRVI14LDD6ANU8IspSEEhCNBy8VY8j4nAIbME2fbMvnlP65Ypa9e7HpLYcaJryAp/z0qh2\r\n\t qUVXkbM7NBGR/gQfTjUa9HduSGNfUAdrPy/PCFyUr6TzuKfWdv1oaHe5muNm91NtaCZdPcy+bTNYf\r\n\t oI6eyoMTJflL8zriZXN7PjVgtZBrRkuGLDBBphNYVLKnqW0Pf9UQf46pCuQvvneVPqSb3pSzoy+O2\r\n\t fiO8+pRyy/J/L9YrHExFlgz38D8S1qYzUq5nGEBOvkTiaJZfu/ie5Gmv0a8W0CkWEqmNgGCg556Wr\r\n\t cSs9YFvPuleEF6mSFSzbj7R1dz4Q==',), 'x-has-attach': ('no',), 'x-qq-business-origin': ('2',), 'x-originating-ip': ('112.80.214.47',), 'x-qq-style': ('',), 'x-qq-mid': ('webmail615t1603251249t9058947',), 'from': ('"=?ISO-8859-1?B?c2g=?=" <samgentlemankaka@foxmail.com>',), 'to': ('"=?ISO-8859-1?B?cW1lYmk=?=" <qmebi@mfk.app>',), 'subject': ('test',), 'mime-version': ('1.0',), 'content-type': ('multipart/related;\r\n\ttype="multipart/alternative";\r\n\tboundary="----=_NextPart_5F8FAC31_11789E80_23290B52"',), 'content-transfer-encoding': ('8Bit',), 'date': ('Wed, 21 Oct 2020 11:34:09 +0800',), 'x-priority': ('3',), 'message-id': ('<tencent_DF1A0C2499D7CA259C7FB26CDFCB49C60809@qq.com>',), 'x-qq-mime': ('TCMime 1.0 by Tencent',), 'x-mailer': ('QQMail 2.x',), 'x-qq-mailer': ('QQMail 2.x',), 'x-qq-sendsize': ('520',), 'feedback-id': ('webmail:foxmail.com:bgweb:bgweb17',)},
    attachments=[
        dict(
            filename='F76361FC@E3C5215F.31AC8F5F.png.jpg',
            content_id='F76361FC@E3C5215F.31AC8F5F.png',
            content_disposition='',
            content_type='image/jpeg',
            payload=b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00s\x00\x00\x001\x08\x06\x00\x00\x00\xe9\xd3\x96\x81\x00\x00\x03ZIDATx\x01\xed\x9bAh\x13A\x14\x86\xffhA\x0cT\xa4\xa9P\xc9A\x8a\x17%\x97\xf4\xe4!t!\xe4fo\x1e\x02\x01o\x81B x\xec)x(9\xe5$\xa5\x10\x08\xf4&\x88\x01{\xab\x07A\x8a\t9xR\x84\x90\x16\t\xa2RZ\xb0\xf1\xa0\x10\xf1 \x91\xd9\xec\xa6;\xb3\t\xd6N\xb0o\xc6\x17\x08\xc9\x9b\x9d\x9d\xbc\xf7\x7f\xf3\xde\xce\x0e\x9bH\xe5\xf9\xe1\x00\xfc\xb2B\x81\x0bVD\xc1A\xb8\n0L\x8b&\xc2\xcc\xfb\xee\x07\x8b\xc2\xf9\xbfC\x89\x0c\x06\x03\xbefZ2\x07\xb8\xccZ\x02R\x84\xc10\x19\xa6E\nX\x14\ng&\xc3\xb4H\x01\x8bB\xe1\xcc\xb4\x08\xe6\x8c\x1aK\xbf\xdf\xc7\x97\x1f\x17\xd5f\xb6\t)p\xed\xf2/D\xa3\xd1\x90G\xd2}\xe6\xc7\xde\xcfP\x07n\xa0\xab\xc0\x8d\xd8%\xc9\xb9Q\x99\x15\x19\xc9/\xb3\x14P\x99\x8d`ri5\x0b\xa4\xf0Ve6\x82i^(\xec\xb1\xaa\x00\xc3T\x151\xd8f\x98\x06\xc3S]g\x98\xaa"\x06\xdb\x0c\xd3`x\xaa\xeb\x0cSU\xc4`\x9ba\x1a\x0cOu=\xb4\x9d\xa7v\xf8\xe7v\xaf\x85\x87\xa56\x9a\xc1\x1fv\x1c\xec&\xbbHo\x1c\x04[\xbd\xef\xb3(\x95s\xc8\xc4\x86f\xfbI\r\xc5\x06\x90\x7f\xb0\x8a\xfb\xb7\xe5\xb6\xe5\xec=\xac\xa7\xe7\xc7\x8c\x01\x8c;Ot\x9c\xd4>v\x90sn\xa4\x9b\x99\x02`\xd5A^\x11H\x00\xd9\xad\xae\xba\xefMG9\x88=\xbci\x88\xb68\x96<\x90\xc2J$\xe3n\xc7f\xfd5\xda\xea)\x16\xd9\xf42SG\xdcN\x17[\xe2|\xe7*\x8e*5\x14C\xcf\xaa\x1d\xa0X\xa8\x9d\xfc\xc2b\x02\xcf\xd6R\x98;i1\xfa\x9bU0\xdbo\x87e8\x9fL!\x93K!s\x064[\x1b\xb5\xe1\x84P\xce\x95\xdaE\xd5\xc8\xddRz\x9c\xbfI\x17f\xa3\x81\xb4[2e\x91\x9a\xf5m\xa4\xebr\x9bk\xf5Zx\x1a\xec?\xee\xda+\x9d\x16\xc7fu\x05\t\xa9M\xbe\xd6*\x87\xc8\x9bta\xba\xb3\x1fx\\hH\x99\x12\\\xc4\xf8\x8b\x13\xa1r\xfb\x85\xb2h\x8a\xa5\xb0^M\x91\x070M\x07\xe9\xc2\xd4\x8d\xf2\x8c\x99)\x95S\xc9\x07y\xd5,\x1d"b\x18\x07sR\x99\xbd\xbe\x10G)\x0b\x94\xeb\xde\xed\xcb_e\xe61\x8e>\x0b"\xe3J\xef^\xa8:\x10a\x17r\xc3\x18\x98\xc3\xc5\x8d\x9c\x1d\xc12;\x97^A\xa6\xb3\x83\xb2\x1fbgg\xc2}\xa9\xdf!\x00\xae\xb7\x8fWb\xe5\xeb\xdc\x0c]C\xfd\xde&|\xd2\x85)-\x80\xba\xde\xfd\xe3\x15,x\x9b\x03\xa7\x167\xb4\xf2<\xc6\xcb\xca6\xca\x81\xdb\x96\xaf\xef>\xb9\x9b\x14\xf9$\xbd\x15\xea\xa9\xe3\x04@\x17\xe6\x08\x82\'>\x80\xe5\xec\x9d@\xe6\xf8\xa5\xf1\x0f\x80\xddI\x11\\\xe6*\xf2\xf4ZxT\xff\x0e,&p7\xb0\xd1\xa0\xf42\xc2\xa4\x073t\xad\x9bGf\xcd\xc1a\xa1\x8b%\xb1\x15\xa7,ld\xc0c4\x1fM\n\xff\x98\x9c\x99\xc3U\xf0,Jy\xf37\x0fFO\xe7\xf1\x93y>l\xb3>\x83O\xe8\xd1\xdd\x9b5KS\x12\xde2L\x12\x18\xa6\xe3\x04\xc3\x9c\x8e\x8e$F\x894\xf6\xbf\xf1?\xa7I\xa0\xd0w\x823S_C2#0L2(\xf4\x1da\x98\xfa\x1a\x92\x19\x81a\x92A\xa1\xef\x08\xc3\xd4\xd7\x90\xcc\x08\x0c\x93\x0c\n}G\x18\xa6\xbe\x86dF`\x98dP\xe8;\xc20\xf55$3\x02\xc3$\x83B\xdf\x91\xdf\xffr\xec\xc6\xdb\xb0\x1e\xeb\x00\x00\x00\x00IEND\xaeB`\x82',
        ),
        ],
    from_values=EmailAddress('sh', 'samgentlemankaka@foxmail.com', 'sh <samgentlemankaka@foxmail.com>'),
    to_values=(EmailAddress('qmebi', 'qmebi@mfk.app', 'qmebi <qmebi@mfk.app>'),),
    cc_values=(),
    bcc_values=(),
    reply_to_values=(),
)